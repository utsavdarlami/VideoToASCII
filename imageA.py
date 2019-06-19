import cv2
import numpy as np
from time import sleep
import os
### working

#imagefile= cv2.imread('1024px-Python-logo-notext.svg.png')
imagefile=cv2.imread('logo.jpg')#put your own image file

#for scaling
#W=70

grayImage =  cv2.cvtColor(imagefile,cv2.COLOR_BGR2GRAY)

# print('height,weight',grayImage.shape)
# grayArray=np.array(grayImage)

# showing image file

cv2.imshow('image',grayImage)

# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`"    #70 levels of gray

#gscale2 = "@%#*+=-:. "

gscale3 = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')


def showAscii(frame):
    global gscale3

      # getting the size for TERMINAL
    screen_height,  screen_width = os.popen('stty size', 'r').read().split()


    # height,width=grayImage.shape
    # imgScale = W/width

    # newX,newY = grayImage.shape[1]*imgScale, grayImage.shape[0]*imgScale
     #newimg = cv2.resize(grayImage,(int(newX),int(newY)))

    #newimg = cv2.resize(frame,(80,32))
    newimg = cv2.resize(frame, dsize=(int(screen_width), int(screen_height)), interpolation=cv2.INTER_CUBIC)

    # height,width=newimg.shape
    h,w=newimg.shape #or row,column
    os.system('clear')
    for i in range(h):# iterates through height(ROW)
        print()
        #converts a single row of pixel to characters.....
        for j in range(w): # iterates through each column for each height(row)
            a = gscale3[(int((newimg[i][j]*16)/255))] # newimag[i][j] gives the pixel value then it is used to obtain coressponding character from the "gscale3" tuple using index
            print(a,end='')
   # sleep(1)

showAscii(np.array(grayImage))

