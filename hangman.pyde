word = []
separator = '' 
joined = ''
def setup():
    size(1000,1000)

def draw():
    background(0)
    
def keyTyped():
    global word, joined

    joined = joined + str(key)
    
    
def keyPressed():
    global joined
    if key == ENTER:
        print(joined)
