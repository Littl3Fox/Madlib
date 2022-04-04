# For this project i use concatenation of strings to replicate the game 
# A few ways to do this 

# programing_language="Python"

# print("I'm practicing "+programing_language) 
# print("I'm practicing {}".format(programing_language))
# print(f"I'm practicing {programing_language}")



while True:
    try:
        verb = input(str("A verb: "))
        adjective = input(str("A adjective: "))
    except:
        print("You did something wrong!! Try again!")
        break
    else:
        madlibs=f"Today was a {adjective} day to {verb}!\
 Today is a awesome day"

        print(madlibs)

        again = input(str("Would you like to play again S/N?:"))
        if(again != "S"):
            break