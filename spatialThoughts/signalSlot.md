### Change Visibility of a Toolbar: 

```
iface.pluginToolBar().setVisible(True)
```

### Add a button to a toolbar; 
```
import os
from datetime import datetime

icon = 'question.svg'
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
icon_path = os.path.join(data_dir, icon)

def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    iface.messageBar().pushInfo('Current Time', current_time)

action = QAction('Show Time')
action.triggered.connect(show_time)
action.setIcon(QIcon(icon_path))
iface.addToolBarIcon(action)
```

### Add New Layers: 

```
import os
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

filename = 'seismic_zones.shp'
uri = os.path.join(data_dir, filename)
iface.addVectorLayer(uri, 'seismic_zones', 'ogr')

filename = 'sf.gpkg|layername=zoning'
uri = os.path.join(data_dir, filename)
iface.addVectorLayer(uri, 'zoning', 'ogr')
```

### Create a New Vector Layer: 

```
mc = iface.mapCanvas()
extent = mc.extent()

vlayer = QgsVectorLayer('Polygon', 'extent', 'memory')
crs = QgsProject.instance().crs()
vlayer.setCrs(crs)

provider = vlayer.dataProvider()

f = QgsFeature()
geometry = QgsGeometry.fromRect(extent)
f.setGeometry(geometry)

provider.addFeature(f)
vlayer.updateExtents() 

QgsProject.instance().addMapLayer(vlayer)
```
