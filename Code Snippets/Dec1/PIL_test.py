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

def splitTrainTest ( imgArr, n, s, r, p ):
      # imgArr is a list of images. n is the number of images and labels in the training set.
  total=len(imgArr)
  train_images =[]
  train_labels =[]
  test_images =[]
  test_labels =[]
  # set the training set
  # user wants n pictures in training set out of len(imgArr).
  # Scissors start at 0
  # Rocks start at s
  # Papers start at s + r
  num_in_testing = total-n
  num_in_paper_test = int(num_in_testing/3)
  num_in_rock_test = num_in_paper_test
  num_in_scissors_test = num_in_testing - 2*num_in_paper_test

  step = (s//num_in_scissors_test)
  print(step)
  j=0
  for i in range(0,s):
    if ((i%step) == 0 and (j<num_in_scissors_test)):
      test_images.append(imgArr[i])
      test_labels.append(2)
      j=j+1
    else: 
      train_images.append(imgArr[i])
      train_labels.append(2)
  j=0
  for i in range(s,r+s):
    if ((i%step) == 0 and (j<num_in_rock_test)):
      test_images.append(imgArr[i])
      test_labels.append(0)
      j=j+1
    else: 
      train_images.append(imgArr[i])
      train_labels.append(0)
  j=0
  for i in range(s+r, total):
    if ((i%step) == 0 and j<num_in_paper_test):
      test_images.append(imgArr[i])
      test_labels.append(1)
      j=j+1
    else: 
      train_images.append(imgArr[i])
      train_labels.append(1)
  print(str(num_in_paper_test)+str(num_in_rock_test)+str(num_in_scissors_test))
  return ( train_images, train_labels, test_images, test_labels )

print (data[10])
print(data[10].shape)
print (len(data))
(train_images,train_labels,test_images,test_labels) = splitTrainTest(data, 1200, 840, 840, 840)
print (len(train_images))
print (len(test_images))
