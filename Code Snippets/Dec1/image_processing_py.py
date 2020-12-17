# Importing libraries
import keras as kr
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import os
from PIL import Image, ImageOps
from numpy.core._asarray import asarray
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense
import tensorflow as tf
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

# Read file
#def read_all_images(folder, ext):
#    all_files = []
#    # Iteration
#    for file in os.listdir(folder):
#        # Get file extension
#        file_ext = os.path.splitext(file)
#        # If file is of specified extension, get full path and append to list
#        if ext in file_ext: 
#            full_file_path = os.path.join(folder, file)
#            all_files.append(full_file_path)
#    return all_files


training_path_paper = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/paper" 
training_path_rock = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/rock" 
training_path_scissors = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/scissors"

img_list_rock = os.listdir(training_path_rock)
img_list_paper = os.listdir(training_path_paper)
img_list_scissors = os.listdir(training_path_scissors)
scale_percent = 60

num = 0
num1 = 0
num2 = 0
img_width = 300
img_height = 300
for image in img_list_paper:
    try:
        img = Image.open(os.path.join(training_path_paper, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\paper\\paper-12-01{0}.jpg'.format(num)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        num += 1
        data = asarray(gs_img)
        print(data)
    except Exception as e:
        break
#print(paper_images)
for image in img_list_rock:
    try:        
        img = Image.open(os.path.join(training_path_rock, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\rock\\rock-12-01{0}.jpg'.format(num1)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        num1 += 1
        data = asarray(gs_img)
        print(data)
    except Exception as e:
        break
    
for image in img_list_scissors:
    try:
        img = Image.open(os.path.join(training_path_scissors, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors\\scissors-12-01{0}.jpg'.format(num2)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        num2 += 1
        data = asarray(gs_img)
        print(data)
    except Exception as e:
        break

# Creating training Image data
TRAINING_DIR = "/train/"
training_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = training_datagen.flow_from_directory(
    TRAINING_DIR,
    target_size=(300,300),
    class_mode='categorical'
)

# Creating validation Image data
VALIDATION_DIR = "/val/"
validation_datagen = ImageDataGenerator(rescale = 1./255)

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size(300,300),
    class_mode='categorical'
)

# Checking image format before sending to model
# https://ai-pool.com/d/what-is-channels_first-in-keras-

#if kr.image_data_format() == 'channels_first':
#    input_shape = (3, img_width, img_height)
#else:
#    input_shape = (img_width, img_height, 3)

# Define Keras model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(300,300,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='relu'),
])

# Compiling DNN

model.compile(loss = 'categorical_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy'])

# Fitting DNN

fitting = model.fit_generator(train_generator, epochs=25, 
        validation_data = validation_generator, verbose = 1)