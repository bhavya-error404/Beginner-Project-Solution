import random
print("""Welcome to the Guessing Game!!!
We have guessed a number from 1 to 100,
you have guess a number and accordingly
a message will be printed that is
whether your choice is higher or lower.

""")
num = 0
ch = input("Want to play? y/n :")
while(ch=='y'):
    x = random.randrange(1,100,1)
    n = -1
    while(n != x):
        n = int(input("\nEnter your guess: "))
        num += 1
        if n>x:
            print("Your guess is higher")
        elif n<x:
            print("Your guess is lower")
        else:
            print("\nCongratulations ! You have guessed the right number.")
            break
    if num==1:
        print("\nYou have taken one guess to hit the right number")
    else:
        print("\nYou have taken {} guesses to hit the right number".format(num))
    ch = input("\nWant to play again? y/n :")
print("You have exited the game.")
    
    

