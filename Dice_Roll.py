import random

def roll():
    print("Your roll is: " + str(random.randint(1, 6)))
    print
    prompt()
    
def prompt():
    x = str.lower(raw_input("Would you like to try again? "))
    if x == "yes":
        roll()
        
    elif x == "no":
        print("Thanks for playing!")
    
    else:
        print("Please enter yes or no.")
        print
        prompt()

x = str.lower(raw_input("Would you like to roll the dice (yes or no)?"))
if x == "yes":
    roll()
    
elif x == "no":
    print("Thanks for playing!")
    print
    
else:
    print("Please enter yes or no.")
    print
    prompt()
