# Importing libraries
import keras as kr
#import pandas as pd
import numpy as np
import PySimpleGUI as ui
import cv2 as cv
import sys
import io
import os
import time
from PIL import Image, ImageOps
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from numpy.core._asarray import asarray
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense
import tensorflow as tf
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import traceback


#training_path_paper = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/paper" 
#training_path_rock = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/rock" 
#training_path_scissors = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/scissors"
#
#img_list_rock = os.listdir(training_path_rock)
#img_list_paper = os.listdir(training_path_paper)
#img_list_scissors = os.listdir(training_path_scissors)
#
#data = []
#num = 0
img_list = []
#
#for image in img_list_scissors:
#    try:
#        img = Image.open(os.path.join(training_path_scissors, image))
#        #img.show() # for debug
#        img.resize((300, 300))
#        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\paper\\paper-12-01{0}.jpg'.format(num)
#        gs_img = ImageOps.grayscale(img)
#        gs_img.save(filename, "JPEG", optimize=False)
#        #gs_img.show() # for debug
#        #data = asarray(gs_img)
#        data.insert(num, 255 - asarray(gs_img))
#        #print(gs_img.shape) # for debug
#        num = num + 1
#        #print(data) # for debug
#    except Exception as e:
#        traceback.print_exc()
#        
##print(paper_images)
#for image in img_list_rock:
#    try:      
#        #num1 = 0  
#        img = Image.open(os.path.join(training_path_rock, image))
#        #img.show() for debug
#        img.resize((300, 300))
#        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\rock\\rock-12-01{0}.jpg'.format(num)
#        gs_img = ImageOps.grayscale(img)
#        gs_img.save(filename, "JPEG", optimize=False)
#        #data = asarray(gs_img)
#        data.insert(num, 255 - asarray(gs_img))
#        num = num + 1
#        #print(data)
#    except Exception as e:
#        traceback.print_exc()
#    
#for image in img_list_paper:
#    try:
#        #num2 = 0
#        img = Image.open(os.path.join(training_path_paper, image))
#        #img.show() for debug
#        img.resize((300, 300))
#        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors\\scissors-12-01{0}.jpg'.format(num)
#        gs_img = ImageOps.grayscale(img)
#        gs_img.save(filename, "JPEG", optimize=False)
#        #data = asarray(gs_img)
#        data.insert(num, 255 - asarray(gs_img))
#        num = num + 1
#        #print(data)
#    except Exception as e:
#        traceback.print_exc()
#
##print(len(data)) # for debug 
#
## Creating training Image data
#
#def splitTrainTest ( data, n, s, r, p ):
## data is a list of images. n is the number of images and labels in the training set.
#    total=len(data)
#    train_images = []
#    train_labels = []
#    test_images = []
#    test_labels = []
#    # set the training set
#    # user wants n pictures in training set out of len(data).
#    # Scissors start at 0
#    # Rocks start at s
#    # Papers start at s + r
#    num_in_testing = total - n
#    num_in_paper_test = int(num_in_testing/3)
#    num_in_rock_test = num_in_paper_test
#    num_in_scissors_test = num_in_testing - 2 * num_in_paper_test 
#    step = (s // num_in_scissors_test)
#    print(step)
#    j=0
#    for i in range(0,s):
#      if ((i%step) == 0 and (j<num_in_scissors_test)):
#        test_images.append(data[i])
#        test_labels.append(2)
#        j=j+1
#      else: 
#        train_images.append(data[i])
#        train_labels.append(2)
#    j=0
#    for i in range(s,r+s):
#      if ((i%step) == 0 and (j<num_in_rock_test)):
#        test_images.append(data[i])
#        test_labels.append(0)
#        j=j+1
#      else: 
#        train_images.append(data[i])
#        train_labels.append(0)
#    j=0
#    for i in range(s+r, total):
#      if ((i%step) == 0 and j<num_in_paper_test):
#        test_images.append(data[i])
#        test_labels.append(1)
#        j=j+1
#      else: 
#        train_images.append(data[i])
#        train_labels.append(1)
#    print(str(num_in_paper_test) + " " + str(num_in_rock_test) + " " + str(num_in_scissors_test) + " ")
#    return ( train_images, train_labels, test_images, test_labels ) 
#
#
#print (data[10])
#print(data[10].shape)
#print (len(data))
#(train_images,train_labels,test_images,test_labels) = splitTrainTest(data, 2000, 840, 840, 840)
#print (len(train_images))
#print (len(test_images))

def modelPredictions(img_list):
  loaded_model = tf.keras.models.load_model('myModel')
  # Creating prediction Keras model to predict user action
  probability_model = tf.keras.Sequential([loaded_model, tf.keras.layers.Softmax()])

  # Attempting to call on model to predict input
  predictions = probability_model.predict(np.asarray(img_list))
  return predictions

