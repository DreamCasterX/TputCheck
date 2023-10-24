#!/usr/bin/python3
# Copyright (c) 2017 Red Hat, Inc. All rights reserved. This copyrighted material
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

from base import ETreeWrapper

from tags import Tags, Attributes

class CommandXML(ETreeWrapper):
    """ CommandXML captures rhcert.command.Command object state as XML """
    def __init__(self, command=None):
        ETreeWrapper.__init__(self, Tags.command)
        if command:
            self.loadCommand(command)

    def loadCommand(self, command):
        self.command = command
        """ extract data from a rhcert.Command object """
        self.set(self.element, Attributes.command, self.command.command)
        if self.command.regex:
            regexElement = self.subElement(self.element, Tags.regex)
            self.setText(regexElement, self.command.regex)
            self.set(regexElement, Attributes.group, self.command.regexGroup)
            self.set(regexElement, Attributes.single_line, self.command.singleLine)

        if self.command.output:
            stdoutElement = self.subElement(self.element, Tags.stdout)
            self.setText(stdoutElement, self.command.output)
        if self.command.errors:
            stderrElement = self.subElement(self.element, Tags.stderr)
            self.setText(stderrElement, self.command.errors)

        self.set(self.element, Attributes.return_value, self.command.returnValue)
        self.set(self.element, Attributes.signal, self.command.signal)

        # is it a remote command via remote.RemoteCommand subclass?
        try:
            self.set(self.element, Attributes.ip_address, self.command.remoteConnection.remote_ip)
        except:
            pass # wasn't a RemoteCommand
        try:
            self.set(self.element, Attributes.hostname, self.command.host)
        except:
            pass # wasn't a RemoteSingleCommand

def unit_test():
    from rhcert.command import Command
    command = Command("rpm -V redhat-certification")
    command.run()
    return True



if __name__ == "__main__":
    import sys
    if unit_test():
        sys.exit(0)
    sys.exit(1)



