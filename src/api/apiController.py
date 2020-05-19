import requests
import json
def getToken():
	envFile = open('../../.env', 'r')
	for row in envFile:
		data = row.split('=')
		if data[0] == 'ncdc_token':
			return data[1]

# call GET request API
# Data source: https://www.ncdc.noaa.gov/cdo-web/webservices/v2#stations
# NOAA api url: https://www.ncdc.noaa.gov/cdo-web/api/v2/stations
token = getToken()
API_ENDPOINT = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations'
r = requests.get(url = API_ENDPOINT, headers = { 'token': token }, params = { 'limit': 5 })
pastebin_url = r.text
print('request url: ' + pastebin_url)

jsonOutput = r.json()
print(jsonOutput)

# call POST request API
# Reference: https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request
API_ENDPOINT = 'https://httpbin.org/post'
r = requests.post(API_ENDPOINT, data = {'key':'value'})
jsonOutput = r.json()
print(jsonOutput)