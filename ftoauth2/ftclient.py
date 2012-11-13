#!/usr/bin/python

import urllib2, urllib, json, httplib

client_id = ""
client_secret = ""
access_token = ""
refresh_token = ""

tableId = ''

def simpleQuery():    
    access_token = refreshToken()
    query = 'SELECT * FROM %s' % tableId
    request = urllib2.Request(
      url='https://www.googleapis.com/fusiontables/v1/query?%s' % \
        (urllib.urlencode({'access_token': access_token,
                           'sql': query})))
    
    request_open = urllib2.urlopen(request)
    response = request_open.read()
    request_open.close()
    print dir(response)
    print response


def refreshToken():
    data = urllib.urlencode({
      'client_id': client_id,
      'client_secret': client_secret,
      'refresh_token': refresh_token,
      'grant_type': 'refresh_token'})
    request = urllib2.Request(
      url='https://accounts.google.com/o/oauth2/token',
      data=data)
    request_open = urllib2.urlopen(request)
    response = request_open.read()
    request_open.close()
    tokens = json.loads(response)
    access_token = tokens['access_token']
    return access_token
    
    
def insertRecord(formItems, formData):
    access_token = refreshToken()
    query = "INSERT INTO %s " % tableId
    query += "('%s', '%s', '%s', '%s', '%s') " % tuple(formItems)
    query += "VALUES ('%s', '%s', '%s', '%s', '%s')" % tuple(formData)
    request = urllib2.Request(
      url='https://www.googleapis.com/fusiontables/v1/query?%s' % \
        (urllib.urlencode({'access_token': access_token,
                           'sql': query})), data="")
    request_open = urllib2.urlopen(request)
    response = request_open.read()
    request_open.close()
    

if __name__ == "__main__":
    formItems = ['LatLng', 'Date Recorded', 'Address', 'Type', 'Notes']
    items = ["test123", "test123", "test123", "test123", "test123"]
    insertRecord(formItems, items)
    
