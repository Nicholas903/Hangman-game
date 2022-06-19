# global variables

add_library('minim')    # add minim audio library

import random # adds random number
import time # returns the elapsed time 

word = ''
guess = ''
mode = 0
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
time_reset = -1
select = False
colour = 0
word_is_in_list = False

# ################################################

def setup():
    global frame,win_sound, lose_sound, correct_sound, incorrect_sound 
    size(1000,1000)
    # changes font 
    font = createFont("Bubblegum.ttf", 150)
    textFont(font)
    frameRate(20)
    minim = Minim(this)
    
    win_sound = minim.loadFile("win_sound.mp3")
    lose_sound = minim.loadFile("lose_sound.mp3")
    correct_sound = minim.loadFile("correct_sound.mp3")
    incorrect_sound = minim.loadFile("incorrect_sound.mp3")

frame, max_frame = 1, 77
        
frame2, max_frame2 = 1, 14    

def draw():
    global mode, result,guess,space,word_guess,word_list, display,rendered_frame,number,word,incorrect_guessed_letter,correct,time_reset,select,colour,frame, frame2,word_is_in_list

    background(255)
    
    
    
    # when mode is 0 generate the menu screen
    if mode == 0:
        new_game = True
        menu()
        Image = loadImage("43980.png")
        image(Image,600,20)
        win_sound.pause()
        lose_sound.pause()
        win_sound.rewind()
        lose_sound.rewind()

    # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
    if mouseX < 770 and mouseX > 570 and mouseY < 600 and mouseY > 500 and mode == 0:
        fill(255,200)
        rect(570,500,200,100,10)
        
    # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
    if mouseX < 450 and mouseX > 250 and mouseY < 600 and mouseY > 500 and mode == 0:
        fill(255,200)
        rect(250,500,200,100,10)

   
   
    # if mode is 2 generate game rules        
    elif mode == 2:
        rules()
        Image2 = loadImage("png.png")
        image(Image2, 200,350)
        
        # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
        if mouseX < 950 and mouseX > 750 and mouseY < 800 and mouseY > 700 and mode == 2:
            fill(255,200)
            rect(750,700,200,100,10)

        

    
    
    
    
    # if mode is 1 generate the word input screen 
    if mode == 1:
        background(0)

        fill(255)
        stroke(0,0,colour)
        rect(350,450,300,100,10)    
        fill(0)
        textSize(26)
        text(word,400,510)
        fill(255)
        text("Please enter a word",370,430)
        text("Hit enter to type in another word",270,590)

        stroke(0)
        rect(700,850,150,100,10)
        stroke(0)
        rect(150,850,150,100,10)
        fill(0)
        text("Back",190,915)
        text("start",735,895)
        text("game",735,925)

        # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
        if mouseX < 295 and mouseX > 155 and mouseY < 950 and mouseY > 850 and mode == 1:
            fill(255,200)
            rect(150,850,150,100,10)
            
        # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
        if mouseX < 845 and mouseX > 705 and mouseY < 950 and mouseY > 850 and mode == 1:
            fill(255,200)
            rect(700,850,150,100,10)


    # if mode is 3 count the number of letters are in the word ad converts them into blank spaces
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


    # draws game
    if mode == 4 or mode == 5 or mode == 6:
        textSize(60)
        fill(0)
        text(str(correct), 250, 945)
        text(result,250,950)

        design()
        correct_guessed_letter()
        incorrect_guess()
        
    # when mode is 5 print player congradulations when mode is 6 print sympathetic message
    if (mode == 5 or mode == 6):
        if time_reset == -1:
            time_reset = time.time()
            
        reset_game() 

    
