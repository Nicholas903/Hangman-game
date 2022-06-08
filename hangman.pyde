joined = ''
mode = 1
result = ''
def setup():
    size(1000,1000)

def draw():
    global mode, result
    if mode == 1:
        background(0)
        fill(255)
        rect(600,450,300,100)    
        fill(0)
        textSize(26)
        text(joined,650,500)
    
    elif mode == 3:
        background(255)
        joined_list = list(joined)
        for x in range(len(joined_list)-1):
            if joined_list[x] == " ":
                result = result + "  "
            else:
                result = result + "_ "
            
            
        print(result)
        mode = 0
        
        
    
    
def keyTyped():
    global joined
    joined = joined + str(key)
    if key == BACKSPACE and len(joined) > 0:
        joined = joined[:len(joined)-2]
                                  
def keyPressed(): 
    global mode 
    if key == ENTER:
        mode = 3
