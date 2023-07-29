# WMS

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
### delete old extent 

```
extent: [-13884991, 2870341, -7455066, 6338219],
```
# WFS

### go to : https://openlayers.org/en/v4.6.5/examples/vector-wfs.html

- copy vector layer code and paste in map file.
  
```
var vectorSource = new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: function(extent) {
          return 'https://ahocevar.com/geoserver/wfs?service=WFS&' +
              'version=1.1.0&request=GetFeature&typename=osm:water_areas&' +
              'outputFormat=application/json&srsname=EPSG:3857&' +
              'bbox=' + extent.join(',') + ',EPSG:3857';
        },
        strategy: ol.loadingstrategy.bbox
      });


      var vector = new ol.layer.Vector({
        source: vectorSource,
        style: new ol.style.Style({
          stroke: new ol.style.Stroke({
            color: 'rgba(0, 0, 255, 1.0)',
            width: 2
          })
        })
      });
```

### reset credentials 
- own server
- own layer
- own crs

FROM

```
 var vectorSource = new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: function(extent) {
          return 'https://ahocevar.com/geoserver/wfs?service=WFS&' +
              'version=1.1.0&request=GetFeature&typename=osm:water_areas&' +
              'outputFormat=application/json&srsname=EPSG:3857&' +
              'bbox=' + extent.join(',') + ',EPSG:3857';
        },
        strategy: ol.loadingstrategy.bbox
      });

```

TO
```
var vectorSource = new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: function(extent) {
          return 'http://localhost:8080/geoserver/wfs?service=WFS&' +
              'version=1.1.0&request=GetFeature&typename=tiger:tiger_roads&' +
              'outputFormat=application/json&srsname=EPSG:4326&' +
              'bbox=' + extent.join(',') + ',EPSG:4326';
        },
        strategy: ol.loadingstrategy.bbox
      });
```
