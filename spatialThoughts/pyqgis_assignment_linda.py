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
