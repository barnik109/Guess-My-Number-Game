import random
print("\t Welcome to 'Guess My Number'!")
print("\n I'm thinking of a number between 1 and 100.\n")
print("Try to guess it in as few attempts as possible")
my_number=random.randint(1,100)
guess=int(input("\nTake a Guess:"))
tries=1
while(my_number!=guess):
    if guess>my_number:
        print("Lower...")
    else:
            print("Higher...")
    guess=int(input("\nTake a Guess:"))
    tries+=1
print("\nYou guessed it! The number was",my_number)
print("And it only took you",tries,"tries!/n")
print("\nPress enter key to exit")