# this function is all of the player typing 
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode,word_selected,correct,incorrect_guessed_letter,number
    if mode == 4:
        
        guess = str(key)
        guess = guess.lower()
        
        # this checks if the guess is in the word
        if guess in selected_word:
            for j in range(len(selected_word)):
                if guess == selected_word[j]:
                    word_guess[j] = guess
                    incorrect_guessed_letter = False
                    correct_sound.play()
                    correct_sound.rewind()
                    
            # if the user has guessed a correct letter add it to the list of correct guesses
            correct = " ".join((selected_word) for selected_word in word_guess)
            textSize(60)
            design()
            word_selected = word_selected.lower()
            space = word_selected.replace("", " ")[1: -1]
            
            # compares the list of words that the player has guessed to the selected word 
            if correct == space:
                open('Words.txt', 'w').close()
                mode = 5
         
        # if guess is not in the word add one to the counter and incorrect_guess becomes true and play sound                                
        elif guess not in selected_word:
            counter += 1
            incorrect_guessed_letter = True
            incorrect_sound.play()
            incorrect_sound.rewind()

        return
    
    # if mode is 1 and user has clicked on the box allow user to type                                 
    if mode == 1 and select == True:
        word = word + key
        word = word.strip("\n")
        # if user makes a mistake they can backspace and correct it. 
        if key == BACKSPACE and len(word) > 0 and mode == 1:
            word = word[:len(word)-2]

# message for when player 2 gesses a correct letter  
def correct_guessed_letter():
    if incorrect_guessed_letter == False:
        textSize(26)
        fill(0)
        text("The letter",150,870)
        text(guess,290,870)
        text("is in the word",310,870)
  
# message for when player 2 gesses an incorrect letter and checks # of incorrect guesses and draws a part of the hanging man for each incorrect letter             
def incorrect_guess():
    global mode,guess,incorrect_sound 
    if incorrect_guessed_letter == True:
        textSize(26)
        fill(0)
        text("The letter",150,870)
        text(guess,290,870)
        text("is not in the word",315,870)

    # prints head 
    if counter >= 1:
        textSize(26)
        fill(0)
        ellipse(700,250,100,100)
        
    # prints body 
    if counter >= 2:
        textSize(26)
        line(700,300,700,500)
         
    # prints right arm
    if counter >= 3:
        textSize(26)
        line(700,400,800,350)
        
    # prints left arm
    if counter >= 4:
        textSize(26)
        line(600,350,700,400)        

    # prints right leg
    if counter >= 5:
        textSize(26)
        line(700,500,750,600) 
       
    # prints left leg and switches to losing screen
    if counter >= 6:
        textSize(26)
        line(650,600,700,500) 
        open('Words.txt', 'w').close()
        
        mode = 6

# main menu design                  
def menu():
    strokeWeight(10)

    background(255)
    textSize(120)
    fill(0)
    text("HANGMAN",50,250)
    fill(255)
    rect(250,500,200,100,10)
    rect(570,500,200,100,10)
    textSize(60)
    fill(0)
    text("PLAY", 280,570)
    textSize(60)
    fill(0)
    text("RULES", 590,570)

# rules menu design                  
def rules():

    background(0)
    fill(0)
    textSize(120)
    fill(255)
    text("RULES", 350, 150)
    textSize(20)
    text("1. The host is randomly chosen among the 2 players. If you are the host, create a list of words.", 20,200)
    text("2. The other player will attempt to guess the word that is randomly chosen by the computer.", 20, 250)
    text("3. If the player incorrectly guesses 6 letters that are not in the word, the game is over.",20, 300)
    rect(750,700,200,100,10)
    textSize(60)
    fill(0)
    text("BACK", 775,780)        


# game menu design                  
def design():
    strokeWeight(10)
    line(300,100,700,100)
    line(300,800,300,100)
    line(200,800,400,800)
    line(700,200,700,100) 
    

