from random import randint

print("System activation.........")


def starts():
    while True:
        answer = input("Do you want to play 'Number Guessing Game'? ")

        if answer.lower() in ["yes", "i want to", "exactly", "sure", "maybe", "yeah"]:
            print("Let's start!\n")
            return game()
        
        elif answer.lower() in ["no", "nope", "not at all", "never", "nono"]:
            print("We will definitely play next time!\n")
            break

        else:
            print("Unfortunately, your request could not be processed. You might have made a mistake. Please enter the text correctly!\n")
            

def game():
    while True:
        try_count = 1
        number = randint(1, 100)
        print("The program has thought of an integer from 1 to 100, inclusive.", "Try to guess it!", sep="\n")

        while True:
            info = input()
            
            if not info.isdigit():

                if info.lower() in ["idk", "idontknow", "i dont know", "i don't know"]:
                    print("I beat you this time!", f"The secret number is: {number}")
                    break

                else:
                    print("You might have made a mistake. Please enter the answer correctly without symbols!")
                    print("Try again!")

            elif info.isdigit():
                info = int(info)

                if info == number:
                    print("You guessed the answer correctly!", f"It took you {try_count} shots to get it.", sep="\n")
                    break
                elif info > 100:
                    print("Value exceeds 100! This is impossible.")
                else:
                    print("Your guess is incorrect!")

                    if max(info, number) - min(info, number) <= 10:
                        print("This time your answer was close to the secret number!")
                    else:
                        print("This time your answer is far from the secret number!")
                    
                    if info > number:
                        print("Your number is too high.")
                    else:
                        print("Your number is too low.")
                        
                try_count += 1

                        
        if (input("Type 'yes' if you want to restart the round or start a new game: ")).lower().strip() in  ["yes", "i want to", "exactly", "sure", "maybe", "yeah"]:
            continue
        else:
            print("It was a pleasure playing with you!", "See you next time!\n", sep="\n")
            break
        

starts()