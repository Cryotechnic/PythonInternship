# Importing libraries
import PySimpleGUI as ui
import sys
import cv2 as cv
from PIL import Image
import io
import os
# from sys import exit as exit

num = 0

# Main source
def guiElem():
    ui.ChangeLookAndFeel('Dark')

    # Defining window layout
    layout = [[ui.Text('RPS with DNN - v.0.0.1A (Pre-release)', size=(40,1), justification='center',
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
            "Made For: Vanier College, © Ron Friedman 2021. All rights reserved ©",
            keep_on_top=True)
        elif button == 'Submit':

            filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\scissors-12-01{0}.jpg'.format(num)

        
        ret, frame = vCap.read()

        # "filter", converts to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Converting to PIL image for processing
        img = Image.fromarray(gray) # PIL from frame
        bio = io.BytesIO() # Allocates space in memory for data stream. Required for updating image
        img.save(bio, format='PNG') # Saves image to png
        imgbytes = bio.getvalue() # Placeholder to use in openCV
        wd.FindElement('image').Update(data=imgbytes) # Update Window element with new image



guiElem()