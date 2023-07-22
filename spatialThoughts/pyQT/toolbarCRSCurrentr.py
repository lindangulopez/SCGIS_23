import os
from qgis.core import QgsCoordinateReferenceSystem
from qgis.PyQt.QtWidgets import QLabel, QLineEdit, QPushButton
from qgis.utils import iface

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

crsToolbar = iface.addToolBar('CRS Toolbar')

label = QLabel('Enter an EPSG Code or authid', parent=crsToolbar)
crsTextBox = QLineEdit('EPSG:4326', parent=crsToolbar)
crsTextBox.setFixedWidth(120)
button = QPushButton('Go!', parent=crsToolbar)

crsToolbar.addWidget(label)
crsToolbar.addWidget(crsTextBox)
crsToolbar.addWidget(button)

def showErrorMessage(message):
    iface.messageBar().pushCritical('Error', message)

def changeCrs():
    crsText = crsTextBox.text()
    if ':' in crsText:
        authid = crsText
    else:
        try:
            epsgCode = int(crsText)
            authid = f'EPSG:{epsgCode}'
        except ValueError:
            showErrorMessage('Invalid input. Please enter a valid EPSG code (integer) or authid (e.g., EPSG:4326).')
            return

    iface.messageBar().pushInfo('Function called', f'You entered {authid}')
    # Add code to change the project CRS to the authid
    QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(authid))

button.clicked.connect(changeCrs)
