import datetime
import json
import time
import urllib2

def github(query):
    url = 'https://api.github.com' + query
    return json_get(url)

def github_unixtime(timestamp):
    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return int(time.mktime(dt.timetuple()))

def json_get(url):
    return json.loads(urllib2.urlopen(url).read())
