# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA



# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/CIM-generic"

class Element(object):
    # <<< element
    # @generated
    def __init__(self, uuid='', *args, **kw_args):
        """ Initialises a new 'Element' instance.

        @param uuid: 
        """
 
        self.uuid = uuid



        super(Element, self).__init__(*args, **kw_args)
    # >>> element



class CombinedVersion(Element):
    """ The combined version denotes the versions of the subpackages that have been combined into the total CIIMmodel. This is a convenience instead of having to look at each subpackage.
    """
    # <<< combined_version
    # @generated
    def __init__(self, date='', version='', *args, **kw_args):
        """ Initialises a new 'CombinedVersion' instance.

        @param date: Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        @param version: Form is IEC61970CIMXXvYY_IEC61968CIMXXvYY_combined where XX is the major CIM package version and the YY is the minor version, and different packages could have different major and minor versions.   For example IEC61970CIM13v18_IEC61968CIM10v16_combined.  Additional packages might be added in the future. 
        """
        # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        self.date = date

        # Form is IEC61970CIMXXvYY_IEC61968CIMXXvYY_combined where XX is the major CIM package version and the YY is the minor version, and different packages could have different major and minor versions.   For example IEC61970CIM13v18_IEC61968CIM10v16_combined.  Additional packages might be added in the future. 
        self.version = version



        super(CombinedVersion, self).__init__(*args, **kw_args)
    # >>> combined_version



# <<< cim15v01
# @generated
# >>> cim15v01
