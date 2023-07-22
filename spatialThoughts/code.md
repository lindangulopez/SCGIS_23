# [QGIS Interface API ](https://courses.spatialthoughts.com/pyqgis-in-a-day.html#qgis-interface-api-qgisinterface)

{
layer = iface.activeLayer()
layer.startEditing()
layer.deleteAttribute(1)
layer.commitChanges()
}

- layer = iface.activeLayer(): This line uses the iface object and runs the activeLayer() method which returns the currently selected layer in QGIS. We will learn more about iface in the QGIS Interface API section. The method returns the reference to the layer which is saved in the layer variable.
- layer.startEditing(): This is equivalent to putting the layer in the editing mode.
- layer.deleteAttribute(1): The deleteAttribute() is a method from QgsVectorLayer class. It takes the index of the attribute to be deleted. Here we pass on index 1 for the second attribute. (index 0 is the first attribute)
- layer.commitChanges(): This method saves the edit buffer and also disables the editing mode.

### Calculating distance using PyQGIS

{
from qgis.core import QgsDistanceArea

san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')


lat1, lon1 = san_francisco
lat2, lon2 = new_york
# Remember the order is X,Y
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

distance = d.measureLine([point1, point2])
print(distance/1000)

}
