word = ''
guess = ''
mode = 1
space = ''
result = ''
word_guess = []
word_list = []
display = ""

def setup():
    size(1000,1000)

def draw():
    global mode, result,guess,space,word_guess,word_list, display
    
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
        space = " ".join(word) 
        word_list = list(word)
        for x in range(len(word_list)-1):
            if word_list[x] == " ":
                result = result + "  "
            else:
                result = result + "_ "
                
        for y in range(len(word_list)-1):
            word_guess.append(" ")
 
        fill(0)
        text(result,450,800)
        mode = 4

        
    
    
    
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display
    
    if mode == 4:
        guess = str(key)
        print(guess)
        if guess in word_list:
            print(space)
            print("Character found")
            for j in range(len(word_list)-1):
                if guess == word_list[j]:
                    word_guess[j] = guess
            print(word_guess)
            background(255)
            correct = " ".join((word_list) for word_list in word_guess)

            text(str(correct), 450, 798)
            text(result,450,800)

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
    
