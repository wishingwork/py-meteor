import csv

def getCSVFormat(csvfile):
	sniffer = csv.Sniffer()
	csv_dialect = sniffer.sniff(csvfile.readline(), ',')
	return 	csv_dialect

# read CSV
# csv data from GSOD - https://www7.ncdc.noaa.gov/CDO/cdoselect.cmd?datasetabbv=GSOD
with open('../../data/GSOD_data.txt') as csvfile:

	csv_dialect = getCSVFormat(csvfile)
    
	readCSV = csv.reader(csvfile, csv_dialect)
	header = next(readCSV)

	stn = ''
	data = []
	for row in readCSV:
		data.append(float(row[3]))
		if stn != '' and stn != row[0]:
			break
		stn = row[0]

# write CSV
with open('./ouput.csv', 'w') as ouput:
	writer = csv.writer(ouput)
	writer.writerows(map(lambda x: [x], data))
