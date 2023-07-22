import os
from qgis.core import QgsCoordinateReferenceSystem
from qgis.PyQt.QtWidgets import QLabel, QLineEdit, QPushButton
from qgis.utils import iface

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

crsToolbar = iface.addToolBar('CRS Toolbar')

label = QLabel('Enter an EPSG Code', parent=crsToolbar)
crsTextBox = QLineEdit('4326', parent=crsToolbar)
crsTextBox.setFixedWidth(80)
button = QPushButton('Go!', parent=crsToolbar)

crsToolbar.addWidget(label)
crsToolbar.addWidget(crsTextBox)
crsToolbar.addWidget(button)

def showErrorMessage(message):
    iface.messageBar().pushCritical('Error', message)

def changeCrs():
    epsgText = crsTextBox.text()
    try:
        epsgCode = int(epsgText)
        iface.messageBar().pushInfo('Function called', f'You entered {epsgCode}')
        # Add code to change the project CRS to the EPSG code
        QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(epsgCode))
    except ValueError:
        showErrorMessage('Invalid EPSG code. Please enter a valid integer.')

button.clicked.connect(changeCrs)
