import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
"""
folders test and trains
"""

folder_tt = ['test', 'train']
emotions = ['angry', 'disgusted', 'fearful',
            'happy', 'sad', 'surprised', 'neutral']

# to keep count of each category
angry = 0
disgust = 0
fear = 0
happy = 0
sad = 0
surprised = 0
neutral = 0
angry_test = 0
disgust_test = 0
fear_test = 0
happy_test = 0
sad_test = 0
surprised_test = 0
neutral_test = 0

dataCSV = pd.read_csv('./dataset/data.csv')
testm = np.zeros((48, 48), dtype=np.uint8)

# list file csv by line
# d ==  Data
"""
tqdm is a Python library that allows you to output a smart progress bar by wrapping around any iterable.
A tqdm progress bar not only shows you how much time has elapsed
"""
for d in tqdm(range(len(dataCSV))):
    txt = dataCSV['pixels'][d]
    words = txt.split()

    # 48*48 pixel
    for size in range(2304):
        i = size // 48
        j = size % 48
        testm[i][j] = int(words[size])
    img = Image.fromarray(testm)

    # training script rename
    if d < 35889:
        if dataCSV['emotion'][d] == 0:
            img.save('./dataset/train/angry/'+str(angry)+'.jpg')
            angry += 1
        elif dataCSV['emotion'][d] == 1:
            img.save('./dataset/train/disgust/'+str(disgust)+'.jpg')
            disgust += 1
        elif dataCSV['emotion'][d] == 2:
            img.save('./dataset/train/fear/'+str(fear)+'.jpg')
            fear += 1
        elif dataCSV['emotion'][d] == 3:
            img.save('./dataset/train/happy/'+str(happy)+'.jpg')
            happy += 1
        elif dataCSV['emotion'][d] == 6:
            img.save('./dataset/train/neutral/'+str(neutral)+'.jpg')
            neutral += 1
        elif dataCSV['emotion'][d] == 4:
            img.save('./dataset/train/sad/'+str(sad)+'.jpg')
            sad += 1
        elif dataCSV['emotion'][d] == 5:
            img.save('./dataset/train/surprise/'+str(surprised)+'.jpg')
            surprised += 1

    # testing script rename

    if dataCSV['emotion'][d] == 0:
        img.save('./dataset/test/angry/'+str(angry_test)+'.jpg')
        angry_test += 1
    elif dataCSV['emotion'][d] == 1:
        img.save('./dataset/test/disgust/'+str(disgust_test)+'.jpg')
        disgust_test += 1
    elif dataCSV['emotion'][d] == 2:
        img.save('./dataset/test/fear/'+str(fear_test)+'.jpg')
        fear_test += 1
    elif dataCSV['emotion'][d] == 3:
        img.save('./dataset/test/happy/'+str(happy_test)+'.jpg')
        happy_test += 1
    elif dataCSV['emotion'][d] == 6:
        img.save('./dataset/test/neutral/'+str(neutral_test)+'.jpg')
        neutral_test += 1
    elif dataCSV['emotion'][d] == 4:
        img.save('./dataset/test/sad/'+str(sad_test)+'.jpg')
        sad_test += 1
    elif dataCSV['emotion'][d] == 5:
        img.save('./dataset/test/surprise/'+str(surprised_test)+'.jpg')
        surprised_test += 1
