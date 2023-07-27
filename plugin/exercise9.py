import os
import pandas as pd

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

# Check if a layer is selected
layer = iface.activeLayer()
if not layer:
    iface.messageBar().pushMessage('Please select a layer', level=Qgis.Critical)
    exit()

# Check if the selected layer is a vector layer
if layer.type() != QgsMapLayer.VectorLayer:
    iface.messageBar().pushMessage('Please select a vector layer', level=Qgis.Critical)
    exit()

# Check if any features are selected
if layer.selectedFeatureCount() == 0:
    iface.messageBar().pushMessage('No features selected', level=Qgis.Critical)
    exit()

# Get a list of field names
fieldnames = [field.name() for field in layer.fields()]

# Get a list of attributes for each selected feature
data = [f.attributes() for f in layer.selectedFeatures()]

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=fieldnames)

# Save to file
output_name = 'output.csv'
output_path = os.path.join(data_dir, output_name)
df.to_csv(output_path, index=False)

iface.messageBar().pushMessage('Success:', 'Output file written at ' + output_path, level=Qgis.Success)
