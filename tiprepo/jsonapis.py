import json
import urllib2

def github(query):
    url = 'https://api.github.com' + query
    return json_get(url)

def json_get(url):
    return json.loads(urllib2.urlopen(url).read())
