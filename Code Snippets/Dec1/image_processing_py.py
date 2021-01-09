# Importing libraries
import keras as kr
#import pandas as pd
import numpy as np
import PySimpleGUI as ui
import cv2 as cv
import sys
import io
import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from numpy.core._asarray import asarray
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense
import tensorflow as tf
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import traceback

training_path_paper = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/paper" 
training_path_rock = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/rock" 
training_path_scissors = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/scissors"

img_list_rock = os.listdir(training_path_rock)
img_list_paper = os.listdir(training_path_paper)
img_list_scissors = os.listdir(training_path_scissors)

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


def kerasModel():      
  # Define Keras model
  model = tf.keras.Sequential([
      tf.keras.layers.Flatten(input_shape=(300, 300)),
      tf.keras.layers.Dense(256, activation='relu'),
      tf.keras.layers.Dense(3)
  ])

  # Compiling DNN
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

def guiElem():
    ui.ChangeLookAndFeel('Dark')

    # Defining window layout
    layout = [[ui.Text('RPS with DNN - v.0.0.1B (Pre-release)', size=(40,1), justification='center',
    font='Roboto 18')],
    [ui.Image(filename='', key='image')],
    [ui.ReadButton('Exit', size=(10,1), pad=((200, 0), 3), font='Roboto 18'),
    ui.RButton('Submit', size=(10,1), font='Roboto 18'),
    ui.RButton('About', size=(10,1), font='Any 18')]]

    # Create window & display without plotting
    wd = ui.Window('RPS Demo - Keras & Tensorflow Compute', location=(800,400))
    wd.Layout(layout).Finalize()

    # Loops:
    # This will iterate every millisecond to display webcam frame and update the GUI
    # to reflect such changes.
    #
    # This should also not crash when no camera is detected/is being used by another process (WIP)

    vCap = cv.VideoCapture(0)
    while True:
        button, values = wd._ReadNonBlocking()

        if button is 'Exit' or values is None:
            sys.exit(0)
        elif button == 'About':
            ui.PopupNoWait("Hey! You've stumbled across my Rock, Paper & Scissor game using Tensorflow!",
            "This was made in collaboration with Vanier College's Julie Plante {DESC HERE}, as well as the Quebec Government's MITACS fund.",
            "Authors: Ron Friedman (GUI & Backend), Julie Plante (Research & Guidance)",
            "Made For: Vanier College, © Ron Friedman 2021. All rights reserved.",
            keep_on_top=True)
        elif button == 'Submit':
          # placeholder for file-saving feature
            filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors-12-01{0}.jpg'.format(num)

        
        ret, frame = vCap.read() # read vCap device (webcam)

        # "filter", converts to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Converting to PIL image for processing
        img = Image.fromarray(gray) # PIL from frame
        bio = io.BytesIO() # Allocates space in memory for data stream. Required for updating image
        img.save(bio, format='PNG') # Saves image to png
        imgbytes = bio.getvalue() # Placeholder to use in openCV
        wd.FindElement('image').Update(data=imgbytes) # Update Window element with new image

guiElem()
kerasModel()