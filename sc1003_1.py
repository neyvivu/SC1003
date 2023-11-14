import random
print("Please select one of the following options: ")
print("    1. Guessing number: ")
print("    2. Calculate sum: ")
choice = int(input())

if choice == 1:
 x = random.randint(1,9)
 print(x)
 guesses_remaining = 3
 count = 0
 guess = 0 

 while  guesses_remaining > 0:

    while True:
        try:
            guess = int(input("Enter a number between 1 and 9: "))
            if (1 <= guess and guess <= 9):
                break     
            else:
                print("Your guess was NOT a number between 1 and 9.  Try again.")
        except:
            print("Your guess was NOT an Integer.  Try again.")

    guesses_remaining -= 1
    count = count + 1
    print(guess)

    if guess == x:
        print ("Congratulations. You guessed it by ", count," trial! ")
        guesses_remaining = 0    
        break
    elif guess < x:
        print ("guess is low")
    elif guess > x:
        print ("guess is high")

    if guesses_remaining == 0:
        print ("\nSorry, you exceed the trial limit. Failed. The winning number was:",x, "\n\nBetter luck next time!")

elif choice == 2:
    start_num = random.randint(55,66)
    sum = 0
    print("Please calculate the sum of 5 integers start from", start_num)
    for i in range(start_num, start_num +5):
       sum = sum + i 

    print(sum)
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
    else:
        print("Sorry, wrong answer. Failed.")

else: 
    print("Wrong answer. Bye.")


