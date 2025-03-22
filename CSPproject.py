import cmu_graphics
from cmu_graphics import *

x_offset = ((1200 - 400) / 2) - 50
y_offset = (800 - 400) / 2

Rect(0 + x_offset, 0 + y_offset, 500, 400, fill='white', border='black', borderWidth=4)

Label("How the two main functions of a servo works", 250 + x_offset, -100 + y_offset, size=50, bold=True)

Line(200 + x_offset, 0 + y_offset, 200 + x_offset, 400 + y_offset)
Label("Continuous", 100 + x_offset, 40 + y_offset, size=25)
Label("Continuously rotates left or right", 100 + x_offset, 70 + y_offset, size=12)
Label("Standard", 300 + x_offset, 40 + y_offset, size=25)
Label("Goes to inputted value", 300 + x_offset, 65 + y_offset, size=12)
Label("between -90 and 90", 300 + x_offset, 80 + y_offset, size=12)

Rect(65 + x_offset, 118 + y_offset, 70, 150)
Rect(265 + x_offset, 118 + y_offset, 70, 150)



CservoHorn = Group(
    Arc(100 + x_offset, 140 + y_offset, 23, 100, 270, 180, fill='lightGrey'),
    Circle(100 + x_offset, 120 + y_offset, 3, fill='white'),
    Circle(100 + x_offset, 110 + y_offset, 3, fill='white'),
    Circle(100 + x_offset, 100 + y_offset, 3, fill='white'),
    Arc(100 + x_offset, 140 + y_offset, 23, 100, 90, 180, fill='lightGrey'),
    Circle(100 + x_offset, 160 + y_offset, 3, fill='white'),
    Circle(100 + x_offset, 170 + y_offset, 3, fill='white'),
    Circle(100 + x_offset, 180 + y_offset, 3, fill='white'),
    Circle(100 + x_offset, 140 + y_offset, 13, fill='lightGrey', borderWidth=2, border='white'),
    Circle(100 + x_offset, 140 + y_offset, 5)
)

SservoHorn = Group(
    Arc(300 + x_offset, 140 + y_offset, 23, 100, 270, 180, fill='lightGrey'),
    Circle(300 + x_offset, 120 + y_offset, 3, fill='white'),
    Circle(300 + x_offset, 110 + y_offset, 3, fill='white'),
    Circle(300 + x_offset, 100 + y_offset, 3, fill='white'),
    Arc(300 + x_offset, 140 + y_offset, 23, 100, 90, 180, fill='lightGrey'),
    Circle(300 + x_offset, 160 + y_offset, 3, fill='white'),
    Circle(300 + x_offset, 170 + y_offset, 3, fill='white'),
    Circle(300 + x_offset, 180 + y_offset, 3, fill='white'),
    Circle(300 + x_offset, 140 + y_offset, 13, fill='lightGrey', borderWidth=2, border='white'),
    Circle(300 + x_offset, 140 + y_offset, 5),
)

C_leftButton = Group(
    Rect(20 + x_offset, 310 + y_offset, 77, 55, fill='lime'),
    Label('Left', 59 + x_offset, 337.5 + y_offset, size=20)
)

C_rightButton = Group(
    Rect(103 + x_offset, 310 + y_offset, 77, 55, fill='red'),
    Label('Right', 141 + x_offset, 337.5 + y_offset, size=20)
)

inputs = Label('Input Values', 300 + x_offset, 300 + y_offset, size=20,bold=True)
inputRect = Rect(250 + x_offset, 330 + y_offset, 100, 30, fill='white', border='black')
inputLabel = Label('', 300 + x_offset, 345 + y_offset, size=20)
errorLabel = Group()

cursor = Rect(0, 0, 1, 1, visible=False)
cursor.rotateAngle = -24

inputText = '0'
targetAngle = 0
rotationSpeed = 5

setValueLabel = Label("Set Values", 435 + x_offset, 80 + y_offset, size=20, bold=True)
setValueButtons = []

def getAnglesnum():
    x = False
    while x == False:
        setAngleNum = app.getTextInput('give the number of set angles you want your servo to go to. Must be between 0 and 6')
        if int(setAngleNum) <0 or int(setAngleNum) >6:
            x = False
        else:
            x = True
    return setAngleNum
SET_VALUES = [0]*int(getAnglesnum())
def ButtonMaker():    
    for i in range(len(SET_VALUES)):
        g = False
        while g == False:
            setAngles = app.getTextInput('give one angle you want your servo to go to when you click. MUST BE BETWEEN -90 AND 90!!!!!')
            intsetangles = int(setAngles)
            if intsetangles < -90 or intsetangles > 90:
                g = False
            else:
                SET_VALUES[i] = int(setAngles)
                button = Group(
                    Rect(400 + x_offset, 100 + y_offset + i * 50, 70, 30, fill="lightBlue"),
                    Label(str(SET_VALUES[i]), 435 + x_offset, 115 + y_offset + i * 50, size=15)
                )
                g = True
                setValueButtons.append(button)
ButtonMaker()

def checkerror(inputText):
    try:
        value = float(inputText)
        if not (-90 <= value <= 90):
            errorLabel.clear()
            errorLabel.add(Label('Value not in boundaries', 300 + x_offset, 380 + y_offset, size=15, fill='red'))
            return False
        else:
            errorLabel.clear()
            errorLabel.add(Label('', 300 + x_offset, 380 + y_offset, size=15, fill='red'))
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

    

def onMousePress(mouseX, mouseY):
    global inputText, targetAngle
    cursor.centerX = mouseX
    cursor.centerY = mouseY

    if inputRect.contains(mouseX, mouseY):
        inputText = ''
        inputLabel.value = inputText

    for i, button in enumerate(setValueButtons):
        if button.contains(mouseX, mouseY):
            targetAngle = SET_VALUES[i]
            inputText = str(SET_VALUES[i])
            inputLabel.value = inputText

cmu_graphics.run()