# resets the game values when game is over and adds a delay before switching to the winner or loser screen
def reset_game():
    global time_reset

    cooldown = 2
    
    if time.time() < time_reset + cooldown:

        return
    
    global mode, result,guess,space,word_guess,word_list, display,rendered_frame,number,word,incorrect_guessed_letter,correct,time_reset,frame, frame2,win_sound, lose_sound, correct_sound, incorrect_sound 
    background(0)
    fill(255)
    rect(800,850,150,100,10)
    fill(0)
    textSize(26)
    text("Back",840,915)
    word_list = []
    word = ''
    guess = ''
    result = ''
    word_guess = []
    word_selected = ''
    space = ''
    correct = ''
    incorrect_guessed_letter = None
    
    if mode == 5:
        # plays winner sound 
        win_sound.play()
        
        frame += 1
        if frame >= max_frame:
            # adds animation to win screen 
            frame = 1
        print("(" + str(frame) + ")")
        image(loadImage("winning/(" + str (frame) + ").gif"), 245,200,500,300)
        textSize(50)
        fill(255)
        text("Congratulatios you guessed the word",10,600) 
        text("YOU WON!", 375, 650)
          
        # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
        if mouseX < 950 and mouseX > 800 and mouseY < 950 and mouseY > 850 and (mode == 5 or mode == 6):
            fill(255,200)
            rect(800,850,150,100,10)
            
        
    else:
        
        # plays loser sound 
        lose_sound.play() 
        
        # adds animation to lose screen 
        frame2 += 1
        if frame2 >= max_frame2:
            frame2 = 1
        print("(" + str(frame2) + ")")
        image(loadImage("losing/(" + str (frame2) + ").gif"), 245,200,500,300)
        textSize(50)
        fill(255)
        text("That is unfortunate",230,600)
        text("You did not guess the word",150,650)
        text("YOU LOST!", 375, 700)
        
        # if the mouse curser goes over this box add a transparent square over box to show that the user can select it 
        if mouseX < 950 and mouseX > 800 and mouseY < 950 and mouseY > 850 and (mode == 5 or mode == 6):
            fill(255,200)
            rect(800,850,150,100,10)
    
    
# when a key is pressed                                
def keyPressed(): 
    global mode ,word,word_is_in_list
    
    # when user has seleced the text box in mode 1 they want to add a word to the list they can press enter
    if key == ENTER and mode == 1 and select == True:
        if word in word_list:
            word = ''
            return
        # adds word typed into txt file 
        word_list.append(word)
        file = open('Words.txt',"a")
        file.write(word+"\n")
        file.close()
        word = ''
        word_is_in_list = True

    

        
# if someone clicks mouse            
def mousePressed():
    # checks clicks if it is in respective mode/menu
    global mode, selected_word, word_list,word_selected,word,guess,result,word_guess,counter, time_reset,select,colour,word_is_in_list

    # when button is pressed to start one of the words that were added will be randomly selected 
    if mouseX < 845 and mouseX > 705 and mouseY < 950 and mouseY > 850 and mode == 1 and word_is_in_list == True:
        mode = 3 
        selected_word = word_list[random.randint(0,len(word_list)-1)]
        word_selected = selected_word
        selected_word = selected_word.lower()
        
        
    # when game is over and player two has won or lost return to menu button  
    if mouseX < 950 and mouseX > 800 and mouseY < 950 and mouseY > 850 and (mode == 5 or mode == 6) :
        mode = 0
        word_list = []
        word = ''
        guess = ''
        result = ''
        word_guess = []
        word_selected = ''
        space = ''
        counter = 0
        incorrect_guessed_letter = None
        time_reset = -1
        word_is_in_list = False

   
    # when pressed the first part of the game will begin 
    if mouseX < 450 and mouseX > 250 and mouseY < 600 and mouseY > 500 and mode == 0:
        colour = 0
        mode = 1 
        return
     
    # when pressed will bring player to the rules page
    if mouseX < 770 and mouseX > 570 and mouseY < 600 and mouseY > 500 and mode == 0:
        mode = 2
        return

    # retuns to menu
    if mouseX < 950 and mouseX > 750 and mouseY < 800 and mouseY > 700 and mode == 2:
        mode = 0
        return

    # retuns to menu
    if mouseX < 295 and mouseX > 155 and mouseY < 950 and mouseY > 850 and mode == 1:
        open('Words.txt', 'w').close()
        word_is_in_list = False
        word_list = []
        mode = 0
        return

    # when clicked allows the player to enter in words
    if mouseX < 645 and mouseX > 345 and mouseY < 545 and mouseY > 455 and mode == 1:
        select = True
        colour = 255
        
    else:
        select = False
        colour = 0

        
    
