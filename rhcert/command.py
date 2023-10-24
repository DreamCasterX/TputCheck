# Copyright (c) 2006 Red Hat, Inc. All rights reserved. This copyrighted material
# is made available to anyone wishing to use, modify, copy, or
# redistribute it subject to the terms and conditions of the GNU General
# Public License v.2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Author: Greg Nichols
#
# Overview:
#    The Command class is a wrapper for shell commands that performs
#    validation and error checking.  Example usage can be seen in the
#    __main__ self test function at the end of this file.

import datetime
import json
import re
import subprocess
import sys

from commandxml import CommandXML
from tags import Constants


class Command:

    debug = None # None, Constants.off, Constants.low, Constants.high

    @classmethod
    def setDebug(cls, debug=Constants.high):
        cls.debug = debug

    @classmethod
    def isDebug(cls):
        return cls.debug and cls.debug != Constants.off

    @classmethod
    def getDebug(cls):
        return cls.debug

    def __init__(self, command):
        """ Creates a Command object that wraps the shell command
            via the supplied string, similar to os.system.   The
            constuctor does not actually execute the command.
        """
        self.command = command
        self.regex = None
        self.singleLine = True
        self.regexGroup = None
        self.raw_output = None
        self.output = None
        self.errors = None
        self.returnValue = 0
        self.signal = 0
        self.pipe = None

    def execute(self):
        # this  is the primitive for actually executing the command in a pipe to a subprocess
        # Using if/else instead of try/except due to the known bug in subprocess python 2.6.6
        # https://bugs.python.org/issue12085
        # Using [0] instead of .major because RHEL6 ships with python 2.6.6
        if sys.version_info[0] > 2:  # python3
            self.pipe = subprocess.Popen(self.command, shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         encoding='utf8',
                                         errors='replace')
        else:  # python2
            self.pipe = subprocess.Popen(self.command, shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        (output, errors) = self.pipe.communicate()
        if output:
            #Strip new line character/s if any from the end of output string
            output = output.rstrip('\n')
            self.raw_output = output
            self.output = output.splitlines()
        if errors:
            self.errors = errors.splitlines()
        self.signal = 0
        self.returnValue = 0
        if self.pipe.returncode < 0:
            self.signal = self.pipe.returncode
        else:
            self.returnValue = self.pipe.returncode

        # if called in a test run, sys.stdout is a rhcert.log.Log so dump XML there.
        try:
            sys.stdout.logOnly(CommandXML(self).toXML())
        except AttributeError:
            pass

    def get_json_output(self):
        data = {}
        if self.raw_output:
            data = json.loads(self.raw_output)
        return data

    def start(self):
        # Using if/else instead of try/except due to the known bug in subprocess python 2.6.6
        # https://bugs.python.org/issue12085
        # Using [0] instead of .major because RHEL6 ships with python 2.6.6
        if sys.version_info[0] > 2:  # python3
            self.pipe = subprocess.Popen(self.command, shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         encoding='utf8')
        else:  # python2
            self.pipe = subprocess.Popen(self.command, shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        # if called in a test run, sys.stdout is a rhcert.log.Log so dump XML there.
        try:
            sys.stdout.logOnly(CommandXML(self).toXML())
        except AttributeError:
            pass

    def _checkErrors(self, ignoreWarnings=False):
        # non-zero return or signals raise ErrorReturn or Killed in preference to ErrorOutput
        self._checkReturnValue()

        if self.errors and len(self.errors) > 0:
            # when stderr reported warning not error and command succeed
            if ignoreWarnings:
                if self.returnValue != 0:
                    raise HwCertCommandErrorOutput(self, self.errors)
            else:
                raise HwCertCommandErrorOutput(self, self.errors)


    def _checkReturnValue(self):
        if self.returnValue != 0 or self.signal != 0:
            # if error returned, show stdout and stderr before raising exception
            self.printOutput()
            self.printErrors()
            if self.returnValue != 0:
                raise HwCertCommandErrorReturned(self, self.returnValue)
            if self.signal != 0:
                raise HwCertCommandErrorKilled(self, self.signal)


    def run(self, ignoreErrors=False, ignoreWarnings=False):
        """ run the command, logging stdout and stderr to CommandXML in log

            ignoreErrors: do not raise exceptions
            ignoreWarnings: do not raise an exception if there is stderr, but a zero return.
        """
        self.execute()
        if self.getDebug() == Constants.high: # replaces "echo" behavior
            self.printOutput()
        if not ignoreErrors:
            self._checkErrors(ignoreWarnings)
        return 0

    def echo(self, ignoreErrors=False, ignoreWarnings=False):
        """ DEPRECATED """
        return self.run(ignoreErrors, ignoreWarnings)

    def echoIgnoreErrors(self):
        """ DEPRECATED """
        return self.run(ignoreErrors=True)

    def echoIgnoreWarnings(self):
        """ DEPRECATED """
        return self.run(ignoreErrors=False, ignoreWarnings=True)

    def getIgnoreErrors(self):
        self.execute()
        return self.output

    def printOutput(self):
        if self.output:
            for line in self.output:
                sys.stdout.write( line )
                sys.stdout.write("\n")
            sys.stdout.flush()

    def printErrors(self):
        if self.errors:
            for line in self.errors:
                sys.stderr.write( line )
                sys.stderr.write("\n")
            sys.stderr.flush()

    def _getString(self, regex=None, regexGroup=None, singleLine=True, returnList=False, ignoreErrors=False, keyGroup=None, valueGroup=None):
        """
        Get the string from the command's output.  With default parameters
        it returns the command's single line of output as a string.

        If singleLine is True, and multiple lines are found in the output,
        HwCertCommandException is raised.

        The regex parameter allows the output to be searched for a regular
        expression match.  If no regexGroup is supplied, the entire pattern
        match is returned.   The regexGroup parameter allows named
        substrings of the match to be returned if regex has named groups
        via the "(?P<name>)" syntax.   If no match is found,
        HwCertCommandException is raised.

        Another capability is to construct a dictionary using keyGroup and
        valueGroup.  If no match is foud, HwCertCommandException is raised.
        """
        self.regex = regex
        self.singleLine = singleLine
        self.regexGroup = regexGroup

        self.execute()

        if self.singleLine:
            if self.output and len(self.output) > 1:
                raise HwCertCommandException(self, "Found %u lines of output, expected 1" % len(self.output))

            if self.output:
                line = self.output[0].strip()
                if not self.regex:
                    return line
                # otherwise, try the regex
                pattern = re.compile(self.regex)
                match = pattern.match(line)
                if match:
                    if self.regexGroup:
                        return match.group(self.regexGroup)
                    # otherwise, no group, return the whole line
                    return line

                # no regex match try a grep-style match
                if not self.regexGroup:
                    match = pattern.search(line)
                    if match:
                        return match.group()

            # otherwise
            raise HwCertCommandStringNotFound(self, "no match for regular expression %s" % self.regex)

        #otherwise, multi-line or single-line regex
        if not self.regex:
            raise HwCertCommandError(self, "no regular expression set for multi-line command")
        pattern = re.compile(self.regex)
        result = None
        if returnList:
            result = list()
        if keyGroup and valueGroup:
            result = dict()
        if self.output:
            for line in self.output:
                if self.regexGroup:
                    match = pattern.match(line)
                    if match:
                        if returnList:
                            result.append(match.group(self.regexGroup))
                        else:
                            return match.group(self.regexGroup)
                elif keyGroup and valueGroup:
                    match = pattern.match(line)
                    if match:
                        keyMatch = match.group(keyGroup)
                        valueMatch = match.group(valueGroup)
                        result[keyMatch] = valueMatch
                else:
                    # otherwise, return the matching line
                    match = pattern.search(line)
                    if match:
                        if returnList:
                            result.append(match.group())
                        else:
                            return match.group()
            if result:
                return result

        # otherwise
        raise HwCertCommandStringNotFound(self, "no match for regular expression %s" % self.regex)

    def getStringDict(self, regex=None, ignoreErrors=False, keyGroup=None, valueGroup=None, ignoreWarnings=False):
        """ like getStringList, except return a dictionary with matches for keygroup and valuegroup."""
        result = self._getString(regex, keyGroup=keyGroup, valueGroup=valueGroup, singleLine=False)
        if not ignoreErrors:
            self._checkErrors(ignoreWarnings)
        return result

    def getStringList(self, regex=None, regexGroup=None, ignoreErrors=False, ignoreWarnings=False):
        """ like getString, except return a complete list of matches on multiple lines."""
        result = self._getString(regex, regexGroup, singleLine=False, returnList=True)
        if not ignoreErrors:
            self._checkErrors(ignoreWarnings)
        return result

    def getString(self, regex=None, regexGroup=None, singleLine=True,  ignoreErrors=False, ignoreWarnings=False):
        """ like getString, except return a complete list of matches on multiple lines."""
        result = self._getString(regex, regexGroup, singleLine, returnList=False)
        if not ignoreErrors:
            self._checkErrors(ignoreWarnings)
        return result

    def getInteger(self, regex=None, regexGroup=None, singleLine=True,  ignoreErrors=False, ignoreWarnings=False):
        """
        getInteger is the same as getString, except the output is required to
        be an Integer.
        """
        value = self.getString(regex, regexGroup, singleLine,  ignoreErrors, ignoreWarnings)
        return int(value)

    def getPID(self):
        if self.pipe:
            return self.pipe.pid
        raise HwCertCommandException(self.command, "call to getPID() before start()")

    def readline(self):
        if self.pipe:
            return self.pipe.stdout.readline()
        raise HwCertCommandException(self.command, "call to readline() before start()")

    def poll(self):
        if self.pipe:
            return self.pipe.poll()
        # otherwise, command never started
        raise HwCertCommandException(self.command, "call to poll() before start()")


# HwCert Command Exceptions:
# These exceptions are organized in a type hierarch to allow different levels of exceptions
# to be caught and handled:
#
#    HwCertCommandException                - all exceptions raised by Command
#        HwCertCommandError                - commands that either returned non-zero, or were killed
#            HwCertCommandErrorReturned    - commands that returned non-zero
#            HwCertCommandErrorKilled      - commands that were killed via signal
#        HwCertCommandErrorOutput          - commands that had output on stderr
#        HwCertCommandStringNotFound       - commands where regex string matches failed


class HwCertCommandException(Exception):
    def __init__(self, command, message):
        self.message = message
        self.command = command

    def __str__(self):
        return "\"%s\" %s" % (self.command.command, self.message)

    # BaseException.message has been deprecated since Python 2.6.  To prevent
    # DeprecationWarning from popping up over this pre-existing attribute, use
    # a new property that takes lookup precedence.
    def _get_message(self): return self.__message
    def _set_message(self, value): self.__message = value
    message = property(_get_message, _set_message)

class HwCertCommandErrorOutput(HwCertCommandException):
    def __init__(self, command, stderr=None):
        HwCertCommandException.__init__(self, command, "has output on stderr")
        if stderr:
            self._set_message(stderr)

class HwCertCommandError(HwCertCommandException):
    def __init__(self, command, message):
        HwCertCommandException.__init__(self, command, message)

class HwCertCommandErrorReturned(HwCertCommandError):
    def __init__(self, command, returnValue):
        HwCertCommandError.__init__(self, command, "returned %d" % returnValue)

class HwCertCommandErrorKilled(HwCertCommandError):
    def __init__(self, command, signal):
        HwCertCommandError.__init__(self, command, "signal %d" % signal)

class HwCertCommandStringNotFound(HwCertCommandError):
    def __init__(self, command, message):
        HwCertCommandError.__init__(self, command, message)

def unitTest():
    result = True
    try:
        # positive test: run
        command = Command("ls -a")
        print("ls -a:")
        command.run()

        # positive test: simple match
        year = "%u" % datetime.date.today().year
        command = Command("date")
        print("is it %s" % year)
        print(command.getString(year))

        # positive test: regex on single line
        command = Command("date")
        print("day of the week via date: %s" %  command.getString(regex="^(?P<day>[MTWF][a-z]).*$", regexGroup="day"))

        # positive test: regex on multiline
        command = Command("who")
        print("a device via who: %s" % command.getString(regex="^(?P<user>[a-z]+) (?P<device>[a-z/]+[0-9]*)[ \t]*(?P<date>2\d+-\d+-\d+).*$", regexGroup="device", singleLine=False))

        #positive test: integer - simple match
        command = Command("du .")
        print("simple du: %u" % command.getInteger(regex="\d+", singleLine=False))

        #positive test: integer
        command = Command("df .")
        print("blocks via df: %u" % command.getInteger(regex="^[^\t]+[ \t]+(?P<blocks>[0-9]+[ \t]+).*$", regexGroup="blocks", singleLine=False))

    except HwCertCommandException as e:
        print("Error: positive test failed:")
        print(command.command)
        print(e)
        result = False

    # negative test: fail simple match
    try:
        print("is it 1999?:")
        command = Command("date")
        command.getString(regex="1999")
        print("Error: invalid string match should raise exception")
        result = False
    except HwCertCommandException as e:
        print(e)

    # negative test: return value
    try:
        print("negative test: return value:")
        command = Command("exit 1")
        print("call exit(1)")
        command.echo()
        print("Error: non-zero return value should raise exception")
        result = False
    except HwCertCommandException as e:
        print(e)
        print("passed")

    # negative test: killed subprocess
    # disabling this test - to test it, use "killall sleep" while the unit test has paused.
    if False:
        try:
            print("negative test: killed subprocess:")
            sleep = Command("sleep 10")
            print("call sleep 10")
            sleep.echo()
            print("Error: killed process should raise exception")
            result = False
        except HwCertCommandException as e:
            print(e)
            sleep.printErrors()
            print("passed")

    # negative test: expect single line, get multiple
    try:
        print("negative test: more than one line of output")
        command = Command("ls -a")
        print("command: %s" % command.getString())
        print("Error: multi-line output when one line is expected should raise exception")
        result = False
    except HwCertCommandException as e:
        print(e)

    # negative test: output on stderr
    try:
        print("negative test: output on stderr")
        command = Command("echo \"boguserror\" >&2; echo \"boguserror\"")
        print("error echo: %s" % command.getString(regex="boguserror", singleLine=False))
        print("Error: output on stderr should raise exception")
        result = False
    except HwCertCommandException as e:
        print(e)

    return result

if __name__ == "__main__":
    if not unitTest():
        print("command.py unit test FAILED")
        exit(1)
    print("command.py unit test passed")
    exit(0)
