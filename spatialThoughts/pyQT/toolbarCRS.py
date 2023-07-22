import os
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

crsToolbar = iface.addToolBar('CRS Toolbar')

label = QLabel('Enter an EPSG Code', parent=projectToolbar)
crsTextBox = QLineEdit('4326', parent=projectToolbar)
crsTextBox.setFixedWidth(80)
button = QPushButton('Go!', parent=projectToolbar)

crsToolbar.addWidget(label)
crsToolbar.addWidget(crsTextBox)
crsToolbar.addWidget(button)

def changeCrs(crsText):
    epsgCode = int(crsTextBox.text())
    iface.messageBar().pushInfo('Function called', f'You entered {epsgCode}')
    # Add code to change the project CRS to the EPSG code
    QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(epsgCode))
    
button.clicked.connect(changeCrs)