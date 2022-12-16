#
# Current web scrapers
# Based on chapters 1 - 3 in the repositiries text (Web Scraping with Python, 2nd Edition).
#

#
# Imports
#
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import random
import datetime


#
# Initializations / Globals
#
random.seed( datetime.datetime.now() )



#
# Functions
#
def findTitle( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )

    else:
        try:
            bs = BeautifulSoup( html.read(), 'html5lib' )
            title = bs.head.title
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if title == None:
            print( 'Title could not be found' )
        else:
            print( ' ' )
            print( 'Webpage Title: ')
            print( title )



def findTagClass( url, findTag, findClass ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            bs = BeautifulSoup( html.read(), 'html5lib' )
            class_to_find = bs.find_all( findTag, { 'class' : findClass } )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if class_to_find == None:
            print( 'Tag and Class could not be found' )
        else:
            print( ' ' )
            print( 'All instances of the', findTag, 'tag, &', findClass, 'class.' )
            for tagClass in class_to_find:
                print( tagClass.get_text() )



def findIdClass( url, findId, findClass ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            bs = BeautifulSoup( html.read(), 'html5lib' )
            idClass_to_find = bs.find_all( id = findId, class_ = findClass )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if idClass_to_find == None:
            print( 'Id and Class could not be found' )
        else:
            print( ' ' )
            print( 'All instances of the', findId, 'Id, &', findClass, 'class.' )
            for idClass in idClass_to_find:
                print( idClass.get_text() )



def findHeaderAll( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            bs = BeautifulSoup( html.read(), 'html5lib' )
            find_all_headers = bs.find_all( [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6' ] )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if find_all_headers == None:
            print( 'No Headers could not be found' )
        else:
            print( ' ' )
            print( 'All Headers: ' )
            for headers in find_all_headers:
                print( headers.get_text() )



def findInstancesOfText( url, findText ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found.' )
    else:
        try:
            bs = BeautifulSoup( html.read(), 'html5lib' )
            text_to_find = bs.find_all( text = findText )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if text_to_find == None:
            print( 'Tag and Class could not be found.' )
        else:
            print( ' ' )
            print( 'The text:', findText, ', occurs', len( text_to_find ), "times."  )



def findImages( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found.' )
    else:
        try:
            bs = BeautifulSoup( html, 'html5lib' )
            images_to_find = bs.find_all( 'img' )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        if images_to_find == None:
            print( 'No images could not be found.' )
        else:
            print( ' ' )
            print( 'Images found on this webpage are: ' )
            for image in images_to_find:
                print( image[ 'src' ] )



def findDoubleAttributes( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( "\n", 'HTTP Error: ', e )
    except URLError as e:
        print( "\n", 'URL Error: ', e )
        print( 'The server could not be found.' )
    else:
        try:
            bs = BeautifulSoup( html, 'html5lib' )
            doubleAttrs_to_find = bs.find_all( lambda tag: len( tag.attrs ) == 2 )
        except AttributeError as e:
            print( "\n", 'Attribute Error: ', e )
        if doubleAttrs_to_find == None:
            print( "\n", 'No double attributes could not be found.' )
        else:
            print( "\n", 'There are', len( doubleAttrs_to_find ), 'tags with double attributes.' )
            print( "\n", 'The Double Attributes found on this webpage are: ' )
            for doubleAttrs in doubleAttrs_to_find:
                print( doubleAttrs.get_text() )



def findHyperlinks( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            bs = BeautifulSoup( html, 'html5lib' )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        for link in bs.find_all( 'a' ):
            if 'href' in link.attrs:
                print( link.attrs[ 'href' ] )



def findWikipediaArticles( url ):
    try:
        html = urlopen( url )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            bs = BeautifulSoup( html, 'html5lib' )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        for link in bs.find( 'div', {'id' : 'bodyContent' } ).find_all( 'a', href=re.compile( '^(/wiki/)((?!:).)*$' ) ):
            if 'href' in link.attrs:
                print( link.attrs[ 'href' ] )











#
# Test Code
#

#findTagClass( 'http://www.pythonscraping.com/pages/warandpeace.html', 'span', 'green' )
#findIdClass( 'http://www.pythonscraping.com/pages/warandpeace.html', 'text', 'red' )
#findInstancesOfText( 'http://www.pythonscraping.com/pages/warandpeace.html', 'the prince' )
#findTitle( 'http://www.pythonscraping.com/pages/page1.html' )
#findHeaderAll( 'http://www.pythonscraping.com/pages/warandpeace.html' )
#findImages( 'http://www.pythonscraping.com/pages/page3.html' )
#findDoubleAttributes( 'http://www.pythonscraping.com/pages/page3.html' )
#findHyperlinks( 'http://en.wikipedia.org/wiki/Kevin_Bacon' )
#findWikipediaArticles( 'http://en.wikipedia.org/wiki/Kevin_Bacon' )
