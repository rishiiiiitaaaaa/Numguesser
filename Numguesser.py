import random
import time 

print ("hii!! welcome to the guessing game . please guess a number beween 1 to 100")
print ("Picking a number ....")
time.sleep(2)
guess = int (input("what is your guess ?:"))
coreect_num=random.randint(1,100)
guess_count=1

while guess != coreect_num:
    guess_count+=1

    if guess<coreect_num:

     guess = int (input(" !Wrong! Need to guess higher :"))
    else :
     guess = int (input(" !Wrong! Need to guess lower :"))
  
print(f"Congrats! the right answer{coreect_num}.It took {guess_count}guesses ") 
