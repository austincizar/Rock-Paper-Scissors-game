import random

name = input("Enter your name: ")
print ("Good Luck ", name)

options = ['Rock', 'Paper', 'scissors']
pc = random.choice(options)

# print instructions 
print ("Game Instructions: \n rock beats scissors \n paper beats rock \n scissors beats paper.")


  
    
 

def game():
    user_option = input("input: \n r for rock: \n p for paper: \n s for scissors: \n x to exit the game: \n ")
    if user_option == "r":
        user_option = "Rock"
    if user_option == "p":
        user_option = "Paper"
    if user_option == "s":
        user_option = "scissors"
        
    if user_option == pc:
        print ("PC selected ", pc, "\n It's a Tie!")
    elif user_option == "Rock" and pc == "Paper":
        print("PC selected: ", pc)
        print ("Paper beats Rock! PC wins!") 
    elif user_option == "Rock" and pc == "scissors":
        print("PC selected: ", pc)
        print ("Rock beats scissors! You win!") 
    
    elif user_option == "Paper" and pc == "Rock":
        print("PC selected: ", pc)
        print ("Paper beats Rock! You win!")   
    elif user_option == "Paper" and pc == "scissors":
        print("PC selected: ", pc)
        print ("scissors beats Paper! PC wins!")   
    elif user_option == "scissors" and pc == "Paper":
        print("PC selected: ", pc)
        print ("scissors beats Paper! you win!")  
    elif user_option == "scissors" and pc == "Rock":
        print("PC selected: ", pc)
        print ("Rock beats scissors! PC wins!")  
    else:
        if user_option == "x":
            print("You've excited the game.")
            return
        print("Wrong input, Try again!")
        game()
game()
