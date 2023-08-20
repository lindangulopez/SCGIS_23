####################### ####################### ####################### ####################### ####################### ####################### 
####################### ####################### ####################### ####################### ####################### ####################### 
####################### ####################### ####################### ####################### ####################### ####################### 

# Description:	impor and plot data, 	create digital surface model (DSM), digital terrain model (DTM), and canopy height model (CHM) rasters from ALS data; 
#               computation of summary metrics and tree segmentation
# Date:				August 2023
# Purpose: introduction to lidar workshop 

####################### ####################### ####################### ####################### ####################### ####################### 
####################### ####################### ####################### ####################### ####################### ####################### 
####################### ####################### ####################### ####################### ####################### ####################### 

require(lidR)
require(raster)
require(tidyverse)


## alternative data 

#LASfile <- system.file("extdata", "Topography.laz", package="lidR")
#lidar_pc <- readLAS(LASfile)
#plot(lidar_pc, size = 3, bg = "white")


Path <- "D:/LiDAR_workshop/LiDAR_workshop/Data/" ## define your path directory 
setwd(Path)
###################################
### Perimeter of the study site 
Perimeter <- shapefile(paste0(Path, "/shp/PerimeterS.shp"))
plot(Perimeter)

## import data and get information
lidar_pc <- readLAS(paste0(Path, "/ALS/ALS_Selway.laz")) 
#lidar_pc <- readLAS(paste0(Path, "/ALS/ALS_Selway.laz"), select = "xyzi", filter = "-drop_z_below 1400") #  explore options such as filter = "-keep_first", filter = " -drop_z_below 10"
print(lidar_pc)
print(header(lidar_pc))
plot(lidar_pc)
plot(lidar_pc, color = "Z", bg = "white", axis = TRUE, legend = TRUE) 
plot(lidar_pc, color = "Intensity")
plot(lidar_pc, color = "ScanAngleRank", pal = rainbow)


########################### DIGITAL TERRAIN MODEL 

dtm_tin <- rasterize_terrain(lidar_pc, res = 1, algorithm = tin())
dtm_tin2 <-  rasterize_terrain(lidar_pc, algorithm = knnidw(k = 6L, p = 2))
plot(dtm_tin)
plot(dtm_tin2)
dtm_r<- raster(dtm_tin) %>% crop(., Perimeter)  %>% mask(., Perimeter)
plot(dtm_r)
plot(Perimeter, add=T)

## DIGITAL SURFACE MODEL 

dsm <- rasterize_canopy(lidar_pc, res = 1, dsmtin())
dsm_r<- raster(dsm) %>% crop(., Perimeter)  %>% mask(., Perimeter)
col <- height.colors(15)
plot(dsm_r, col=col)
plot(Perimeter, add=T)

########### HEIGHT NORMALIZATION 

ground_pc <- filter_ground(lidar_pc) # this function filters the ground returns
plot(ground_pc, size = 3)


nlas <- normalize_height(lidar_pc, tin(), dtm = dtm_tin)
lidR::plot(nlas)

nlas <- lidar_pc - dtm_tin 
plot(nlas)

writeLAS(nlas, paste0(Path, "/outputs/Selway_pcNormalized.laz"))

## CANOPY HEIGHT MODEL 
chm <- rasterize_canopy(nlas, res = 1, algorithm = p2r())
col <- height.colors(25)
plot(chm, col = col)

# Khosravipour et al. pitfree algorithm
chm <- rasterize_canopy(nlas, res = 1, pitfree(thresholds = c(0, 10, 20, 30), max_edge = c(0, 1.5))) 
chm <-  raster(chm)  %>% crop(., Perimeter)  %>% mask(., Perimeter)
plot(chm)
plot(Perimeter, add=T)

writeRaster(chm, "chm.tif")

################################# AREA BASED METRICS

cloud_metrics(nlas, func = ~mean(Z))
mean_height<- pixel_metrics(nlas, func = ~mean(Z), res=5)

plot(mean_height)
metrics <- pixel_metrics(nlas2, .stdmetrics, 5) # calculate standard metrics

plot(metrics$zq95, col = height.colors(50))
plot(metrics$zq5, col = height.colors(50))

################################# TREE LEVEL ANALYSIS
TreeArea <-  shapefile(paste0(Path, "/shp/TreeSeg_area.shp"))
plot(TreeArea, add=T)

nlas_s <- clip_roi(nlas, TreeArea)
chm_s <- chm %>% crop(., TreeArea) %>% mask(., TreeArea)
plot(nlas_s)
plot(chm_s)

## Tree segmentation 
plot(nlas)

ttops_5m<- locate_trees(nlas_s, lmf(ws = 5))
ttops_8m<- locate_trees(nlas_s, lmf(ws = 8))

par(mfrow=c(1,2))
plot(chm_s, col = height.colors(50))
plot(sf::st_geometry(ttops_5m), add = TRUE, pch = 3)
plot(chm_s, col = height.colors(50))
plot(sf::st_geometry(ttops_8m), add = TRUE, pch = 3)

plot(nlas_s) |> add_treetops3d(ttops_5m)
plot(nlas_s) |> add_treetops3d(ttops_8m)

crown_segmentation<- segment_trees(nlas_s, silva2016(chm_s, ttops_5m,  max_cr_factor = 0.5, exclusion = 0.2, ID ="treeID"))
crown_segmentation<- segment_trees(nlas_s, li2012(dt1 = 1.5, dt2 = 2, R = 2, Zu = 15, hmin = 2, speed_up = 10))

plot(crown_segmentation, bg = "white", size = 4, color = "treeID") # visualize trees
tree10 <- filter_poi(crown_segmentation, treeID == 50)
plot(tree10, size = 8, bg = "white")

cmetrics <- crown_metrics(crown_segmentation, .stdtreemetrics, geom = "convex")
plot(cmetrics["convhull_area"], main = "Tree crowns")
