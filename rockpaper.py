import random
exit = False 
while exit == False:
    options = ["Rock" , "Paper", "Scissors"]
    user_input = input("Chose Rock , Paper, Scissors or Exit: " "\n")
    computer_choice = random.choice(options)

    if user_input == "exit":
        print("Game Over")
        exit = True
    #When it's a tie
    elif user_input == "Rock" and computer_choice == "Rock":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("It's a tie :)" , "\n")
    elif user_input == "Paper" and computer_choice == "Paper":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("It's a tie :)" , "\n")
    elif user_input == "Scissors" and computer_choice == "Scissors":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("It's a tie :)", "\n")
    #When computer wins
    elif user_input == "Rock" and computer_choice == "Paper":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print(" Paper covers rock computer wins!" "\n")
    elif user_input == "Paper" and computer_choice == "Scissors":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("Scissors cuts paper computer wins!" "\n")
    elif user_input == "Scissors" and computer_choice == "Rock":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("Rock smaches Scissors computer wins!" "\n")
    #When user wins
    elif user_input == "Rock" and computer_choice == "Scissors":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("Rock smaches Scissors you win!" "\n")
    elif user_input == "Paper" and computer_choice == "Rock":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("Paper covers rock you win!" "\n")
    elif user_input == "Sicissors" and computer_choice == "Paper":
        print("You chose " , user_input , " and computer chose" , computer_choice)
        print("Scissors cuts you win!" "\n")
    else:
        print("invalid choice" , user_input, "\n")
    
    








        

     
