import os
from datetime import datetime

icon = 'question.svg'
data_dir = os.path.join('D:\Cursos\Curso PyQGIS SpatialThoughts\pyqgis_masterclass')
icon_path = os.path.join(data_dir, icon)

def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    iface.messageBar().pushMessage('Current Time',current_time, Qgis.MessageLevel.Info,7)

action = QAction('Show Time')
action.triggered.connect(show_time)
action.setIcon(QIcon(icon_path))
iface.addToolBarIcon(action)