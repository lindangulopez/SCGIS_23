layer = iface.activeLayer()

if layer.name() == 'zonig':
    iface.messageBar().pushMessage('Sucess','You selected the right layer', Qgis.MessageLevel.Success,10)
else:
    iface.messageBar().pushMessage('Error','Wrong Layer Selected', Qgis.MessageLevel.Critical,10)