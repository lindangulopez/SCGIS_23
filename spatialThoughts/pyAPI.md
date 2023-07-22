[PyQGIS](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)  is the Python interface to QGIS. It is created using SIP and integrates with PyQt.

- QGIS C++ API documentation is available at https://qgis.org/api/3.28/
- QGIS Python API documentation is available at https://qgis.org/pyqgis/3.28/
- Both C++ and Python APIs are identical for most part, but certain functions are not available in the Python API.
- The QgisInterface class provides methods for interaction with the QGIS environment

### Change Title of QGIS Main Window: 

```
title = iface.mainWindow().windowTitle()
new_title = title.replace('QGIS', 'My QGIS')
iface.mainWindow().setWindowTitle(new_title)
```

### Change Icon of QGIS Main Window: 

```
import os

icon = 'qgis-black.png'
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
icon_path = os.path.join(data_dir, icon)
icon = QIcon(icon_path)
iface.mainWindow().setWindowIcon(icon)
```

### Remove Raster and Vector Menus: 

```
vector_menu = iface.vectorMenu()
raster_menu = iface.rasterMenu()
menubar = vector_menu.parentWidget()
menubar.removeAction(vector_menu.menuAction())
menubar.removeAction(raster_menu.menuAction())
```
