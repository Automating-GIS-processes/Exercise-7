
"""
Starter code for Automating-GIS-processes/exercise-6 Problem 1:

    - Create a new folder on your computer (if it does not already exists)
    - Download each tile in the list (if they do not already exist) and save the raster files into the new directory

There are 7 TASKS embedded in the code which you need to complete in order to solve problem 1.

Source data:
http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.2.html (Hansen et al 2013).

Reference:
Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman,
S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013.
“High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53.

"""
#Import modules
import os
import urllib.request


# Define Variables:
root_dir = r"/home/geo/"                            # Root directory
foldername = "HansenData"                           # Name of the new folder
result_dir =  os.path.join(root_dir, foldername)    # Full directory for the new folder
input_textfile = "linklist.txt"                     # name of the text file that contains the download links (one link per row)
DownloadCount = 0                                   # integer variable which will count how many files you have downloaded


# TASK 1: Create destination folder 'result_dir' (using os.makedirs) IF the destination folder does not already exist
# see https://github.com/Python-for-geo-people/Lesson-5-Reading-Writing/blob/master/Lesson/writing-to-file.md#-useful-functions-related-to-filepaths

# INSERT YOUR CODE HERE FOR TASK 1

# Open the text file and read each line into a list
with open(input_textfile) as f:
    LinkList =                                      # TASK 2: read the input file line by line into the LinkList. As a result you should have a list where each item is a link to one raster tile.

for url in LinkList:
    # extract only filename from the url
    filename =                                      # TASK 3: store only the filename into this variable

    #filepath for the file that will be downloaded:
    filepath  = os.path.join(result_dir, filename)

    # if file already exists, don't copy it again:
    if  :                                           # TASK 4: check if the file exists already using the os-module.
        print (filepath + " already exists")

    else:  # if file does not already exist...
        try:
            urllib.request.urlretrieve( , )         # TASK 5: insert correct wariables into the urlretrieve-function. WHAT are you downloading and WHERE will it be stored.
            print ("")                              # TASK 6: insert an informative message that will be printed when the download is complete.
            DownloadCount =                         # TASK 7: Update the variable DownloadCount so that it counts how many files you have downloaded.

        except:                                     # In case there is an error with downloading the data the code will jump over that spesific file
            print ("Could not download" + filename)

print("Download completed. Number of tiles downloaded: " + DownloadCount)

# DONE! At this point you should have all the tiles listed in the linklist downloaded in the result folder as .tif -files and you can proceed to problem 2.
