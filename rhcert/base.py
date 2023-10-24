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


from xml.etree import ElementTree

from tags import Constants

class ETreeWrapper(object):
    """ ETreeWrapper is an element tree wrapper base class for rhcert """
    def __init__(self, root):
        self.root = root
        self.new()

    def new(self):
        self.element = ElementTree.Element(self.root)

    def load(self, xmlString):
        self.element = ElementTree.fromstring(xmlString)

    def toXML(self):
        return ElementTree.tostring(self.element).decode() + u'\n'

    def set(self, element, attribute, value):
        stringValue = self.__makeString(value)
        if not stringValue:
            return False
        return element.set(attribute, stringValue)

    def setText(self, element, text):
        textString = self.__makeText(text)
        if not textString:
            return False
        element.text = textString
        return True

    def subElement(self, element, tag):
        return ElementTree.SubElement(element, tag)

    def __makeText(self, data):
        if not data:
            return ""

        if type(data) is list:
            try:
                data = "\n".join(data)
            except Exception:
                pass
        return self.__makeString(data)

    def __makeString(self, value):
        try: #python2
            if type(value) == unicode:
                return value
        except:
            pass # python3, or python2 not unicode type

        if type(value) is bytes:
            return value.decode(Constants.utf_8)
        if type(value) != str: # int, float, etc.
            return str(value)
        return value

def unit_test():
    return True



if __name__ == "__main__":
    import sys
    if unit_test():
        sys.exit(0)
    sys.exit(1)



