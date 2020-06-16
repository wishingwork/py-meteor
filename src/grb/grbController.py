#pygrib 
#doc - http://jswhit.github.io/pygrib/docs/index.html
#Github - https://github.com/jswhit/pygrib

import pygrib
grib = '../../data/gfs_3_20200601_0000_000.grb2'

#open/read grib file
grbs = pygrib.open(grib)
outputFile = open('gfsvar.txt', 'w')
ii=0
for g in grbs:
	print(g)
	outputFile.write(
		str(ii) + '##' +
		g.typeOfLevel + '##' + str(g.level) + '##' + 
		g.name + '##' + str(g.validDate) + '##' +
		str(g.analDate) + '##' + str(g.forecastTime) + "\n")
	ii = ii + 1
outputFile.close()

#check domain of grib file
grb = grbs[1]
lats, lons = grb.latlons()
print(lats.shape, lats.min(), lats.max(), lons.shape, lons.min(), lons.max())

#get data from grib file
uu = grbs[320]['values']
print(uu)