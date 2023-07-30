### Install here : 

C:\geoserver\data_dir

##### Lauch manually
- C:\Users\BBEES\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GeoServer
- [http://localhost:8080/geoserver](http://localhost:8080/geoserver/web/)

##### [Logs](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.admin.LogPage?24&filter=false) same as CDM
- see on : C:\geoserver\logs

###### [Workspaces](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.workspace.WorkspacePage?25&filter=false)
- see files at C:\geoserver\data_dir\workspaces

##### [Stores](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.store.StorePage?26&filter=false)

##### [Edit Vector Data Source](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.store.DataAccessEditPage?30&storeName=nyc&wsName=tiger)
- see C:\geoserver\data_dir\data\nyc

###### [layer](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.store.DataAccessEditPage?33&storeName=states_shapefile&wsName=topp)
- see C:\geoserver\data_dir\workspaces\topp\states_shapefile\states

## To Edit Layer
###### [click on layer name](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.layer.LayerPage?47&filter=false)
###### [Edit Layer](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?49&name=states&wsName=topp)
  - [DATA](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?49&name=states&wsName=topp)
  - [PUBLISHING](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?50&name=states&wsName=topp)
      -[Styles](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.wms.web.data.StylePage?56&filter=false)
  - [DIMENSIONS](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?51&name=states&wsName=topp)
  - [TILE CATCHING](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?52&name=states&wsName=topp)
  - [SECURITY](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.resource.ResourceConfigurationPage?53&name=states&wsName=topp)

##### [Layer Preview](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.demo.MapPreviewPage?58&filter=false)
- [OpenLayers](http://localhost:8080/geoserver/sf/wms?service=WMS&version=1.1.0&request=GetMap&layers=sf%3Aroads&bbox=589434.8564686741%2C4914006.337837095%2C609527.2102150217%2C4928063.398014731&width=768&height=537&srs=EPSG%3A26713&styles=&format=application/openlayers)
- [GML](http://localhost:8080/geoserver/sf/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=sf%3Aroads&maxFeatures=50)
- [GeoJSON](http://localhost:8080/geoserver/sf/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=sf%3Aroads&maxFeatures=50&outputFormat=application%2Fjson)

##### [Layer group](http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.data.layergroup.LayerGroupEditPage?60&group=tiger-ny)



