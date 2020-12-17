from PIL import Image, ImageOps
import os
from numpy.core._asarray import asarray
#image = Image.open("D:\\GitHub Repos\\PythonInternship\\Code Snippets\Dec1\\rps\\rps\\resized\\scissors\\scissors-12-011680.jpg")
#image.show()

training_path_paper = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/paper" 
training_path_rock = "D:/GitHub Repos/PythonInternship/Code Snippets/Dec1/rps/rps/rock" 

img_list_paper = os.listdir(training_path_paper)
img_list_rock = os.listdir(training_path_rock)

num = 0
num_num = 0
#for image in img_list_paper:
#    paper_images = []
#    img = Image.open(os.path.join(training_path_paper, image))
#    #img.show()
#    img.resize((300, 300))
#    filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\paper\\paper-12-01{0}.jpg'.format(num)
#    rgb_img = img.convert('RGB')
#    rgb_img.save(filename, "JPEG", optimize=False)
#    num += 1
#    paper_images.append(rgb_img)
#    print(paper_images)

for image in img_list_rock:
    try:        
        img = Image.open(os.path.join(training_path_rock, image))
        #img.show() for debug
        img.resize((300, 300))
        filename = 'D:\\GitHub Repos\\PythonInternship\\Code Snippets\\Dec1\\rps\\rps\\resized\\rock\\rock-12-01{0}.jpg'.format(num_num)
        gs_img = ImageOps.grayscale(img)  
        #img.convert('RGB')
        gs_img.save(filename, "JPEG", optimize=False)
        num_num += 1
        data = asarray(gs_img)
        print(type(data))
        print(data.shape)
        print(data)
    except Exception as e:
        break

# Creating numpy array
