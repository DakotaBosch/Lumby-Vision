import glob
import os
import random

imgs =  glob.glob("data/*.png")

data_size = len(imgs)
ratio = 0.8
train_size = int(data_size*ratio)

random.seed()
random.shuffle(imgs)

train = imgs[:train_size] 
test = imgs[train_size:]

print (train)


with open('config/test.txt', 'w') as file:
    for text in test:
        file.write(text)
        file.write('\n')

with open('config/train.txt', 'w') as file:
    for text in train:
        file.write(text)
        file.write('\n')