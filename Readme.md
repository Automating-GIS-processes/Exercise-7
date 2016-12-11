## Exercise 7: Delineate forest areas from canopy cover data

### Goal of the exercise
In this exercise we are going to work with the **[Global Forest Change Dataset](http://earthenginepartners.appspot.com/science-2013-global-forest) by Hansen et al (2013) in order to generate a forest layer for our area of interest**. The purpose of this exercise is to practice how to automate the whole processing chain including data download, processing and visualization. During this exercise you will practice the basic raster processing steps introduced in [lesson 7](https://github.com/Automating-GIS-processes/Lesson-7-Automating-Raster-Data-Processing/blob/master/Python-and-Gdal.ipynb). 

Additional hints will be added on the [hints page](https://github.com/Automating-GIS-processes/Lesson-7-Automating-Raster-Data-Processing/blob/master/hints-exercise-7) if needed.

### Source data
The Global Forest Change Dataset consists of several different products than are downloadable from [here](http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.2.html) For delineating forest areas, we will use the tree canopy cover data from year 2000 (*treecover2000*) and use a treshold of 50 % canopy cover for detecting forested areas. 

The treecover data contains information of canopy closure for all vegetation taller than 5 m height stored as a percentage per grid cell. For example value 100 would refer to complete canopy cover and value 5 would refer to 5 % canopy cover of the grid square area (30 x 30 m). For more information on the source dataset, please refer to the original publication (Hansen et al 2013), and the [data download site](http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.2.html).

## Instructions

**In order to complete the exercise you need to download all treecover tiles covering Madagascar (Problem 1) extract forest areas based on the 50 % treshold (Problem 2)**. The idea is that only by altering the input linklist, you could repeat the process for any given area in the world.

### Problem 0: Create a text file with download links
- Go to the [data download site for the Hansen data](http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.2.html) and figure out which tiles you need to download in order to cover Madagascar. For this exercise we only need a few tiles out of the whole dataset!
- Save the download links to a text file (one url per row). 

### Problem 1: Downloading the data
Using a python script, execute the following steps:
- **Create a new folder** on your computer (if it does not already exists)
- Read the textfile generated in problem 0 as input
- **Download each tile** in the list (if they do not already exist) using `urllib.request` and save the raster files into the new directory
- **Print out statistics** (min, max, mean) of each downloaded tile and save the info to a text file

*For problem 1, a starter code [downloadTiles.py](downloadTiles_starterScript.py) is provided with further instructions. However, feel free to come up with your own approach to the problem!* 

### Problem 2: Delineate forest areas from the rasters
- **Create a binary forest/non-forest layer** from each of the input tiles (using `gdal_calc.py`)
- **Mosaic** the tiles into one layer and **reduce the output resolution** to ~1km x 1km (using `gdalwarp`)
- [**Optional: Vectorize**] the forest areas and store them as a shapefile (not included in lesson, you can try to figure out how to do this!)
- Document your work on github (code, Figure of the output raster/vector)

*Problem 2 can be completed using Gdal command line utility tools `gdal_calc.py` and `gdalwarp` which can also be run as standalone tools from the Terminal/Command prompt. You can try running the tools via Python as subprocess, or use Python for generating the syntax for the tools.* 


###**Reference:**
Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013. “High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53.


Global Forest Change Webmap: http://earthenginepartners.appspot.com/science-2013-global-forest.

Data download and more details: http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.2.html
