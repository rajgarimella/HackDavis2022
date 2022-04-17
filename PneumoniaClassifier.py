
# Created by James Jasper Fadden O'ROarke
# This is a image classifer built from the Keras python library and based on previous machine learning attempts. It is designed to determine whether a lung scan is suffering from pneumonia or is healthy, serving as a core part of the project. There is logic for the classifer framework, training the classifer, and saving/loading for use. 
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
import os

#This special function imports training/testing images/labels from a hierarchy of folders, inferring labels based on folder names and setting based on similar metadata between images.
(trainDataImage, trainDataLabel), = image_dataset_loader.load('./PneumoniaDataset', ['TrainingData'])

model = Sequential()

model.add(Conv2D(60, kernel_size = 1, activation='relu', input_shape=(64, 64, 3), padding='same'))
model.add(Dropout(0.2))

model.add(Conv2D(35, kernel_size = 1, activation='relu', padding='same'))
model.add(Dropout(0.2))

model.add(MaxPool2D(2, 2))

model.add(Conv2D(20, kernel_size = 1, activation='relu', padding='same'))
model.add(Dropout(0.2))

model.add(MaxPool2D(2, 2))

model.add(Conv2D(10, kernel_size = 1, activation='relu', padding='same'))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(2, activation='softmax'))

model.summary()

# This function will take a variable, number of rows (corresponds to the number of images/labels in the variable), and check for a boolean that shows whether the variable being reshaped is an image
def Reshaper(var, imNumber, isImage):
    if(isImage==True):
        np.reshape(var, (imNumber, 64, 64, 3))
    else:
        np.reshape(var, (imNumber, 1))
    return var

numImages = len(os.listdir('./PneumoniaDataset/TrainingData/healthyyy')) + len(os.listdir('./PneumoniaDataset/TrainingData/pneumonia'))

trainDataImage = Reshaper(trainDataImage, numImages, True)
trainDataLabel = Reshaper(trainDataLabel, numImages, False)

def OneHotEncode(DataLabel, labelNum):
    OneHot = np.zeros((labelNum, 2))
    count=0

    while (count < labelNum):
        OneHot[count][DataLabel[count].astype(int)] = 1
        count=count+1

    return OneHot

trainDataLabel = OneHotEncode(trainDataLabel, numImages)



model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Here, we give the model a training dataset to estimate from and a training answer set to score itself on, which correspond to the images and labels respectively.
model.fit(trainDataImage, trainDataLabel, epochs=25, batch_size=25)

#print("Model Saved.")

model.save('PneumoniaModel.h5')


