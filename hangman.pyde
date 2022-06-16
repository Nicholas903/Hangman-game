import random
import time

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

# ################################################

def setup():
    size(1000,1000)
    # changes font 
    font = createFont("Bubblegum.ttf", 150)
    textFont(font)
        

def draw():
    global mode, result,guess,space,word_guess,word_list, display,rendered_frame,number,word,incorrect_guessed_letter,correct,time_reset
    background(255)
    
    if mode == 5:
        if time_reset == -1:
            time_reset = time.time()
            
        reset_game()   

        
        
    if mode == 6:
        if time_reset == -1:
            time_reset = time.time()
            
        reset_game() 
    
    
    # when mode is 0 generate the menu screen
    if mode == 0:
        new_game = True
        menu()
        Image = loadImage("43980.png")
        image(Image,600,20)
        
   
   
    # if mode is 2 generate game rules        
    elif mode == 2:
        rules()
        Image2 = loadImage("png.png")
        image(Image2, 200,350)
        
        

    if mode == 1 or mode == 3 or mode == 4:
        design()

        correct_guessed_letter()
        incorrect_guess()

        textSize(60)

        fill(0)
        text(str(correct), 250, 945)
        text(result,250,950)
    
    
    
    # if mode is 1 generate the word input screen 
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
        text("Press to continue",775,830)
        rect(150,850,150,100)
        fill(0)
        text("Back",190,915)



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

    if mode == 4 or mode == 5 or mode == 6:
        textSize(60)
        fill(0)
        text(str(correct), 250, 945)
        text(result,250,950)

        design()
        correct_guessed_letter()
        incorrect_guess()


    
        

   

    
# this function is all of the player typing 
def keyTyped():
    global word,guess,result,space,word_guess,word_list, display,counter,space,mode,word_selected,correct,incorrect_guessed_letter,number
    if mode == 4:
        
        guess = str(key)
        guess = guess.lower()
        if guess in selected_word:
            for j in range(len(selected_word)):
                if guess == selected_word[j]:
                    word_guess[j] = guess
                    incorrect_guessed_letter = False

            correct = " ".join((selected_word) for selected_word in word_guess)
            print(correct)
            textSize(60)
            design()
            word_selected = word_selected.lower()
            space = word_selected.replace("", " ")[1: -1]
            print(space)
            if correct == space:
                open('Words.txt', 'w').close()
                mode = 5
                        
        elif guess not in selected_word:
            counter += 1
            incorrect_guessed_letter = True

        return
            
    if mode == 1:
        word = word + key
        word = word.strip("\n")
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
        print("you won", time.time())
  
# message for when player 2 gesses an incorrect letter and checks # of incorrect guesses and draws a part of the hanging man for each incorrect letter             
def incorrect_guess():
    global mode,guess
    if incorrect_guessed_letter == True:
        textSize(26)
        fill(0)
        text("The letter",150,870)
        text(guess,290,870)
        text("is not in the word",315,870)
    if counter >= 1:
        textSize(26)
        fill(0)
        ellipse(700,250,100,100)
        
    if counter >= 2:
        textSize(26)
        line(700,300,700,500) 
        
    if counter >= 3:
        textSize(26)
        line(700,400,800,350)
        
    if counter >= 4:
        textSize(26)

        line(600,350,700,400)        

    if counter >= 5:
        textSize(26)

        line(700,500,750,600) 
       

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
    rect(250,500,200,100)
    rect(570,500,200,100)
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
    text("2. The other player will attempt to guess the randomly chosen word.", 20, 250)
    text("3. If the other player incorrectly guesses the word more than 6 times, game over.",20, 300)
    rect(750,700,200,100)
    textSize(60)
    fill(0)
    text("BACK", 770,780)        


# game menu design                  
def design():
    strokeWeight(10)
    line(300,100,700,100)
    line(300,800,300,100)
    line(200,800,400,800)
    line(700,200,700,100) 
    

# resets the game values wen game is over and adds a delay before switching to the winner or loser screen
def reset_game():
    global time_reset

    cooldown = 2
    
    if time.time() < time_reset + cooldown:
        return
    
    
    global mode, result,guess,space,word_guess,word_list, display,rendered_frame,number,word,incorrect_guessed_letter,correct,time_reset
    background(0)
    fill(255)
    rect(800,850,150,100)
    word_list = []
    word = ''
    guess = ''
    result = ''
    word_guess = []
    word_selected = ''
    space = ''
    correct = ''
    incorrect_guessed_letter = None
    
    
    
    
# when a key is pressed                                
def keyPressed(): 
    global mode ,word
    if key == ENTER and mode == 1:
        if word in word_list:
            word = ''
            return
        # adds word typed into txt file 
        word_list.append(word)
        file = open('Words.txt',"a")
        file.write(word+"\n")
        file.close()
        word = ''
        
        


        
# if someone clicks mouse            
def mousePressed():
    # checks clicks if it is in respective mode/menu
    global mode, selected_word, word_list,word_selected,word,guess,result,word_guess,counter
   
   
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and mode == 1:
         
        mode = 3 
        selected_word = word_list[random.randint(0,len(word_list)-1)]
        word_selected = selected_word
        selected_word = selected_word.lower()
        print(selected_word)
        
    # when game is over and player two has won or lost return to menu button  
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and (mode == 5 or mode == 6) :
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
   
    # when pressed the first part of the game will begin     
    if mouseX < 450 and mouseX > 250 and mouseY < 600 and mouseY > 500 and mode == 0:
        mode = 1 
     
    # when pressed will bring player to the rules page
    if mouseX < 770 and mouseX > 570 and mouseY < 600 and mouseY > 500 and mode == 0:
        mode = 2
        
    # retuns to menu
    if mouseX < 950 and mouseX > 750 and mouseY < 800 and mouseY > 700 and mode == 2:
        mode = 0
        
    # retuns to menu
    if mouseX < 295 and mouseX > 155 and mouseY < 950 and mouseY > 850 and mode == 1:
        mode = 0
    
