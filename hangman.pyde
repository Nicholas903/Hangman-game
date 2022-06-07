joined = ''

def setup():
    size(1000,1000)

def draw():
    background(0)
    fill(255)
    rect(600,450,300,100)    
    fill(0)
    textSize(26)
    text(joined,650,500)


    
def keyTyped():
    global joined
    joined = joined + str(key)
    if key == BACKSPACE and len(joined) > 0:
        joined = joined[:len(joined)-2]
                                  
'''def keyPressed():
    if key == ENTER:
        background(255)'''
