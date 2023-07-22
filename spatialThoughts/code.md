# [QGIS Interface API ](https://courses.spatialthoughts.com/pyqgis-in-a-day.html#qgis-interface-api-qgisinterface)

```
layer = iface.activeLayer()
layer.startEditing()
layer.deleteAttribute(1)
layer.commitChanges()
```

- layer = iface.activeLayer(): This line uses the iface object and runs the activeLayer() method which returns the currently selected layer in QGIS. We will learn more about iface in the QGIS Interface API section. The method returns the reference to the layer which is saved in the layer variable.
- layer.startEditing(): This is equivalent to putting the layer in the editing mode.
- layer.deleteAttribute(1): The deleteAttribute() is a method from QgsVectorLayer class. It takes the index of the attribute to be deleted. Here we pass on index 1 for the second attribute. (index 0 is the first attribute)
- layer.commitChanges(): This method saves the edit buffer and also disables the editing mode.

### Calculating distance using PyQGIS: 

```
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

```
### [Distance Conversion](https://qgis.org/pyqgis/3.28/core/QgsUnitTypes.html#qgis.core.QgsUnitTypes.DistanceUnit): 

```
from qgis.core import QgsDistanceArea
from qgis.core import QgsUnitTypes

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
print('Distance in meters', distance)

distance_km = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceKilometers)
print('Distance in kilometers', distance_km)

distance_mi = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceMiles)
print('Distance in miles', distance_mi)
```

### [Building a Dialog Box](https://wiki.python.org/moin/PyQt): 

```
mb = QMessageBox()
mb.setText('Click OK to confirm')
mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
return_value = mb.exec()
if return_value == QMessageBox.Ok:
    print('You pressed OK')
elif return_value == QMessageBox.Cancel:
    print('You pressed Cancel')
```
