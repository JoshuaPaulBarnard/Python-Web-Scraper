#
# External Web Crawler
# Based on chapters 1 - 3 in the repositiries text (Web Scraping with Python, 2nd Edition).
#



# Load Libraries
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime
import random



# Initialize Global variables and seeds
pages = set()
allExternalLinks = set()
allInternalLinks = set()
random.seed( datetime.datetime.now() )



# Functions

# Retrieves a list of all the Internal links found on a page
def getInternalLinks( soup, internalURL ):
    internalURL_formatted = '{}://{}'.format( urlparse( internalURL ).scheme, urlparse( internalURL ).netloc )
    internalLinks = []
    print( '\nNow crawling through the site:', internalURL, '\n' )

    # Now we find all of the links that begin with a "/"
    for link in soup.find_all( 'a', href=re.compile( '^(/|.*'+internalURL_formatted+' )' ) ):
        if link.attrs[ 'href' ] is not None:
            if link.attrs[ 'href' ] not in internalLinks:
                if( link.attrs[ 'href' ].startswith( '/' ) ):
                    internalLinks.append( internalURL_formatted + link.attrs[ 'href' ] )
                else:
                    internalLinks.append( link.attrs[ 'href' ] )

    return internalLinks

'''
    # Finds all links that end with "htm" or "html" or "php"
    for link in soup.find_all( 'a', href = re.compile( '(htm|html|php)*$' ) ):
        if link.attrs[ 'href' ] is not None:
            if link.attrs[ 'href' ] not in internalLinks:
                internalLinks.append( link.attrs[ 'href' ] )



    # Finds all links that start with "http" and contain the current URL
    for link in soup.find_all( 'a', href = re.compile( '^(http|www)(('+internalURL_formatted+').)*$' ) ):
        if link.attrs[ 'href' ] is not None:
            if link.attrs[ 'href' ] not in internalLinks:
                internalLinks.append( link.attrs[ 'href' ] )
'''





# Retrieves a list of all the external links found on a page
def getExternalLinks( soup, externalURL ):
    externalLinks = []

    # Finds all links that start with "http" that do not contain the current URL
    for link in soup.find_all( 'a', href = re.compile( '^(http|www)((?!'+externalURL+').)*$' ) ):
        if link.attrs[ 'href' ] is not None:
            if link.attrs[ 'href' ] not in externalLinks:
                externalLinks.append( link.attrs[ 'href' ] )
    return externalLinks


def getRandomExternalLink( startingPage ):
    html = urlopen( startingPage )
    soup = BeautifulSoup( html, 'html5lib' )
    externalLinks = getExternalLinks( soup, urlparse( startingPage ).netloc )
    if len( externalLinks ) == 0:
        print( 'No external links, looking around the site for one' )
        domain = '{}://{}'.format( urlparse( startingPage ).scheme, urlparse( startingPage ).netloc )
        internalLinks = getInternalLinks( soup, domain )
        return getRandomExternalLink( internalLinks[ random.randint( 0, len( internalLinks ) - 1 ) ] )
    else:
        return externalLinks[ random.randint( 0, len( externalLinks ) - 1 ) ]


def followExternalOnly( startingSite ):
    externalLink = getRandomExternalLink( startingSite )
    print( 'Random external link is: {}'.format( externalLink ) )
    followExternalOnly( externalLink )


# collects a list of all external URLs found on the site
def getAllExternalLinks( siteURL ):
    html = urlopen( siteURL )
    domain = '{}://{}'.format( urlparse( siteURL ).scheme, urlparse( siteURL ).netloc )
    soup = BeautifulSoup( html, 'html5lib' )
    internalLinks = getInternalLinks( soup, domain )
    externalLinks = getExternalLinks( soup, domain )
    allInternalLinks.add( siteURL )

    for link in externalLinks:
        if link not in allExternalLinks:
            allExternalLinks.add( link )
            print( link )
    for link in internalLinks:
        if link not in allInternalLinks:
            allInternalLinks.add( link )
            getAllExternalLinks( link )


# collects a list of all Internal URLs and crawls to other sites
def getAllInternalLinks( siteURL ):
    html = urlopen( siteURL )
    domain = '{}://{}'.format( urlparse( siteURL ).scheme, urlparse( siteURL ).netloc )
    soup = BeautifulSoup( html, 'html5lib' )
    allInternalLinks.add( siteURL )
    internalLinks = getInternalLinks( soup, domain )
    externalLinks = getExternalLinks( soup, domain )

    for link in internalLinks:
        if link not in allInternalLinks:
            allInternalLinks.add( link )
            print( link )
    for link in externalLinks:
        if link not in allExternalLinks:
            allExternalLinks.add( link )
            getAllInternalLinks( link )


# collects a list of all the internal URLs found on the site.
def getOnlyInternalLinks( siteURL ):
    html = urlopen( siteURL )
    domain = '{}://{}'.format( urlparse( siteURL ).scheme, urlparse( siteURL ).netloc )
    soup = BeautifulSoup( html, 'html5lib' )
    allInternalLinks.add( siteURL )

    internalLinks = getInternalLinks( soup, domain )
    for link_internal in internalLinks:
        if link_internal not in allInternalLinks:
            allInternalLinks.add( link_internal )
            print( link_internal )

'''
    externalLinks = getExternalLinks( soup, domain )
    for link_external in externalLinks:
        if link_external not in allExternalLinks:
            allExternalLinks.add( link_external )
            getAllInternalLinks( link_external )
'''



#
# Code to execute program
#

#followExternalOnly( 'http://oreilly.com' )
#getAllExternalLinks( 'http://oreilly.com' )
#getAllInternalLinks( 'http://oreilly.com' )
#getOnlyInternalLinks( 'http://oreilly.com' )
