import random
import sys

l=list(range(0,21))
x=random.choice(l)
#print("Our Choice: {}\n\n".format(x))
print("\t:::  Welcome To 'Guess The Number'  :::\n\n")
print("Instructions:\n")
print("1. You have to guess a number between 0 to 20 where both are included")
print("2. If the number you have guessed matches the number we generated, then the game will end ")
print("3. If your guess is wrong!!! then don't worry, you have a total of 5 lives and we also give you some hints")
print("So Let's Get Started!!!\n")

life=5
score=100
while(life!=0):
    print("Your Chance Remaining: {}".format(life))
    n=int(input("Enter a number between 0 and 20 where both are included: "))
    life-=1
    if(n==x):
        print("Congratulations!!! Your number matches to our number")
        print("Your Score: {}".format(score) )
        sys.exit(0)
    elif(x-n<=5 and x-n>=0):
        print("HINTS: Oops!!! you are too close but your number is smaller than our number... Let try it again!!!")
    elif(n-x<=5 and n-x>=0):
        print("HINTS: Oops!!! you are too close but your number is bigger than our number... Let try it again!!!")
    elif(x-n>5 and x-n<=20):
        print("HINTS: Sorry!!! you guess it too low")
    else:
        print("HINTS: Sorry!!! you guess it too high")
    score=score-20
    print("\n")
print("Sorry!!! better luck next time!!!")
print("Our number was: {}".format(x))
print("Your score: 0")
