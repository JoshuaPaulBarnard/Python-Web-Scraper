#
# Six Degrees of Wikipedia solution finder
#  The goal is to link two unlikely subjects (in the first case, Wikipedia articles
#   that link to each other, and in the second case, actors appearing in the same
#   film) by a chain containing no more than six total (including the two original subjects).
# Based on page 33-36 of the repositories text.
#


from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import random
import datetime



random.seed( datetime.datetime.now() )



def getWikipediaLinks( articleURL ):
    try:
        html = urlopen( 'http://en.wikipedia.org{}'.format( articleURL ) )
    except HTTPError as e:
        print( 'HTTP Error: ', e )
    except URLError as e:
        print( 'URL Error: ', e )
        print( 'The server could not be found' )
    else:
        try:
            soup = BeautifulSoup( html, 'html5lib' )
        except AttributeError as e:
            print( 'Attribute Error: ', e )
        return soup.find( 'div', { 'id' : 'bodyContent' } ).find_all( 'a', href=re.compile( '^(/wiki/)((?!:).)*$' ) )



links = getWikipediaLinks( '/wiki/Kevin_Bacon' )
while len( links ) > 0:
    newArticle = links[ random.randint( 0, len( links) - 1 ) ].attrs[ 'href' ]
    print( newArticle )
    links = getWikipediaLinks( newArticle )
