### Create a new Vector Data Source: 

- http://localhost:8080/geoserver/web/wicket/page?72

- link data : C:\ProgramData\GeoServer\data_dir\data\richland_shapes\Data

- Compute bounding box from data & Lat/Lon

- Define projection : EPSG:26917 

- Declare Bounding Box

- [published](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.layer.LayerPage?108)

- view : http://localhost:8080/geoserver/richland/wms?service=WMS&version=1.1.0&request=GetMap&layers=richland%3ACensus_blocks&bbox=468169.09375%2C3733612.5%2C537341.5625%2C3791758.25&width=768&height=645&srs=EPSG%3A26917&styles=&format=application/openlayers

## On QGIS

#### add WMS Layer 

- create a new WMS [connection](http://localhost:8080/geoserver/richland/wms?)
- from [view layer](http://localhost:8080/geoserver/richland/wms?service=WMS&version=1.1.0&request=GetMap&layers=richland%3ACensus_blocks&bbox=468169.09375%2C3733612.5%2C537341.5625%2C3791758.25&width=768&height=645&srs=EPSG%3A26917&styles=&format=application/openlayers)

- Add layers

- Edit layer orders

[## On GeoServer](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.layer.LayerPage?117)
- see [style on pblishing tab](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?115&name=Census_blocks&wsName=richland)
- demo change to [green](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?115&name=Census_blocks&wsName=richland)

## on QGIS
- refresh layer, it now green :D

#### Change and save style
- drag census block layer from directory
- save from QGIS project as : C:\geoserver\data_dir\styles\richland_blocks.sld

## on GeoServer
- [add a new Style](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.data.StyleNewPage?119)
- click on [upload](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.data.StyleNewPage?119)
- Validate then save
- Edit Style via [publishing tab](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?147&name=Census_blocks&wsName=richland)

## on QGIS
- refresh layer, it now back to cream :D
