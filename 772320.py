from graphics import *

acceptableColours = ["blue","green","red","orange","magenta","cyan"]
gridValues = []
gridColours = []

def main():
    colours, size = getInputs()   
    win = drawWindow(size*100,size*100,colours,size)
    swapPatches(win, colours,size)
    
def swapPatches(win, colour, size):
    ##This function will swap the selected patches by mouse click
    continueLoop = True
    while continueLoop == True:
        
        x1,y1 = calculateGrid(win)
        
        #Selects the chosen rectangle for the user to see where they have clicked
        square = drawClearSquare(win, x1,y1)
        
        x2,y2 = calculateGrid(win)
        
        square1 = drawClearSquare(win, x2,y2)
        
        time.sleep(0.1)
        
        if (y2 != y1) or (x2 != x1):
            #Gets the colour of the chosen squares
            colour1 = gridColours[x1 + y1 * size]
            colour2 = gridColours[x2 + y2 * size]
            
            #Gets the pattern of the chosen square
            patch1 = gridValues[x1 + y1 * size]
            patch2 = gridValues[x2 + y2 * size]
            
            #Draws the new square with the correct colouring
            if patch2 == "F":
                drawPatch1(win, (x1 * 100), (y1 * 100), colour[colour2])
            else:
                drawPatch2(win, (x1 * 100), (y1 * 100), colour[colour2])
                
            if patch1 == "F":
                drawPatch1(win, (x2 * 100), (y2 * 100), colour[colour1])
            else:
                drawPatch2(win, (x2 * 100), (y2 * 100), colour[colour1])
                
            #Changes the value to consider the new swap
            gridValues[x2 + y2 * size] = patch1
            gridValues[x1 + y1 * size] = patch2
            
            gridColours[x2 + y2 * size] = colour1
            gridColours[x1 + y1 * size] = colour2
        
        
        square.undraw()
        square1.undraw()
        
def calculateGrid(win):
    ##Calculates where on the screen the user has clicked, getting an x and y value on the grid
    p = win.getMouse()
    
    x = p.getX()
    y = p.getY()
        
    x = int(x / 100)
    y = int(y / 100)
    
    return x,y
        
def drawClearSquare(win,x,y):
    ##Draws a clear square around the selected patch
    square = Rectangle(Point((x * 100),(y * 100)), Point((x * 100) + 100,(y * 100) + 100))
    square.setOutline("black")
    square.setWidth(5)
    square.draw(win)
    
    return square
    
def getInputs():
    ##This function will get the colours and the size of the window for later use
    colours = []
    chosenColours = []
    
    for i in range(3):
        reenter = True
        while reenter == True:
            colour = (input("Enter a colour: ")).lower()
            if (not (colour in acceptableColours)):
                #Checks colour is within those which are allowed
                print("INVALID COLOUR!")
            elif (colour in chosenColours):
                #Checks colour has not already been used
                    print("COLOUR ALREADY CHOSEN!")
            else:
                colours.append(colour)
                chosenColours.append(colour)
                reenter = False
  
    loopAgain = True
    while loopAgain == True:
        #Loops until the size selected a suitable selection
        size = eval(input("Enter the size of the patch window: "))
        if (size == 5) or (size == 7) or (size == 9):
           loopAgain = False 
        else:
            print("INVALID SIZE!")
        
    return colours, size

def drawPatch1(win, x, y, Colour):
    ##Draws the first patch with window, x start, y start and it's colour in the calling
    
    #Draws a white background for the patch to be drawn in
    drawWhiteBackground(win, x, y)
    
    for vertical in range (y,y + 90, 20):
        for horizontal in range(x, x+ 90, 20):
            #Draws the square for the text to be drawn in
            square = Rectangle(Point(horizontal,vertical), Point(horizontal + 20,vertical + 20))
            square.setOutline(Colour)
            square.draw(win)
            
            #Draws the text within the square drawn
            text = Text(Point(horizontal + 10, vertical + 10) , "hi!")
            text.setOutline(Colour)
            text.setSize(7)
            text.draw(win)
            
def drawPatch2(win, x, y, Colour):
    ##Draws the second patch with window, x start, y start and it's colour in the calling
    
    #Draws a white background for the patch to be drawn in
    background = drawWhiteBackground(win, x, y)
    
    for vertical in range (y,y + 90, 20):
        for horizontal in range(x, x + 90, 20):
            #Draws the coloured circle in the background
            backCircle = Circle(Point(horizontal + 10, vertical + 10), 10)
            backCircle.setOutline(Colour)
            backCircle.setFill(Colour)
            backCircle.draw(win)
            
            #Draws the rectangle over the circle, alternating each time it is drawn
            if (horizontal % 40 == 0):
                drawCoverRect(win, "White", horizontal, vertical + 10,  horizontal + 20, vertical + 20)
            else:
                drawCoverRect(win, "White", horizontal, vertical,  horizontal + 10, vertical + 20)
            
            #Draws a plain circle with a coloured outline to finish the plain half of the circle
            innerCircle = Circle(Point(horizontal + 10, vertical + 10), 10)
            innerCircle.setOutline(Colour)
            innerCircle.draw(win)

def drawWhiteBackground(win, x, y):
    background = Rectangle(Point(x, y), Point(x + 100, y + 100))
    background.setFill("White")
    background.setOutline("White")
    background.draw(win)
 
def drawCoverRect(win, colour, x1, y1, x2, y2):
    ##Used by patch 2 to avoid repeating the following code in the statement
    
    coverRect = Rectangle(Point(x1, y1), Point(x2, y2))
    coverRect.setFill(colour)   
    coverRect.setOutline(colour)
    coverRect.draw(win)
    
def drawWindow(x,y, colour, size):
    ##This starts and controls the initial drawing 
    
    win = GraphWin("Patch Window",x,y)
    colourCounter = 0
    
    #Draws each individual patch by calling the appropriate function
    for vert in range(0, y, 100):
        for horz in range(0, x, 100):
            if (horz==(x / 2) - 50) or (vert == (x / 2) - 50):
                drawPatch1(win, horz, vert, colour[colourCounter])
                gridValues.append("F")
            else:
                drawPatch2(win, horz, vert, colour[colourCounter])
                gridValues.append("P")

            gridColours.append(colourCounter)
            colourCounter = colourCounter + 1
            
            
            if colourCounter >= 3:
                colourCounter = 0
    
    return win
    
main()