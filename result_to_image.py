import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import clear_output
from time import sleep
import os

Train_Dir = '../input/training/training.csv'
Test_Dir = '../input/test/test.csv'
lookid_dir = '../input/IdLookupTable.csv'
train_data = pd.read_csv(Train_Dir)  
test_data = pd.read_csv(Test_Dir)
lookid_data = pd.read_csv(lookid_dir)
os.listdir('../input')

def recove_img_data(data, index):
    img = data.iloc[index].Image
    img = list(map(lambda x: int(x), img.split(' ')))
    img = np.array(img).reshape(96, 96)
    return img


def show_img_point(index):
    flag = 0
    for i in range(KEY_POINTS_NUM):
        plt.scatter(train_data.iloc[index, flag],
                    train_data.iloc[index, flag + 1], c='r')
        flag += 2
        plt.imshow(recove_img_data(train_data, index), cmap='gray')


index = np.random.choice(len(train_data))
show_img_point(index)
