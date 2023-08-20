https://ucanr-igis.github.io/rspatial_scgis23/


<body>


<div class="container-fluid main-container">




<div id="header">



<h1 class="title toc-ignore"><img src='images/scgis-logo_acr_bg-trans_240x214.png' style='margin-bottom:0.5em; margin-top:1em; float:right; width:240px;'/><br/><span
class="course-title">Intro to Spatial Data Analysis with
R<br/></span><br/><span class="mod-title">Outline</span></h1>

</div>


<style type="text/css">
h1 {
  font-size: 130%;
}
p {
  font-size: 120%;
}
h1.section_head {
  text-align: center; 
  background-color: #ddd;
  padding: 0.5em;
  border-top: 4px solid gray;
  border-bottom: 4px solid gray;
}
</style>
<p style="font-size:150%;" onclick="showHide(&#39;vfelgf&#39;);return false;">
SCGIS 2023 Annual Conference
</p>
<div id="vfelgf" class="hint">
<div
style="font-size:140%; font-weight:normal; margin-left:0.5em; margin-right:0.5em;">
<p>As we get going, please:<br />
i) open the course website:<br/><tt><a
href="https://ucanr-igis.github.io/rspatial_scgis23"
class="uri">https://ucanr-igis.github.io/rspatial_scgis23</a></tt><br />
<br />
ii) introduce yourself on the community forum:<br/><tt><a
href="https://etherpad.wikimedia.org/p/rspatial-scgis23"
class="uri">https://etherpad.wikimedia.org/p/rspatial-scgis23</a></tt></p>
</div>
</div>
<div class="hrleft">

</div>
<div id="workshop-materials" class="section level1">
<h1>Workshop Materials</h1>
<li class="website">
Website: <span style="font-family:monospace;"><a
href="https://ucanr-igis.github.io/rspatial_scgis23"
target="_blank">https://ucanr-igis.github.io/rspatial_scgis23</a></span>
</li>
<li class="forum">
Community Forum: <a
href="https://etherpad.wikimedia.org/p/rspatial-scgis23"
target="_blank">https://etherpad.wikimedia.org/p/rspatial-scgis23</a>
</li>
<!------------------------   
removed because I no longer want people to use RStudio Desktop
<li class="setup">[Setup](setup.html){target="_blank"}</li>
---------------->
<li class="data">
<a href="datasets.html" target="_blank">Data files</a>
</li>
<li class="notebook">
<a href="notebooks.html" target="_blank" rel="noopener">R Notebooks</a>
</li>
<h1 id="intro-to-r-for-newbies" class="section_head">
Part 1. Intro to R for Newbies
</h1>
<p style="font-size:100%;">
August 14, 2023. 8:00a - 11:00a PDT<br/>Basic R commands, packages,
functions, scripts, importing tabular data, basic plotting
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/wrkshp-intro-pt1.html">Introduction
Part I</a>
</li>
<p class="slides_desc">
Workshop overview, resources, RStudio
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/r-intro01-getting-started.html">Getting
Started with R</a>
</li>
<p class="slides_desc">
R vs RStudio, R as a fancy calculator
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/r-intro02-packages.html">Packages,
Functions, Data Frames, and Importing Data</a>
</li>
<p class="slides_desc">
What’s in a package? Using functions, Importing CSV files as data frames
</p>
<h1 id="spatial-data-processing-and-analysis" class="section_head">
Part 2. Spatial Data Processing and Analysis
</h1>
<p style="font-size:100%;">
August 15, 2023. 8:00a - 11:00a PDT<br/>Spatial R packages, importing
spatial data, spatial transformations, geoprocesing, querying spatial
data, visualization
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/wrkshp-intro-pt2.html">Introduction
Part 2</a>
</li>
<p class="slides_desc">
Workshop overview and review of Part 2
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/rgis-integration.html">Integrating
R &amp; GIS</a>
</li>
<p class="slides_desc">
Where R falls in your GIS tool stack
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/importing-vector.html">Importing
and Plotting Vector Data</a>
</li>
<p class="slides_desc">
Spatial data classses; importing from Shapefiles, KMLs, geodatabases,
and GeoPackages; basic plotting
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/sf-manip.html">Common
Manipulations for sf Objects</a>
</li>
<p class="slides_desc">
WKT, projections, converting data frames into sf, exporting
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/tmap-leaflet.html">Visualization
with tmap and leaflet</a>
</li>
<p class="slides_desc">
Creating static and interactive web maps with tmap &amp; leaflet
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/geoprocessing_pt1.html">Geoprocessing</a>
</li>
<p class="slides_desc">
Geoprocessing functions with sf
</p>
<h1 id="extras" class="section_head">
Extras
</h1>
<li class="slides">
<a target="_blank" class="slides" href="slides/gis101.html">Foundational
GIS Concepts</a>
</li>
<p class="slides_desc">
Vector and Raster Data, Projections, Attribute Tables
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/color.html">Working with
Color</a>
</li>
<p class="slides_desc">
Color models, color functions, RColorBrewer
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/r-arcgis.html">Connecting
R &amp; ArcGIS</a>
</li>
<p class="slides_desc">
R-ArcGIS Bridge, imorting data from AGOL
</p>
<li class="slides">
<a target="_blank" class="slides" href="slides/data-apis.html">Getting
Data from APIs</a>
</li>
<p class="slides_desc">
Using data and API packages, functions to import data directly into R,
API keys
</p>
<div class="hrleft">

</div>
</div>
<div id="other" class="section level1">
<h1>Other</h1>
<li class="website">
<a href="resources.html" target="_blank" rel="noopener">Other
Resources</a>
</li>
<li class="script">
<a
href="https://github.com/ucanr-igis/rspatial_scgis23/tree/main/scripts"
target="_blank" rel="noopener">Sample Scripts</a>
</li>
<li class="acknowledgment">
<a href="acknowledgements.html" target="_blank"
rel="noopener">Acknowledgements</a>
</li>
<p><br />
<br />
</p>
</div>




</div>

<script>

// add bootstrap table styles to pandoc tables
function bootstrapStylePandocTables() {
  $('tr.odd').parent('tbody').parent('table').addClass('table table-condensed');
}
$(document).ready(function () {
  bootstrapStylePandocTables();
});


</script>

<!-- tabsets -->

<script>
$(document).ready(function () {
  window.buildTabsets("TOC");
});

$(document).ready(function () {
  $('.tabset-dropdown > .nav-tabs > li').click(function () {
    $(this).parent().toggleClass('nav-tabs-open');
  });
});
</script>

<!-- code folding -->


<!-- dynamically load mathjax for compatibility with self-contained -->


</body>

