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
        option = f.readlines()[random.randint(0, len(f.readlines()) - 1 )]

        word_list = list(option)
        for x in range(len(word_list)):
            if word_list[x] == " ":
                result = result + "  "
            else:
                result = result + "_ "
                
        for y in range(len(word_list)):
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
        file = open("Words.txt", "w")
        file.write()
        file.close()
    
    
    
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode
    
    if mode == 4:
        guess = str(key)
        print(guess)
        if guess in word_list:
            print(space)
            print("Character found")
            for j in range(len(word_list)):
                if guess == word_list[j]:
                    word_guess[j] = guess
            background(255)
            correct = " ".join((word_list) for word_list in word_guess)
            print(correct)
            textSize(55)
            text(str(correct), 250, 945)
            textSize(60)
            text(result,250,950)
            deign()
            space= word.replace("", " ")[1: -1]
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
    global mode
   
    # retuns to menu
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and mode == 1:
        mode = 3  
