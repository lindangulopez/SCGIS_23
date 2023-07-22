# [Running Processing Algorithms](https://docs.qgis.org/testing/en/docs/user_manual/processing/console.html): 

- Do some geoprocessing
- Go to history
- Copy python code
- fit as a result in code

```
import os
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

filename = 'srtm.tif'
srtm = os.path.join(data_dir, filename)
iface.addRasterLayer(srtm, 'srtm', 'gdal')

results = processing.runAndLoadResults("native:hillshade", 
    {'INPUT': srtm, 
    'Z_FACTOR':2,
    'AZIMUTH':300,
    'V_ANGLE':40,
    'OUTPUT': 'TEMPORARY_OUTPUT'})
```
### Running Multiple Processing Algorithms: 

We can also chain multiple processing tools to build a script to build a data processing pipeline. In the example below, we will do 2 steps

- Clip srtm.tif raster using the shoreline.shp layer.
- Calculate the hillshade on the clipped raster and load it in QGIS.

Note that we are using the processing.run() method for the first step. This method calculates the output, but does not load the result to QGIS. This allows us to carry out multiple processing steps and not load intermediate layers.

```
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsRasterInterface

def add_toolbar_button(iface):
    # Function to add a button to the Plugins Toolbar with an icon
    action = QAction(QIcon('path_to_your_icon.png'), 'Show Raster Statistics', iface.mainWindow())
    action.triggered.connect(show_statistics)
    iface.addToolBarIcon(action)

def show_statistics():
    # Function to calculate and display the raster statistics

    # Get the current map canvas
    canvas = iface.mapCanvas()

    # Get the active raster layer
    layer = canvas.currentLayer()
    if not layer or not layer.type() == QgsMapLayer.RasterLayer:
        iface.messageBar().pushMessage("Error", "Please load and select a raster layer.", level=Qgis.Warning)
        return

    # Get the data provider for the raster layer
    provider = layer.dataProvider()

    # Get the raster interface from the data provider
    raster_interface = provider.rasterInterface()

    # Get the extent of the current map canvas
    extent = canvas.extent()

    # Calculate statistics for the current extent
    band_statistics = raster_interface.bandStatistics(1, QgsRasterInterface.All, extent, 0)

    # Display the statistics in the message bar
    if band_statistics.isValid():
        iface.messageBar().pushMessage(
            "Raster Statistics",
            f"Average value within current extent: {band_statistics.mean}",
            level=Qgis.Success,
            duration=5  # The message will automatically disappear after 5 seconds
        )
    else:
        iface.messageBar().pushMessage("Error", "Failed to compute raster statistics.", level=Qgis.Warning)

# Call the add_toolbar_button() function when the plugin is loaded
add_toolbar_button(iface)

```

