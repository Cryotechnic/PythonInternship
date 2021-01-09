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
import traceback

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


img_width = 300
img_height = 300

data = []
num = 0
for image in img_list_scissors:
    try:
        img = Image.open(os.path.join(training_path_scissors, image))
        #img.show() # for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\paper\\paper-12-01{0}.jpg'.format(num)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        #gs_img.show() # for debug
        #data = asarray(gs_img)
        data.insert(num, 255 - asarray(gs_img))
        #print(gs_img.shape) # for debug
        num = num + 1
        #print(data) # for debug
    except Exception as e:
        traceback.print_exc()
        
#print(paper_images)
for image in img_list_rock:
    try:      
        #num1 = 0  
        img = Image.open(os.path.join(training_path_rock, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\rock\\rock-12-01{0}.jpg'.format(num)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        #data = asarray(gs_img)
        data.insert(num, 255 - asarray(gs_img))
        num = num + 1
        #print(data)
    except Exception as e:
        traceback.print_exc()
    
for image in img_list_paper:
    try:
        #num2 = 0
        img = Image.open(os.path.join(training_path_paper, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors\\scissors-12-01{0}.jpg'.format(num)
        gs_img = ImageOps.grayscale(img)
        gs_img.save(filename, "JPEG", optimize=False)
        #data = asarray(gs_img)
        data.insert(num, 255 - asarray(gs_img))
        num = num + 1
        #print(data)
    except Exception as e:
        traceback.print_exc()

#print(len(data)) # for debug 

# Creating training Image data

def splitTrainTest ( data, n, s, r, p ):
# data is a list of images. n is the number of images and labels in the training set.
    total=len(data)
    train_images = []
    train_labels = []
    test_images = []
    test_labels = []
    # set the training set
    # user wants n pictures in training set out of len(data).
    # Scissors start at 0
    # Rocks start at s
    # Papers start at s + r
    num_in_testing = total - n
    num_in_paper_test = int(num_in_testing/3)
    num_in_rock_test = num_in_paper_test
    num_in_scissors_test = num_in_testing - 2 * num_in_paper_test 
    step = (s // num_in_scissors_test)
    print(step)
    j=0
    for i in range(0,s):
      if ((i%step) == 0 and (j<num_in_scissors_test)):
        test_images.append(data[i])
        test_labels.append(2)
        j=j+1
      else: 
        train_images.append(data[i])
        train_labels.append(2)
    j=0
    for i in range(s,r+s):
      if ((i%step) == 0 and (j<num_in_rock_test)):
        test_images.append(data[i])
        test_labels.append(0)
        j=j+1
      else: 
        train_images.append(data[i])
        train_labels.append(0)
    j=0
    for i in range(s+r, total):
      if ((i%step) == 0 and j<num_in_paper_test):
        test_images.append(data[i])
        test_labels.append(1)
        j=j+1
      else: 
        train_images.append(data[i])
        train_labels.append(1)
    print(str(num_in_paper_test) + " " + str(num_in_rock_test) + " " + str(num_in_scissors_test) + " ")
    return ( train_images, train_labels, test_images, test_labels ) 


print (data[10])
print(data[10].shape)
print (len(data))
(train_images,train_labels,test_images,test_labels) = splitTrainTest(data, 2000, 840, 840, 840)
print (len(train_images))
print (len(test_images))

# Checking image format before sending to model
# https://ai-pool.com/d/what-is-channels_first-in-keras-

#if kr.image_data_format() == 'channels_first':
#    input_shape = (3, img_width, img_height)
#else:
#    input_shape = (img_width, img_height, 3)

# Define Keras model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(300, 300)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(3)
])

# Compiling DNN
#
#model.compile(loss = 'categorical_crossentropy',
#        optimizer='rmsprop',
#        metrics=['accuracy'])
#
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Print arrays containing training & testing sets + length
train_img = np.asarray(train_images)
train_lab = np.asarray(train_labels)
test_img = np.asarray(test_images)
test_lab = np.asarray(test_labels)

print(len(train_img))
print(len(train_lab))

# Fitting DNN
model.fit(train_img, train_lab, epochs=7)

# Testing DNN model for loss and accuracy
test_loss, test_acc = model.evaluate(test_img,  test_lab, verbose=2)
print(len(test_lab))
print('\nTest accuracy:', test_acc)
