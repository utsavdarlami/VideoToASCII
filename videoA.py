# --------------------IMPORT----------------------
import cv2
import numpy as np
# from time import sleep
import os
import numpy
# ------------------------------------------------

#--------------------------FOR CONVERSION ----------------------------------
# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`"    #70 levels of gray

# gscale2 = "@%#*+=-:. "

# tuple for Conversion of pixle to corresponding Character
#Greyscale to ASCII characters

gscale3 = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')

greyscaleChars = {
		"70" : "$","69" : "@","68" : "B","67" : "%","66" : "8","65" : "&","64" : "W","63" : "M","62" : "#","61" : "*","60" : "o","59" : "a","58" : "h","57" : "k","56" : "b","55" : "d","54" : "p","53" : "q","52" : "w",
		"51" : "m","50" : "Z","49" : "O","48" : "0","47" : "Q","46" : "L","45" : "C","44" : "J","43" : "U","42" : "Y","41" : "X","40" : "z","39" : "c","38" : "v","37" : "u","36" : "n","35" : "x","34" : "r","33" : "j",
		"32" : "f","31" : "t","30" : "/","29" : "\\","28" : "|","27" : "(","26" : ")","25" : "1","24" : "{","23" : "}","22" : "[","21" : "]","20" : "?","19" : "-","18" : "_","17" : "+","16" : "~","15" : "<","14" : ">",
		"13" : "i","12" : "!","11" : "l","10" : "I","9" : ";","8" : ":","7" : ",","6" : "\"","5" : "^","4" : "`","3" : "'","2" : ".","1" :  " "	,"0" :  " "
		}
#Greyscale to ASCII characters reversed
greyscaleCharsRev = {
		"0" : "$","1" : "@","2" : "B","3" : "%","4" : "8","5" : "&","6" : "W","7" : "M","8" : "#","9" : "*","10" : "o","11" : "a","12" : "h","13" : "k","14" : "b","15" : "d","16" : "p","17" : "q","18" : "w",
		"19" : "m","20" : "Z","21" : "O","22" : "0","23" : "Q","24" : "L","25" : "C","26" : "J","27" : "U","28" : "Y","29" : "X","30" : "z","31" : "c","32" : "v","33" : "u","34" : "n","35" : "x","36" : "r","37" : "j",
		"38" : "f","39" : "t","40" : "/","41" : "\\","42" : "|","43" : "(","44" : ")","45" : "1","46" : "{","47" : "}","48" : "[","49" : "]","50" : "?","51" : "-","52" : "_","53" : "+","54" : "~","55" : "<","56" : ">",
		"57" : "i","58" : "!","59" : "l","60" : "I","61" : ";","62" : ":","63" : ",","64" : "\"","65" : "^","66" : "`","67" : "'","68" : ".","69" :  " "	,"70" :  " "
		}

# function for converting a img or frame to Ascii and printing it..
def showAscii(frame):
    #global greyscaleChars
    global gscale3
   # imgScale = W/width

    # newX,newY = grayImage.shape[1]*imgScale, grayImage.shape[0]*imgScale
   #newimg = cv2.resize(grayImage,(int(newX),int(newY)))

    #newimg = cv2.resize(frame,(80,32))

    # height,width=frame.shape
    h,w=frame.shape #or row,column
    os.system('clear')
    for i in range(h):# iterates through height(ROW)
        print()
        #converts a single row of pixel to characters.....
        for j in range(w): # iterates through each column for each height(row)
            a = gscale3[((int((newimg[i][j]*16)/255)))] # newimag[i][j] gives the pixel value then it is used to obtain coressponding character from the "gscale3" tuple using index
            # a = greyscaleChars[str((int((newimg[i][j]*69)/255)))] 
            print(a,end='')
   # sleep(1)

# -----------------------------------------------------------------------------------
  
# ----------------------------MAIN ---------------------------------------
# 0 is for MY WEBCAM ///
""" videoCap = cv2.VideoCapture(0) """#uncomment this for webcam
# for any other Video File

videoCap = cv2.VideoCapture("Avengers- Endgame - Teaser Trailer - Dolby Cinema - Dolby.mp4")

if videoCap.isOpened()==False:
    print("file not reading")

while(True):

    # getting the size for TERMINAL
    screen_height,  screen_width = os.popen('stty size', 'r').read().split()

    # Capture frame-by-frame
    ret, frame = videoCap.read()

    # Our operations on the frame come here
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Resizing based on TERMINAL SIZE

    newimg = cv2.resize(grayFrame, (int(screen_width), int(screen_height)))
    
    # newimg = cv2.resize(grayFrame, dsize=(84, 34))#, interpolation=cv2.INTER_CUBIC)
    
    # showAscii(grayFrame)

    #os.system('clear')
    showAscii(newimg)
   
    # Display the resulting frame
    cv2.imshow('frame',grayFrame)
    
    if cv2.waitKey(1) == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()

#------------------------------------_END_-------------------------------
