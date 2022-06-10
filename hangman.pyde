word = ''
guess = ''
mode = 1
space = ''
result = ''
word_guess = []
word_list = []
display = ""
counter = 0
correct = ''

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

    elif mode == 5:
        background(0)
    elif mode == 6:
        background(0)
    
    
    
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode
    
    if mode == 4:
        guess = str(key)
        print(guess)
        if guess in word_list:
            print(space)
            print("Character found")
            for j in range(len(word_list)-1):
                if guess == word_list[j]:
                    word_guess[j] = guess
            background(255)
            correct = " ".join((word_list) for word_list in word_guess)
            print(correct)
            text(str(correct), 450, 798)
            text(result,450,800)
            space= word.replace("", " ")[1: -3]
            print(space)
            if correct == space:
                mode = 5
           
                        
        else:
            counter += 1
            print("Character not found")
            print(counter)
            incorrect_guess()
        return
    

    
    word = word + key
    if key == BACKSPACE and len(word) > 0 and mode == 1:
        word = word[:len(word)-2]
       
def incorrect_guess():
    global mode
    if counter == 1:
        print("h")
    if counter == 2:
        print("b")
    if counter == 3:
        print("ra")
    if counter == 4:
        print("la")
    if counter == 5:
        print("rl")
    if counter == 6:
        print("ll")
        mode = 6


                                        
def keyPressed(): 
    global mode 
    if key == ENTER and mode == 1:
        mode = 3
    
