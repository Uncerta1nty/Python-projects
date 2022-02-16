def wordToDash(unknownw):

    nlet=""

    for i in range(len(unknownw)):

        letter=unknownw[i]

        if letter>="a" and letter<="z" or letter>="A" and letter<="Z":

            nlet+="_ "

        else:

            nlet+=letter+" "

    return nlet


def validate():

    guess=input("Enter a letter: ")

    while not(guess>="a" and guess<="z" or guess>="A" and guess<="Z") or len(guess)!=1:

        print ("Not a valid character. Please enter a letter.")

        guess=input("Enter a letter: ")

    return guess


def checkUsed(uls, guess):

    if guess in uls:

        return  False

    else:

        return  True

    

        

        

def replaceDash(guess, unknownw, secretDash):

    for i in range (len(unknownw)):

        if unknownw[i]==guess:

            secretDash=secretDash[0:i*2]+guess+secretDash[i*2+1:]

        

    return secretDash

       


def output(guessed, finalAnswer):

    if guessed==finalAnswer:

        return True

    else:
        
        return False















def main():


    print("Hangman is a popular word game. In this game, you are given some number of blanks representing a secret phrase. You have  to guess the name using at most 6 number of tries.")

    unknownw=input("Enter your secret phase: ")
    for i in range(100):
        print("")

    lines=wordToDash(unknownw)

    print(lines)

    tries=6

    uls=""

    guessed=""

    finalAnswer=unknownw

    while tries>0 and lines!=unknownw:

        guess=validate()

        letterUsed=checkUsed(uls, guess)

        if letterUsed==False :

            print("You've already used this letter, enter another letter")

        elif letterUsed==True:

            uls+=guess

            if guess in unknownw:

                lines=replaceDash(guess, unknownw, lines)

                print("You have",tries,"tries left.")

                print(lines)

            elif guess.upper() in unknownw:

                guess=guess.upper()

                lines=replaceDash(guess, unknownw, lines)

                print("You have",tries,"tries left.")

                print(lines) 

            elif guess not in unknownw:

                print("This letter is not in the secret phrase")

                tries=tries - 1

                print("You have",tries,"tries left.")

                print(lines)

            elif output(guessed,finalAnswer)== True:
                print("Congrats, you won!!! The secret phrase was", finalAnswer)

            elif output(guessed,finalAnswer)== False:
                
                print(":( The secret phrase was", finalAnswer)

                

            

    

main()
