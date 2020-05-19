import requests
import codecs, json
import numpy as np

def getToken():
	envFile = open('../../.env', 'r')
	for row in envFile:
		data = row.split('=')
		if data[0] == 'ncdc_token':
			return data[1]

def getJSONData():
	# call GET request API
	# Data source: https://www.ncdc.noaa.gov/cdo-web/webservices/v2#stations
	# NOAA api url: https://www.ncdc.noaa.gov/cdo-web/api/v2/stations
	token = getToken()
	API_ENDPOINT = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations'
	r = requests.get(url = API_ENDPOINT, headers = { 'token': token }, params = { 'limit': 5 })
	return r.json()

class NumpyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, np.ndarray):
			return obj.tolist()
		return json.JSONEncoder.default(self, obj)


arrayData = []
jsonData = getJSONData()

# read json format
for station in jsonData['results']:
	arrayData.append(station['name'])
print(arrayData)

# write json into a file
JSON_FILE = 'data.json'
json.dump(
	{ 'value': arrayData },
	codecs.open(JSON_FILE, 'w', encoding='utf-8'),
	separators=(',', ':'),
	sort_keys=True,
	indent=4,
	cls=NumpyEncoder
)
