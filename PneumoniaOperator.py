
# Created by James Jasper Fadden O'ROarke
# This is a pair program for the project's image classifier. It loads a saved h5 model that has been trained and, given any number of 
import flask
import wtforms
import werkzeug.utils
import flask_wtf
import datetime

import tensorflow
import keras
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Dropout
from keras.layers import Conv2D
from keras.layers import Flatten
from keras.layers import MaxPool2D
from keras.models import Sequential
import numpy as np
import image_dataset_loader
import csv
import os

#Load a dataset of images, ignoring their labelling, from a single folder a directory below UserInput. Due to requirements, a second folder is required there but should always be left empty. All of the files are collected in default operating system order.
(dataImage, unusedTrainDataLabel), = image_dataset_loader.load('./PneumoniaDataset', ['UserInput'], shuffle=False)

print(len(dataImage))

model = keras.models.load_model('PneumoniaModel.h5')
imageNum = len(os.listdir('./PneumoniaDataset/UserInput/files'))

np.reshape(dataImage, (imageNum, 64, 64, 3))



output = model.predict(dataImage)


#Program output is via csv files, with the first column for names and the second for diagnosis.
#Ensure the that "ignore" folder is empty or else the program will crash from patientNames going OoB
file = open('prediction.csv', 'w')
writer = csv.writer(file)
patientNames = os.listdir('./PneumoniaDataset/UserInput/files')
patients = np.array(patientNames)


count = 0
for i in output:
    #i contains the predictions, and its second element show's the model's Pneumonia Likelihood
    if (i[1] > 0.00367):
        writer.writerow([patients[count], 'Pneumonia'])
    else:
        writer.writerow([patients[count], 'Healthy'])
    count = count + 1

file.close()