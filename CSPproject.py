from cmu_graphics import *

Line(200,0,200,400)
Label("Continuous",100,50,size = 25)
Label("Standard",300,50,size = 25)
#servo1
Rect(65,118,70,150)

#servo2
Rect(265,118,70,150)

CservoHorn = Group(
Arc(100,140,23,100,270,180,fill = 'lightGrey'),
Circle(100,120,3,fill = 'white'),
Circle(100,110,3,fill = 'white'),
Circle(100,100,3,fill = 'white'),
Arc(100,140,23,100,90,180,fill = 'lightGrey'),
Circle(100,160,3,fill = 'white'),
Circle(100,170,3,fill = 'white'),
Circle(100,180,3,fill = 'white'),
Circle(100,140,13, fill = 'lightGrey',borderWidth = 2,border = 'white'),
Circle(100,140,5)
    )
 
SservoHorn = Group(
Arc(300,140,23,100,270,180,fill = 'lightGrey'),
Circle(300,120,3,fill = 'white'),
Circle(300,110,3,fill = 'white'),
Circle(300,100,3,fill = 'white'),
Arc(300,140,23,100,90,180,fill = 'lightGrey'),
Circle(300,160,3,fill = 'white'),
Circle(300,170,3,fill = 'white'),
Circle(300,180,3,fill = 'white'),
Circle(300,140,13, fill = 'lightGrey',borderWidth = 2,border = 'white'),
Circle(300,140,5),
    )             
    
C_leftButton = Group(
Rect(20,310,77,55,fill = 'lime'),
Label('Left', 59,337.5,size = 20)
    )
    
C_rightButton = Group(
Rect(103,310,77,55,fill = 'red'),
Label('Right', 141,337.5,size = 20)
    )
    
S_leftButton = Group(
Rect(220,340,77,55,fill = 'lime'),
Label('Left', 259,367.5,size = 20)
    )
    
S_rightButton = Group(
Rect(303,340,77,55,fill = 'red'),
Label('Right', 341,367.5,size = 20)
    )
    
S_centerButton = Group(
Rect(262,278,77,55,fill = 'skyBlue'),
Label('Center', 300,305.5,size = 20)
    )
                
cursor = Group(
Rect(157,100,6,15,fill = 'white',border = 'black',borderWidth = 0.5),   
Polygon(152,110,160,105,168,110,160,90,fill = 'white',border = 'black',borderWidth = 0.5)
    )                
cursor.rotateAngle = -24

def onMousePress(mouseX,mouseY):
    cursor.centerX = mouseX
    cursor.centerY = mouseY
SservoHorn.rotateAngle = 0
def onStep():
    if C_leftButton.containsShape(cursor):
        CservoHorn.rotateAngle -= 5
    if C_rightButton.containsShape(cursor):
        CservoHorn.rotateAngle += 5
                 
    angles = [-90,90]
    if S_leftButton.containsShape(cursor):
        if SservoHorn.rotateAngle != angles[0]:
            SservoHorn.rotateAngle -= 2
            
    if S_centerButton.containsShape(cursor):
        if SservoHorn.rotateAngle <= 0:
            SservoHorn.rotateAngle += 2
            
    if S_rightButton.containsShape(cursor):
        if SservoHorn.rotateAngle != angles[1]:
            SservoHorn.rotateAngle += 2
            
    if S_centerButton.containsShape(cursor):
        if SservoHorn.rotateAngle >= 0:
            SservoHorn.rotateAngle -= 2
                 
                     


cmu_graphics.run()