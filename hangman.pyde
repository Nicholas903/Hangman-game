word = ''
guess = ''
mode = 1

result = ''
def setup():
    size(1000,1000)

def draw():
    global mode, result,guess
    if mode == 1:
        background(0)
        
        fill(255)
        rect(600,450,300,100)    
        fill(0)
        textSize(26)
        text(word,650,500)
        fill(255)
        text("Please enter a word",625,430)

    
    elif mode == 3:
        background(255)
        word_list = list(word)
        for x in range(len(word_list)-1):
            if word_list[x] == " ":
                result = result + "  "
            else:
                result = result + "_ "
         
        fill(0)       
        text(result,450,800)
        mode = 4
        
        
    
    
def keyTyped():
    global word,guess
    
    if mode == 4:
        guess = key
        print(guess)
        if str(guess) in word:
            print(word)
            print("Character found")

        else:
            print("Character not found")
        return
    
    word = word + key
    if key == BACKSPACE and len(word) > 0 and mode == 1:
        word = word[:len(word)-2]
       
            
                      
def keyPressed(): 
    global mode 
    if key == ENTER and mode == 1:
        mode = 3
    
