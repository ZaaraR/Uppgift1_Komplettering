# This is a guess the number game.

import random
from pathlib import Path

def asking_name():
    """[frågar efter ditt namn]

    Returns:
        [str]: [returnerar namnet]
    """
    print("Hello! What is your name?")
    myName = input()
    return myName

    
def game(myName):
    """[ett spel som genererar ett slumpmässigt nummer som spelaren ska gissa sig fram till, spelaren får ledtråd om gissningen är för hög eller för låg]

    Args:
        myName ([str]):

    Returns:
        [int]: [hur många gissningar man gjort]
    """
    guessesTaken = 0
    number = random.randint(1,20)
    print("Well," + myName + ", I am thinking of a number between 1 and 20")
    done=False

    while done==False: 
        print("Take a guess between 1 and 20.")
        guess = input()
        try:
            guess = int(guess)
            guessesTaken = guessesTaken + 1
            if guess < number:
                print("Your guess is too low")

            if guess > number:
                print("Your guess is too high")

            if guess == number:
                break
                done=True

        except ValueError:
            print("Only integers allowed")
  

    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job," + myName + "! You guessed my number in"  + guessesTaken +  "guesses!")

    return guessesTaken


def write_results_to_file(name: str, results: int):
    """[Skriver highscore resultat i txt. filen]

    Args:
        name (str): [lägger till namnet i lsitan]
        results (int): [lägger till hur många gissningar i listan]
    """
    f = open("high_score.txt", "a")
    f.write(f"{name}: Guesses {str(results)}.\n" )
    f.close()


def print_high_score():
    """[öppnar high score lista och sorterar resultat med bäst först]
    """

    f = open("high_score.txt", "r")
    file_contents = f.readlines()
    sorted_scorelist = sorted(file_contents, key = lambda file_contents: file_contents.split()[-1])
    for leader in sorted_scorelist:
        print(leader.strip())





def asking_to_play_again():
    """[Frågar om spelaren vill köra spelet igen eller avsluta]
    """
    choose = input("Would you like to play again?\n")
    if choose.lower() =="yes":
        main()
    elif choose.lower() == "no":
        exit() 

def main():

    name = asking_name()
    results = game(name)
    write_results_to_file(name, results)
    print_high_score()
    asking_to_play_again()

if __name__ == "__main__":
   main()   