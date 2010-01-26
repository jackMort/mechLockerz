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
 
import os
import string
import random
import urllib
from mechanize import Browser, LinkNotFoundError
from BeautifulSoup import BeautifulSoup

class Lockerz:
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
    
    def answer_all( self, generator, recursive=False ):
        page = self.br.follow_link( text_regex="DAILIES" );
        self._answer_all( page, generator )
        # ..
        if recursive:
            i = 0
            while True:
                try:
                    i+=1
                    page = self.br.follow_link( text_regex="< Previous Posts" )
                    print "-- page %d" % i
                    self._answer_all( page, generator )
                except LinkNotFoundError:
                    break
        
    def answer( self, id, answer ):
        d = urllib.urlencode( { "id": id, "a": answer, "o": None } )
        r = self.br.open( "http://www.lockerz.com/daily/answer", d );
        print r.read()
        self.br.back()

    def getPTZ( self ):
        s = BeautifulSoup( self.br.open( "http://www.lockerz.com" ).read() )
        return s.find( "span", attrs={ "class": "ptz_value" } ).string
 
    def _answer_all( self, page, generator ):
        s = BeautifulSoup( page.read() )
        e = s.findAll( "div", attrs={ "class": "dailiesEntry" } )
        for i in e:
            try:
                self.answer( i["id"], generator.getRandomSentence() )
            except KeyError:
                print "Already answered ..."    


class WordGenerator:
    def __init__( self, min=2, max=30 ):
        self.min = min
        self.max = max
        stat = os.stat( '/usr/share/dict/words' )
        self.flen = stat[6]
        self.f = open( '/usr/share/dict/words' )

    def getSentance( self, size ):
        words = []
        while len( words ) < size:
            self.f.seek( int( random.random() * self.flen ) )
            words.append( string.split( self.f.read( 50 ) )[0] )
        return ' '.join( words )

    def getRandomSentence( self ):
        return self.getSentance( random.randint( self.min, self.max ) )

# vim: fdm=marker ts=4 sw=4 sts=4
