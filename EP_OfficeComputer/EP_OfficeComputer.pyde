'''
Name: Erin Pigues
Current Date: 03/26/23
Sources Consulted: py.processing.org
By submitting this work, I attest that it is my original work and that I did
not violate the University of Mississippi academic policies set forth in the
M book.
'''

one_file = True

class File():
    #class attributes
    #constuctor, parameters, object attributes
    def __init__(self, tempXcord, tempYcord):
        self.fill = fill
        self.xCord = tempXcord
        self.yCord = tempYcord
    
    #method using object and class attributes    
    def drawFile(self):
        fill(152,106,212)
        rect(self.xCord,self.yCord+5,77.5,51.226)
        rect(self.xCord,self.yCord,25.833,10,5)
        
#declare global Boolean

#keypressed function that flips to False, using a not when mouse is pressed
def keyPressed():
    global one_file
    one_file = not one_file 
    #used both mouse and keypressed because instructions mention both (#7)
def mousePressed():
    global one_file 
    one_file= not one_file
    

def setup():
    size(800,800)
    
def draw():
    global one_file
    first_file_x = 40
    first_file_y = 145
    
    if one_file == True:
        the_wall()
        the_floor()
        the_table()
        the_monitor()
        the_keyboard()
        the_mouse()
    
        file = File(first_file_x,first_file_y) #intial file in scene
        file.drawFile()
            
    else:
        the_wall()
        the_floor()
        the_table()
        the_monitor()
        the_keyboard()
        the_mouse()
        
        rows = 3
        columns = 3
        #draw multiple rows of files within 
        for x in range(rows):
            for y in range(columns):
                file = File(first_file_x + x * 103.33, first_file_y + y * 85.44)
                file.drawFile()
                print (first_file_x + x * 103.33)
    
def the_wall():
    noStroke()
    fill(182,191,227)
    rect(0,0,800,266.66) #x,y,w,h

def the_floor(): #one rect
    fill(49,20,87)
    rect(0,266.66,800,533.34)

def the_table(): #one rect
    fill(250,172,234)
    rect(10,245,775,266.66)

def the_monitor(): #two rect
    fill(107,103,106)
    rect(20,125,320,266.66)
    fill(252,247,251)
    rect(25,130,310,256.33)
    
def the_keyboard(): #two rect, eleven lines
    fill(107,103,106)
    rect(40,400,280,100)
    fill(252,247,251)
    rect(45,405,270,90)
    stroke(107,103,106)
    strokeWeight(3)
    line(45,425,315,425) #3 horizontal lines
    line(45,445,315,445)
    line(45,465,315,465)
    line(60,405,60,495) #8 vertical lines... x + 33.75
    line(93.75,405,93.75,495)
    line(127.5,405,127.5,495)
    line(161.25,405,161.25,495)
    line(195,405,195,495)
    line(228.75,405,228.75,495)
    line(262.5,405,262.5,495)
    line(296.25,405,296.25,495)
    noStroke()

def the_mouse():
    ellipse(385,435,60,80)
    stroke(250,172,234)
    strokeWeight(3)
    line(355,420,455,420)
    line(385,420,385,320)
    noStroke()


    
    
