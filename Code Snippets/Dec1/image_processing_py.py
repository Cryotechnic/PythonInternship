# Importing libraries
#import tensorflow as tf
#import keras as kr
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import os
import cv2

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
for image in img_list_paper:
    try:
        img = cv2.imread(os.path.join(training_path_paper, image))
        print("Resizing")
        img_res = cv2.resize(img, (300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\paper\\paper-12-01{0}.jpg'.format(num)
        cv2.imwrite(filename, img)
        num += 1
        print(filename)
    except Exception as e:
        break
for image in img_list_rock:
    try:
        img = cv2.imread(os.path.join(training_path_rock, image))
        print("Resizing")
        img_res = cv2.resize(img, (300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\rock\\rock-12-01{0}.jpg'.format(num)
        cv2.imwrite(filename, img)
        num += 1
        print(filename)
    except Exception as e:
        break
for image in img_list_scissors:
    try:
        img = cv2.imread(os.path.join(training_path_scissors, image))
        print("Resizing")
        img_res = cv2.resize(img, (300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors\\scissors-12-01{0}.jpg'.format(num)
        cv2.imwrite(filename, img)
        num += 1
        print(filename)
    except Exception as e:
        break
    
# Lists all files of .jpg extension
# jpg_files_rock = read_all_images(training_path_rock, 'jpg')
# jpg_files_paper = read_all_images(training_path_paper, 'jpg')
# jpg_files_scissors = read_all_images(training_path_scissors, 'jpg')