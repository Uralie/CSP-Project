import cmu_graphics
from cmu_graphics import *

Line(200, 0, 200, 400)
Label("Continuous", 100, 40, size=25)
Label("Continuosly rotates left or right", 100,70,size = 12)
Label("Standard", 300, 40, size=25)
Label("Goes to inputed value", 300,65,size = 12)
Label("between -90 and 90", 300, 80, size=12)

Rect(65, 118, 70, 150)
Rect(265, 118, 70, 150)

CservoHorn = Group(
    Arc(100, 140, 23, 100, 270, 180, fill='lightGrey'),
    Circle(100, 120, 3, fill='white'),
    Circle(100, 110, 3, fill='white'),
    Circle(100, 100, 3, fill='white'),
    Arc(100, 140, 23, 100, 90, 180, fill='lightGrey'),
    Circle(100, 160, 3, fill='white'),
    Circle(100, 170, 3, fill='white'),
    Circle(100, 180, 3, fill='white'),
    Circle(100, 140, 13, fill='lightGrey', borderWidth=2, border='white'),
    Circle(100, 140, 5)
)

SservoHorn = Group(
    Arc(300, 140, 23, 100, 270, 180, fill='lightGrey'),
    Circle(300, 120, 3, fill='white'),
    Circle(300, 110, 3, fill='white'),
    Circle(300, 100, 3, fill='white'),
    Arc(300, 140, 23, 100, 90, 180, fill='lightGrey'),
    Circle(300, 160, 3, fill='white'),
    Circle(300, 170, 3, fill='white'),
    Circle(300, 180, 3, fill='white'),
    Circle(300, 140, 13, fill='lightGrey', borderWidth=2, border='white'),
    Circle(300, 140, 5),
)

C_leftButton = Group(
    Rect(20, 310, 77, 55, fill='lime'),
    Label('Left', 59, 337.5, size=20)
)

C_rightButton = Group(
    Rect(103, 310, 77, 55, fill='red'),
    Label('Right', 141, 337.5, size=20)
)

inputRect = Rect(250, 300, 100, 30, fill='white', border='black')
inputLabel = Label('', 300, 315, size=20)
errorLabel = Group()

cursor = Rect(0, 0, 1, 1, visible=False)
cursor.rotateAngle = -24

inputText = '0'
targetAngle = 0
rotationSpeed = 5

def checkerror(inputText):
    try:
        value = float(inputText)
        if not (-90 <= value <= 90):
            errorLabel.clear()
            errorLabel.add(Label('Value not in boundaries', 300, 350, size=15, fill='red'))
            return False
        else:
            errorLabel.clear()
            errorLabel.add(Label('No Error', 300, 350, size=15, fill='red'))
            return True
    except ValueError:
        return False

def onMousePress(mouseX, mouseY):
    global inputText
    cursor.centerX = mouseX
    cursor.centerY = mouseY

    if inputRect.contains(mouseX, mouseY):
        inputText = ''
        inputLabel.value = inputText

def onKeyPress(key):
    global inputText, targetAngle
    if key == 'backspace':
        inputText = inputText[:-1]
    elif key.isdigit() or key == '-' or key == '.':
        inputText += key
    elif key == 'enter':
        if checkerror(inputLabel.value) == False:
            targetAngle = 0
            inputText = ''
        else:
            try:
                targetAngle = max(-90, min(90, float(inputText)))
            except ValueError:
                pass
            inputText = ''
    inputLabel.value = inputText

def onStep():
    global targetAngle

    if C_leftButton.containsShape(cursor):
        CservoHorn.rotateAngle -= 5
    if C_rightButton.containsShape(cursor):
        CservoHorn.rotateAngle += 5

    currentAngle = SservoHorn.rotateAngle
    if currentAngle < targetAngle:
        SservoHorn.rotateAngle = min(targetAngle, currentAngle + rotationSpeed, 90)
    elif currentAngle > targetAngle:
        SservoHorn.rotateAngle = max(targetAngle, currentAngle - rotationSpeed, -90)

cmu_graphics.run()