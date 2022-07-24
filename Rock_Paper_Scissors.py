from tkinter import * 
from tkinter import ttk
import random

#initialize score variables
computerScore = 0
playerScore = 0

#function for resetting game/reset scoreboard and score/activate buttons/remove results
def retry_Game():
    global playerScore
    global computerScore
    playerScore = 0
    computerScore = 0
    scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    rock['state'] = 'active'
    paper['state'] = 'active'
    scissors['state'] = 'active'
    computerResult.configure(text = "")
    results.configure(text = "")

#function for continuing current game/reset buttons/remove results
def continue_Game():
    rock['state'] = 'active'
    paper['state'] = 'active'
    scissors['state'] = 'active'
    computerResult.configure(text = "")
    results.configure(text = "")

#function for disabling buttons after weapon choice
def disable_Buttons():
    rock['state'] = 'disable'
    paper['state'] = 'disable'
    scissors['state'] = 'disable'
   
#function for player choice for rock
def rockButton():
    #call the score variables 
    global computerScore
    global playerScore
    #computer choice using random.choice 
    computerChoice = random.choice(['a piece of paper.', 'a rock.', 'a pair of scissors.'])
    #if else statements for the computer's choice
    if computerChoice == 'a piece of paper.':
        computerResult.configure(text = 'a piece of paper.')
        results.configure(text = 'Computer Won...') 
        #add point for computer winning and update the scoreboard label
        computerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    elif computerChoice == 'a rock.':
        computerResult.configure(text = 'a rock.') 
        results.configure(text = 'It is a draw.')   
    else:
        computerResult.configure(text = 'a pair of scissors.') 
        results.configure(text = 'You Won!')
        #add point for player winning and update the scoreboard label
        playerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    #calls function to disable buttons
    disable_Buttons()
    
       
#function for player choice for paper
def paperButton():
    #call the score variables 
    global computerScore
    global playerScore
    #computer choice using random.choice 
    computerChoice = random.choice(['a piece of paper.', 'a rock.', 'a pair of scissors.'])
    #if else statements for the computer's choice
    if computerChoice == 'a piece of paper.':
        computerResult.configure(text = 'a piece of paper.')
        results.configure(text = 'It is a draw.')
    elif computerChoice == 'a rock.':
        computerResult.configure(text = 'a rock.')
        results.configure(text = 'You Won!')
        #add point for player winning and update the scoreboard label
        playerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    else:
        computerResult.configure(text = 'a pair of scissors.')
        results.configure(text = 'Computer Won...')
        #add point for computer winning and update the scoreboard label
        computerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    #calls function to disable buttons
    disable_Buttons()

#function for player choice for scissors
def scissorsButton():
    #call the score variables 
    global computerScore
    global playerScore
    #computer choice using random.choice 
    computerChoice = random.choice(['a piece of paper.', 'a rock.', 'a pair of scissors.'])
    #if else statements for the computer's choice
    if computerChoice == 'a piece of paper.':
        computerResult.configure(text = 'a piece of paper.')
        results.configure(text = 'You Won!')
        #add point for player winning and update the scoreboard label
        playerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    elif computerChoice == 'a rock.':
        computerResult.configure(text = 'a rock.')
        results.configure(text = 'Computer Won...')
        #add point for computer winning and update the scoreboard label
        computerScore += 1
        scoreboard.configure(text = 'Your score:   ' + str(playerScore) + '     Computer score:   ' + str(computerScore))
    else:
        computerResult.configure(text = 'a pair of scissors.')
        results.configure(text = 'It is a draw.')
    #calls function to disable buttons
    disable_Buttons()

#function for rules window
def start_Window():
    #creates instance of second window
    window = Toplevel()
    window.title('Rock! Paper! Scissors!')
    window.geometry("500x230")
    #raises window to the top of all windows
    window.attributes('-topmost', True)
    Label(window, text = 'Rules:').place(x = 235, y = 25)
    Label(window, text = '- Rock Beats Scissors \n - Scissors Beats Paper \n - Paper Beats Rock'). place(x = 175, y = 55)
    #destroys window on button click
    battleButton = Button(window, text = "Battle!", command = lambda: window.destroy(), width = 16).place(x = 185, y = 140)
    
#creates instance of the main window
gameWindow = Tk()
gameWindow.title('Rock! Paper! Scissors!')
gameWindow.geometry("500x270")
#calls the start window function
start_Window()
#raises game window above all windows except start window
gameWindow.lift()


Label(gameWindow, text = 'Choose your weapon!').place(x = 180, y = 10)

#creates buttons/calls appropriate function/sets attributes/seperate placement so that button variable does not come back as "none"
rock = Button(gameWindow, text = 'ROCK', command = rockButton, width = 16)
rock.place(x = 20, y = 50)
paper = Button(gameWindow, text = 'PAPER', command = paperButton, width = 16)
paper.place(x = 185, y = 50)
scissors = Button(gameWindow, text = 'SCISSORS', command = scissorsButton, width = 16)
scissors.place(x = 345, y = 50)

Label(gameWindow, text = 'Computers weapon is... ').place(x = 110, y = 110) 

#creates scoreboard and will be updated through functions using .configure()
scoreboard = Label(gameWindow, text = 'Your score:   ' + str(playerScore) + '       Computer score:   ' + str(computerScore))
scoreboard.place(x = 120, y = 170)

#creates the result labels that will be updated through function
computerResult = Label(text = '')
computerResult.place(x = 265, y = 110)
results= Label(text = '', width = 16)
results.place(x = 185, y = 140)

#creates reset and continue buttons to call the functions to either keep or reset score and activate weapon buttons
resetButton = Button(gameWindow, text = 'Reset Score', command = lambda: retry_Game(), width = 16).place(x = 100, y = 220)
continueButton = Button(gameWindow, text = 'Continue', command = lambda: continue_Game(), width = 16).place(x = 260, y = 220)

#creates window       
gameWindow.mainloop()