Purpose: To automate the task of entering measurements from microscopy images into spreadsheets

It is a time-consuming, slow process to manually open up each image, read the necessary measurements, and input them into your spreadsheet. And to repeat the process for many times.

This script works comfortably for hundreds of images, saving some 80% of the time needed (for 200 photos) to complete the data entry into a spreadsheet. Presently, the accuracy of the data is about 93%-95%, while images are also pre-processed with black and white filters to mask the background and protect the data. 

Data is also post-processed to be placed in arrays, indexed by their filenames.

========================================================================================

Before using this script, you'll need to configure:

1. Your own .json file, which is done on Google Developer Console
2. Your dependencies and software to run the python scripts
3. Ensure that both folders 'Copy the photos here' and 'Processed Photos' are empty. Copy your desired photos into the 'Copy the photos here'
4. Run 'bw'
5. Run 'main'
6. Run 'postprocess'

Done

#### Known and unresolved problems ###

--Main--
1. Code does not return 'cpt' correctly if there are photos in the subfolders.

--Post Processing--
1. Code will not recognise if one or more consecutive  photos either i) have no measurements labeled, (ii) the main code does not output any one of three measurements in each photo. 
