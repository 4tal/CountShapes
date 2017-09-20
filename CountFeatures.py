import cv2
import numpy

global howManyInfect
global counter
global numberOfObjectsMat
global height
global width
global tempImage


counter=1
howManyInfect=0

def infect(_height,_width):
    global numberOfObjectsMat
    global howManyInfect
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
                r,g,b=tempImage[y,x]
                if((numberOfObjectsMat[y,x]<1) and r==0):
                    numberOfObjectsMat[y,x]= 150
                    stackH.append(y)
                    stackW.append(x)
                    howManyInfect+=1


tempImage = cv2.imread('newImg64.pgm')
#print tempImage
xPos=yPos=0;
tempImage=cv2.medianBlur(tempImage,3)



#Get scaling
height= tempImage.shape[0]
width = tempImage.shape[1]
numberOfObjectsMat = numpy.zeros((height,width))



while yPos < height: #Loop through rows
    while xPos < width: #Loop through collumns

        r,g,b = tempImage[yPos,xPos]

        #print r,g,b
        if(r<150):
            r=0;
        else:
            r=255;
        if(g<150):
            g=0;
        else:
            g=255;
        if(b<150):
            b=0;
        else:
            b=255
        #print r,g,b
        #print "hey"
        tempImage[yPos,xPos]=r,g,b;

        #after.itemset((xPos, yPos, 0), 255) #Set B to 255
        #after.itemset((xPos, yPos, 1), 255) #Set G to 255
        #after.itemset((xPos, yPos, 2), 255) #Set R to 255

        xPos = xPos + 1 #Increment x position by 1
    xPos=0;
    yPos = yPos + 1 #Increment X position by


tempImage=cv2.medianBlur(tempImage,11)


xPos=yPos=0



while yPos < height: #Loop through rows
    while xPos < width: #Loop through collumns
        r,g,b = tempImage[yPos,xPos]

        if(((r==0)or(g==0)or(b==0))and (numberOfObjectsMat[yPos,xPos]<1)):
            howManyInfect=0
            infect(yPos,xPos)

            if(howManyInfect>20):
                counter+=1
        xPos = xPos + 1 #Increment Y position by 1
    xPos=0
    yPos = yPos + 1 #Increment X position by



print "finish"
print counter-1



cv2.imshow("my",tempImage);
cv2.waitKey(0)
cv2.destroyAllWindows()




