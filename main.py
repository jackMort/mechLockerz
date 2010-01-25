#!/usr/bin/env python
# Copyright (C) 2010  lech.twarog@gmail.com
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lockerz import Lockerz
from lockerz import WordGenerator

lockerz = Lockerz( "<USER>", "<PASSWORD>" )
if lockerz.connect():
	ptz = lockerz.getPTZ()
	generator = WordGenerator()
	lockerz.answer_all( generator, recursive=True )
	print ":: PTZ before: %s, after %s" % ( ptz, lockerz.getPTZ() )
else:
	print "Cannot connect, check user and password ..."

# vim: fdm=marker ts=4 sw=4 sts=4
