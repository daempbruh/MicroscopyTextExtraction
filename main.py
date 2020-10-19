# Import libraries
import io
import os
import pandas as pd
import timeit
import warnings
from pathlib import Path
from google.cloud import vision

warnings.filterwarnings('ignore')

# Edit the directories accordingly here
json_directory = 'C:/Users/320100141/Desktop/Python Venv/VisionAI/venv/ServiceAccountToken.json'
photo_directory = 'C:/Users/320100141/Desktop/Python Venv/VisionAI/Processed Photos'

# Run software keys to utilise Google Services
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_directory

# Import imaging client
client = vision.ImageAnnotatorClient()

# Checks for the number of files found
cpt = sum([len(files) for r, d, files in os.walk(photo_directory)])
print(cpt, "photos found")  # To check the length of the files in the given directory

# Returns a list of the file names; serves as label
plist = os.listdir(photo_directory)
print("The photos are:", plist)

# To create the master DataFrame and its counter
df = pd.DataFrame(columns=['photo', 'width'])
i = 0

pathlist = Path(photo_directory).rglob('**/*.jpg')
for path in pathlist:
    # Reads the image into the code
    start = timeit.default_timer()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    # Construct image instance and annotate image response
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    stop = timeit.default_timer()
    i = i + 1
    print(int(100*i/cpt), "% completed. ~", 10+10*round(int((stop - start)*(cpt-i))/10), "seconds left.")

    for text in texts:
        df = df.append(
            dict(
                photo=plist[i-1],
                width=text.description
            ),
            ignore_index=True
        )

        # Data cleaning
        df = df[pd.to_numeric(df['width'], errors='coerce').notnull()]
        df = df.select_dtypes(exclude=['int64'])
        df['width'] = df['width'].astype(str).astype(float).round()
        df_e = df[~(df['width'] <= 100)]
        df_e['width'] = df_e['width'].div(1000)

# Change to your desired filename
df_e.to_csv('raw.csv')

print("Extraction complete.")