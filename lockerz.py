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
 
import urllib
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

class Lockerz():
    def __init__( self, name, password ):
        self.name = name
        self.password = password
        self.br = Browser()

    def connect( self ):
        self.br.open( "http://www.lockerz.com" )
        self.br.select_form( nr=0 )
        self.br["handle"] = self.name
        self.br["password"] = self.password

        self.br.submit()
        return "Lockerz : My Locker" in self.br.title()
        
    def answer_daily( self, answer ):
        r = self.br.follow_link( text_regex="DAILIES" )
        s = BeautifulSoup( r.read() )
        e = s.findAll( "div", attrs={ "class": "dailiesEntry" } ) 
        for i in e:
            try:
                self.answer( i["id"], answer )
            except KeyError:
                print "Already answered"    

    def answer( self, id, answer ):
        d = urllib.urlencode( { "id": id, "a": answer, "o": None } )
        r = self.br.open( "http://www.lockerz.com/daily/answer", d );
        print r.read()

# vim: fdm=marker ts=4 sw=4 sts=4
