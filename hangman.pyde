import random
import time

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
word_selected = ''
incorrect_guessed_letter = None
rendered_frame = False


def setup():
    size(1000,1000)

def draw():
    global mode, result,guess,space,word_guess,word_list, display,rendered_frame
    background(255)
    
    if mode == 1 or mode == 2 or mode == 3 or mode == 4:
        deign()
        incorrect_guess()
        correct_guessed_letter()
        textSize(60)

        fill(0)
        text(str(correct), 250, 945)
        text(result,250,950)

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

    if mode == 4 or mode == 5 or mode == 6:
        textSize(60)
        fill(0)
        text(str(correct), 250, 945)
        text(result,250,950)

        deign()
        incorrect_guess()
        correct_guessed_letter()


    if mode == 5:
        if rendered_frame == True:
            
            delay(3000)
            background(0)
        else:
            rendered_frame = True
        
    if mode == 6:
        delay(3000)
        background(0)
        
   

    
    
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode,word_selected,correct,incorrect_guessed_letter
    if mode == 4:
        
        guess = str(key)
        if guess in selected_word:
            for j in range(len(selected_word)):
                if guess == selected_word[j]:
                    word_guess[j] = guess
                    incorrect_guessed_letter = False


            correct = " ".join((selected_word) for selected_word in word_guess)
            textSize(60)
            deign()
            print(word_guess)

            space = word_selected.replace("", " ")[1: -1]
            if correct == space:
                open('Words.txt', 'w').close()
                mode = 5
                        
        elif guess not in selected_word:
            counter += 1
            print(guess)
            print(counter)
            incorrect_guessed_letter = True
            incorrect_guess()
        return
            

    word = word + key
    word = word.strip("\n")
    if key == BACKSPACE and len(word) > 0 and mode == 1:
        word = word[:len(word)-2]

def correct_guessed_letter():
    if incorrect_guessed_letter == False:
        textSize(26)
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is in the word",310,870)
        
def incorrect_guess():
    global mode,guess
    if counter >= 1:
        textSize(26)
        fill(255)
        ellipse(700,250,100,100)
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True
    if counter >= 2:
        textSize(26)
        line(700,300,700,500) 
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True
    if counter >= 3:
        textSize(26)
        line(700,400,800,350)
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True
    if counter >= 4:
        textSize(26)

        line(600,350,700,400) 
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True

    if counter >= 5:
        textSize(26)

        line(700,500,750,600) 
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True

    if counter >= 6:
        textSize(26)

        line(650,600,700,500) 
        open('Words.txt', 'w').close()
        fill(0)
        text("The letter",150,870)
        text(guess,280,870)
        text("is not in the word",310,870)
        incorrect_guessed_letter == True

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
    global mode, selected_word, word_list,word_selected
   
   
    # retuns to menu
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and mode == 1:
        for word in map(lambda n:n.strip("\n"), open('Words.txt').readlines()):
            if word not in word_list:
                word_list.append(word) 
                
                
        mode = 3 
        selected_word = word_list[random.randint(0,len(word_list)-1)]
        word_selected = selected_word
