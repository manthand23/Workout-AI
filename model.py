import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 
import cv2
import os
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.python.keras.backend import binary_crossentropy, conv2d

#this is the path for the pictures
#make this a relative path
path = "/Users/Kalp/GitHubRepos/workout_app/server_side/Content"

print(cv2.imread(path + "/training/good/3.jpg").shape)

#Transformations for the images
train = ImageDataGenerator(rescale = 1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test = ImageDataGenerator(rescale = 1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
validation = ImageDataGenerator(rescale = 1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

#gets the images from directory, resizes them, defining classes and groups(good and bad pushups)
train_dataset = train.flow_from_directory(path+"/training", target_size = (64, 64), batch_size = 32, class_mode = 'binary', )
test_dataset = test.flow_from_directory(path+"/testing", target_size = (64, 64), batch_size = 32, class_mode = 'binary', )
validation_dataset = validation.flow_from_directory(path+"/validation", target_size = (64, 64), batch_size = 32, class_mode = 'binary', )

print(train_dataset.class_indices)

#initializing the model
cnn = tf.keras.models.Sequential()

#adding a filter to the CNN
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size = 3, activation="relu", input_shape=[64, 64, 3]))

#Pooling layer -> makes the convolution layers smaller
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides=2))

#Second filter
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size = 3, activation="relu"))

#Second pooling layer
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2, strides=2))

#Flattening layer
cnn.add(tf.keras.layers.Flatten())

#Connection
cnn.add(tf.keras.layers.Dense(units = 128, activation = "relu", ))

#Output
cnn.add(tf.keras.layers.Dense(units = 1, activation = "sigmoid"))

cnn.compile(optimizer = "adam", loss = 'binary_crossentropy', metrics = ['accuracy'])

cnn.fit(x = train_dataset, validation_data = test_dataset, epochs = 20)

cnn.save('model.h5')


