Before using this script, you'll need to configure:

1. Your own .json file, which is done on Google Developer Console
2. Your dependencies and software to run the python scripts
3. Ensure that both folders 'Copy the photos here' and 'Processed Photos' are empty. Copy your desired photos into the 'Copy the photos here'
4. Run 'runmefirst'
5. Run 'runme'

Done

#### Known and unresolved problems ###

--Pre Processing--
1. No dynamic thresholding, currently fixed at 120.

--Main--
1. Code does not return 'cpt' correctly if there are photos in the subfolders.

--Post Processing--
1. Code will not recognise if one or more consecutive scratch photos either i) Have no scratch measurements labeled, (ii) the main code does not output any one of three measurements in each photo. 
--- Result: Array is not properly organised, and will need additional work to rearrange the data.

--GUI--
1. No progress bar implemented.