def guiElem():
    ui.ChangeLookAndFeel('Dark')

    # Defining window layout
    layout = [[ui.Text('RPS with DNN - v.1.1.0 (RC1)', size=(40,1), justification='center',
    font='Roboto 18')],
    [ui.Image(filename='', key='image')],
    [ui.ReadButton('Exit', size=(10,1), pad=((200, 0), 3), font='Roboto 18'),
    ui.RButton('Submit', size=(10,1), font='Roboto 18'),
    ui.RButton('About', size=(10,1), font='Any 18')]]

    # Create window & display without plotting
    wd = ui.Window('RPS Demo - Keras & Tensorflow Compute', location=(800,400))
    wd.Layout(layout).Finalize()
    ui.popup_annoying("This program is a Rock, Paper, Scissor game in which you, the player, uses your webcam to "
    "make a rock, paper, or scissor with your hand and have the convolutional neural network analyze the shape you made "
    "and play a random move against you, with the result being displayed at the end.", "While it is a neural network and can "
    "be classified as an artificial intelligence, please be aware that the analysis it makes is up to 76% accurate, and so "
    "there could be times where it does not recognize the shape you make properly.",
    "Please make sure that you are on a white background and that your shape is centered and clearly visible. Press 'Submit' once "
    "you are ready to begin, and enjoy! Please report and bugs or issues to Julie Plante or Ron Friedman (1926133). Thanks!")

    # Loops:
    # This will iterate every millisecond to display webcam frame and update the GUI
    # to reflect such changes.
    #
    # This should also not crash when no camera is detected/is being used by another process (WIP)

    vCap = cv.VideoCapture(0)
    counter = 0
    while True:
        button, values = wd._ReadNonBlocking()
        ret, frame = vCap.read() # read vCap device (webcam)

        if button is 'Exit' or values is None:
            vCap.release() # destroys vCam device in memory
            cv.destroyAllWindows() # Destroys preview if it exists
            sys.exit(0)

        elif button == 'About':
            ui.PopupNoWait("Hey! You've stumbled across my Rock, Paper & Scissor game using Tensorflow!",
            "This was made in collaboration with Vanier College's Julie Plante, as well as the Quebec Government's MITACS fund.",
            "Authors: Ron Friedman (GUI & Backend), Julie Plante (Research & Guidance)",
            "Made For: Vanier College, © Ron Friedman, Julie Plante 2021. All rights reserved. This work is licensed under the GPLv3 License.",
            title='Project Information', keep_on_top=True)

        elif button == 'Submit':
          # placeholder for file-saving feature
            #filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\cap\\vCap{0}.jpg'.format(counter)
            img_list.clear()
            convert = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            #cv.imwrite(filename, convert)
            counter = counter + 1
            resize = cv.resize(convert, (300, 300), interpolation = cv.INTER_AREA)
            resize = np.reshape(resize, (300, 300, 1))
            img_list.append(resize)
            cv.imshow('Preview', resize)
            time.sleep(3)
            result = modelPredictions(img_list)

            def WhatIsIt (x):
              if (x == 0):
                return("Rock")
              elif (x == 1):
                return("Paper")
              else:
                return("Scissors")

            matrixOfWinner = np.array([[0, 2, 1],[1, 0, 2],[2, 1, 0]])
            rng = np.random.default_rng()
            player1 = np.argmax(result) 
            player2 = rng.integers(0, 3)
            winner = matrixOfWinner[player1, player2]
            print("player1 played : "+WhatIsIt(player1))
            print("player2 played : "+WhatIsIt(player2))
            if (winner == 0):
              ui.PopupNoWait("User played " + WhatIsIt(player1) + ", while AI played " + WhatIsIt(player2) + " and it was a draw.", title="Results", keep_on_top=True)
              print("oh... it is a draw!")
            else:
              ui.PopupNoWait("User played " + str(WhatIsIt(player1)) + ", while AI played " + str(WhatIsIt(player2)) + " and the winner was player " + str(winner) + "! Congrats to player " + str(winner) + "!", title="Results", keep_on_top=True)
              print("The Winner is player" + str(winner))

            print("Written at" + str(result))

        # "filter", converts to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Converting to PIL image for processing
        img = Image.fromarray(gray) # PIL from frame
        bio = io.BytesIO() # Allocates space in memory for data stream. Required for updating image
        img.save(bio, format='PNG') # Saves image to png
        imgbytes = bio.getvalue() # Placeholder to use in openCV
        wd.FindElement('image').Update(data=imgbytes) # Update Window element with new image
guiElem()