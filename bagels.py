import random

def instructions():
    print("""I am thinking of a 3 digit number. Try to guess what it is.
          Here are some clues: 
          
          What I say:               What that means:
          Pico                      One digit is correct but in the wrong place
          Fermi                     One digit is correct and in the right place
          Bagels                    No digit is correct
          
          Let\'s get started!!
          """)

def game():
    x = random.randint(0,9)
    y = random.randint(0,9)
    z = random.randint(0,9)
    number = str(x) + str(y) + str(z)

    tries = 1
    while tries < 11:
        inpt = input(f"Guess #{tries}: ")
        tries += 1
        if inpt == number:
            print("You got it!")
            won = input("Do you want to play again?")
            if won.upper() == "YES":
                game()
            else:
                break
        else:
            for digits in inpt: 
                if digits in number:
                    if inpt.find(digits) == number.find(digits):
                        print("Fermi.")
                    elif inpt.find(digits) != number.find(digits):
                        print("Pico.")
            else:
                print("Bagels.")
        if tries == 10:
            lost = input("You \'re out of guesses. Do you want to play again?")
            if lost.upper() == "YES":
                game()
            else:
                break
    
instructions()
game()