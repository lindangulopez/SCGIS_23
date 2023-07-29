### open on localhost: 

http://localhost/github/SCGIS_23/openlayers/WMS_test.html

### replace wms url with geoserver url: 

http://localhost:8080/geoserver/tiger/wms

### switch layer to 

tiger:tiger_roads

### copy lat-lon

http://localhost:8080/geoserver/tiger/wms?service=WMS&version=1.1.0&request=GetMap&layers=tiger%3Atiger_roads

**&bbox=-74.02722%2C40.684221%2C-73.907005%2C40.878178**

&width=476&height=768&srs=EPSG%3A4326&styles=&format=application/openlayers

### get and set projection on file

on console : 

```
map.getView().getProjection()
```
[xb {wb: 'EPSG:3857', a: 'm', i: Array(4), oe: Array(4), b: 'enu', …}]

```
var map = new ol.Map({
        layers: layers,
        target: 'map',
        view: new ol.View({
          center: [-73.907005, 40.878178],
          projection:'EPSG:4326',
          zoom: 4
        })
      });
```


