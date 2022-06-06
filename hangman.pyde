word = []
separator = '' 
joined = ('') 
def setup():
    size(1000,1000)

def draw():
    background(0)
    
def keyTyped():
    word.append(key)
    
    joined = separator.join(word)
    print(joined)
def keyPressed():
    global joined
    if key == ENTER:   
        print(joined)
