import os
from qgis.core import QgsProject

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

vector_layer = 'seismic_zones.shp'
vector_layer_path = os.path.join(data_dir, vector_layer)

raster_layer = 'srtm.tif'
raster_layer_path = os.path.join(data_dir, raster_layer)

# Input vector has invalid geometries
# Fix them first
results = processing.run("native:fixgeometries", {
    'INPUT': vector_layer_path,
    'METHOD': 0,
    'OUTPUT': 'TEMPORARY_OUTPUT'
})

fixed_vector_layer = results['OUTPUT']

# Run Zonal Statstics and load the resulting layer
zonal_stats_result = processing.run("native:zonalstatisticsfb", {
    'INPUT_RASTER': raster_layer_path,
    'RASTER_BAND': 1,  # If your raster has multiple bands, adjust this accordingly
    'INPUT_VECTOR': fixed_vector_layer,
    'COLUMN_PREFIX': 'Avg_Elevation_',  # This prefix will be used for the new attribute containing the average elevation
    'STATISTICS': [2],  # Use 2 for Mean (average) elevation
    'OUTPUT': 'TEMPORARY_OUTPUT'
})

zonal_stats_layer = QgsProject.instance().addMapLayer(zonal_stats_result['OUTPUT'])

# Now you can work with the 'zonal_stats_layer' which contains the average elevation within each seismic zone.
