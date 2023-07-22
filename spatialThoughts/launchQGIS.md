## Running Python Code at QGIS Launch: 

It is possible to execute some PyQGIS code every time QGIS starts. QGIS looks for a file named startup.py in the user’s Python home directory, and if it is found, executes it. This file is very useful in customizing QGIS interface with techniques learnt in the previous section.

If you are running multiple versions of QGIS, a very useful customization is to display the QGIS version number and name in the main window. The version name is stored in a global QGIS variable called qgis_version. We can read that variable and set the main window’s title with it. We connect this code to the signal iface.initializationCompleted signal when the main window is loaded.

Create a new file named startup.py with the following code. Note the imports at the top - including iface. When we ran the code snippets in the Python Console, we did not have to import any modules since they are done automatically when the console starts. For pyqgis scripts elsewhere, we have to explicitly import the modules (classes) that we want to use.

```
from qgis.utils import iface
from qgis.core import QgsExpressionContextUtils

def customize():
    version = QgsExpressionContextUtils.globalScope().variable('qgis_version')
    title = iface.mainWindow().windowTitle()
    iface.mainWindow().setWindowTitle('{} | {}'.format(title,version))


iface.initializationCompleted.connect(customize)
```

see path: https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/intro.html#running-python-code-when-qgis-starts
