import re
import random

user_info = {'Test': 'Test12345', 
             'Jack': 'Test12345', 
             'Tom': 'Password1', 
             'tt': 'Tgh46302H'}

def is_valid_password(password):
    return (
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        len(password) > 8
    )

def getUserName():
    while True:
        username = input("Input your user name: ")
        if username in user_info:
            print("The user exists. Please choose another user name.")
        else:
            return username

def getPassword():
    while True:
        password = input("Input your password:\n"
                         " 1. The password has at least one upper case letter\n"
                         " 2. The password has at least one lower case letter\n"
                         " 3. The password has at least one digit\n"
                         " 4. Its length is more than 8\n")

        if is_valid_password(password):
            return password
        else:
            print("Your password is weak. Please enter a new password")

def register_user(username, password):
    user_info[username] = password
    print("New User registered. You can start the game.")

def user_login():
    while True:
        username = input("Input user name: ")
        password = input("Input password: ")

        if username in user_info and user_info[username] == password:
            print(f"Welcome back, {username}, You can start the game.")
            break
        else:
            print("Invalid username or password. Please try again.")

def play_as_guest():
    print("Dear Guest, you have to pass one quiz to play the game.")
    flag = 0
    while True:
        print("Please select one of the following quizzes:")
        print(" 1. Number guessing")
        print(" 2. Calculate sum")
        quiz_choice = input()
        
        if quiz_choice == '1':
            flag = play_number_guessing_game()
            break
        elif quiz_choice == '2':
            flag = play_calculate_sum_game()
            break
        else:
            print("Invalid option. Please choose a valid quiz.")
        if flag == 1: 
            print("Congrats")

def play_number_guessing_game():

    number_to_guess = random.randint(1, 9)
    trials = 0
    guesses_remaining = 3
    correct = 0
    print(number_to_guess)
    
    while  guesses_remaining > 0:

        while True:
            try:
                guess = int(input("Enter an integer between 1 and 9: "))
                if (1 <= guess and guess <= 9):
                    break     
                else:
                    print("Your guess was NOT a number between 1 and 9.  Try again.")
            except:
                print("Your guess was NOT an Integer.  Try again.")

        guesses_remaining -= 1
        trials = trials + 1
            
        if guess == number_to_guess:
            print("Congratulations. You guessed it by ", trials," trial! ")
            guesses_remaining = 0  
            correct = 1  
            break
        elif guess < number_to_guess:
            print ("guess is low")
        elif guess > number_to_guess:
            print ("guess is high")

    if guesses_remaining == 0 and correct == 0:
            print ("\nSorry, you exceed the trial limit. Failed. The winning number was:",number_to_guess, "\nBetter luck next time!")
            return 0
    return 1

def play_calculate_sum_game():
    

    start_num = random.randint(55,66)
    sum = 0
    print("Please calculate the sum of 5 integers start from", start_num)
    for i in range(start_num, start_num +5):
       sum = sum + i 

    ans = 0 
    while True:
        try:
            ans = int(input("Please enter the answer: "))
        except: 
            print("Wrong input. Please try again.")
        else:
            break 
    print(sum)
    if (ans == sum):
        print("Correct answer.")
        return 1
    else:
        print("Sorry, wrong answer. Failed.")
        return 0

while True:
    print("Please select one of the following options:")
    print(" 1. User registration")
    print(" 2. User Login")
    print(" 3. Play the game as a guest")
    choice = input()

    if choice == '1':
        register_user(getUserName(), getPassword())
    elif choice == '2':
        user_login()
    elif choice == '3':
        play_as_guest()
    else:
        print("Invalid option. Please choose a valid option.")
