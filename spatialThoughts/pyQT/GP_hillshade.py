import os
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

filename = 'srtm.tif'
srtm = os.path.join(data_dir, filename)
filename = 'shoreline.shp'
shoreline = os.path.join(data_dir, filename) 

results = processing.run("gdal:cliprasterbymasklayer", 
    {'INPUT':srtm,
    'MASK': shoreline,
    'OUTPUT':'TEMPORARY_OUTPUT'})

clipped_dem = results['OUTPUT']
   
results = processing.runAndLoadResults("native:hillshade", 
    {'INPUT': clipped_dem, 
    'Z_FACTOR':2,
    'AZIMUTH':300,
    'V_ANGLE':40,
    'OUTPUT': 'TEMPORARY_OUTPUT'})
print(result)    