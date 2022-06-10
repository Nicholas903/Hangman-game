import random

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
selected_word = ''

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
        text(word,650,510)
        fill(255)
        text("Please enter a word",625,430)
        rect(800,850,150,100)
        
    
    elif mode == 3:
        background(255)
    
        deign()
        for x in range(len(selected_word)):
            if selected_word[x] == " ":
                result = result + "  "
            else:
                result = result + "_ "
                
        for y in range(len(selected_word)):
            word_guess.append(" ")
 
        fill(0)
        textSize(60)
        text(result,250,950)
        mode = 4

    elif mode == 5:
        delay(3000)
        background(0)
    elif mode == 6:
        delay(3000)
        background(0)
        
    
    
    
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode
    
    if mode == 4:
        guess = str(key)
        print(guess)
        if guess in selected_word:
            print("Character found")
            for j in range(len(selected_word)):
                if guess == selected_word[j]:
                    word_guess[j] = guess
            background(255)
            correct = " ".join((selected_word) for selected_word in word_guess)
            textSize(55)
            text(str(correct), 250, 945)
            textSize(60)
            text(result,250,950)
            deign()
            space = word.replace("", " ")[1: -1]
            if not(' ' in word_guess):
                open('Words.txt', 'w').close()
                print(word_guess)
                
                mode = 5
                        
        else:
            return
            counter += 1
            print("Character not found")
            print(counter)
            incorrect_guess()
            
            
        return
    

    
    word = word + key
    word = word.strip("\n")
    if key == BACKSPACE and len(word) > 0 and mode == 1:
        word = word[:len(word)-2]
       
def incorrect_guess():
    global mode
    if counter == 1:
        fill(255)
        ellipse(700,250,100,100)
    if counter == 2:
        line(700,300,700,500) 
    if counter == 3:
        line(700,400,800,350) 
    if counter == 4:
        line(600,350,700,400) 

    if counter == 5:
        line(700,500,750,600) 

    if counter == 6:
        line(650,600,700,500) 
        open('Words.txt', 'w').close()

        mode = 6
        

def deign():
    strokeWeight(10)
    line(300,100,700,100)
    line(300,800,300,100)
    line(200,800,400,800)
    line(700,200,700,100) 
    
                                    
def keyPressed(): 
    global mode ,word
    if key == ENTER and mode == 1:
        file = open('Words.txt',"a")
        file.write(word+"\n")
        file.close()
        word = ''
        
        


        

def mousePressed():
    # checks clicks if it is in respective mode/menu
    global mode, selected_word, word_list
   
   
    # retuns to menu
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and mode == 1:
        for word in map(lambda n:n.strip("\n"), open('Words.txt').readlines()):
            if word not in word_list:
                word_list.append(word) 
                
                
        mode = 3 
        selected_word = word_list[random.randint(0,len(word_list)-1)]
        print(selected_word)
