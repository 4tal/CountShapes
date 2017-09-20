import cv2
import numpy

def infect(_height,_width,counter):
    global numberOfObjectsMat
    global howManyInfect
    global newImg
    numberOfObjectsMat[_height,_width]=counter
    stackH=[]
    stackW=[]
    stackH.append(_height)
    stackW.append(_width)
    while(len(stackH)>0):
        tempH=stackH.pop()
        tempW=stackW.pop()
        for y,x in [(tempH+i,tempW+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
            if((0<y and y<height) and (0<x and x < width)):
                r,g,b=newImg[y,x]
                if((numberOfObjectsMat[y,x]<1) and r==0):
                    numberOfObjectsMat[y,x]= 150
                    stackH.append(y)
                    stackW.append(x)
                    howManyInfect+=1
def myObjectCounter(img):
    global height
    global width
    global numberOfObjectsMat
    global howManyInfect
    global newImg

    currentNumberOfObjects=1

    height= img.shape[0]
    width = img.shape[1]
    newImg=cv2.medianBlur(img,3)
    xPos=yPos=0
    #Get scaling

    numberOfObjectsMat = numpy.zeros((height,width))
    while yPos < height: #Loop through rows
        while xPos < width: #Loop through collumns
            r,g,b = newImg[yPos,xPos]
            if(r<150):
                r=0
            else:
                r=255
            if(g<150):
                g=0
            else:
                g=255
            if(b<150):
                b=0
            else:
                b=255

            #if(yPos<(height/95) or (yPos>(95*(height/100))) or (xPos>(95*(width/100))) or xPos<(5*(width/100))):
            #    r=255
            #    g=255
            #    b=255
            newImg[yPos,xPos]=r,g,b

            xPos = xPos + 1 #Increment x position by 1
        xPos=0
        yPos = yPos + 1 #Increment X position by
    newImg=cv2.medianBlur(newImg,9)
    xPos=yPos=0
    while yPos < height: #Loop through rows
        while xPos < width: #Loop through collumns
            r,g,b = newImg[yPos,xPos]

            if(((r==0)or(g==0)or(b==0))and (numberOfObjectsMat[yPos,xPos]<1)):
                howManyInfect=0
                infect(yPos,xPos,currentNumberOfObjects)
                #print howManyInfect
                if(howManyInfect>200):
                    currentNumberOfObjects+=1
                    #print howManyInfect
            xPos = xPos + 1 #Increment Y position by 1
        xPos=0
        yPos = yPos + 1 #Increment X position by
    return currentNumberOfObjects-1

"""
tempImage = cv2.imread('newImg64.pgm')
cv2.imshow("Idan",tempImage)
cv2.waitKey(1)
print myObjectCounter(tempImage)
cv2.imshow("Idan",newImg)
cv2.waitKey(0)
"""




