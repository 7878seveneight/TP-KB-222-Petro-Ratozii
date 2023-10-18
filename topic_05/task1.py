import random
import cowsay

cowsay.cow("Hi, let's play Rock-paper-scissors")
option = ["rock", "paper", "scissors"]

while (userChoice := input("(Choose between rock, paper or scissors)\n\t").strip().lower()) not in option:
    print("Invalid choice. Choose between rock, paper or scissors!")
cowChoice = random.choice(option)
cowsay.cow(f"{cowChoice}!!!")
match userChoice, cowChoice:
    case ('rock', 'paper'):
        print("Cow wins!")
        cowsay.cow("I WIN! MOOO!!!")
    case ('rock', 'scissors'):
        print("You win!")
        cowsay.trex("NOOO! How could I lose... I'm filled with anger and now I've become a dinosaur! I WILL EAT YOU")
    case ('rock', 'rock'):
        print("Game is tied.")
        cowsay.cow("Oh... It's tie.")
    case ('paper', 'rock'):
        print("You win!")
        cowsay.trex("NOOO! How could I lose... I'm filled with anger and now I've become a dinosaur! I WILL EAT YOU")
    case ('paper', 'paper'):
        print("Game is tied.")
        cowsay.cow("Oh... It's tie.")
    case ('paper', 'scissors'):
        print("Cow wins!")
        cowsay.cow("I WIN! MOOO!!!")
    case ('scissors', 'rock'):
        print("Cow wins!")
        cowsay.cow("I WIN! MOOO!!!")
    case ('scissors', 'paper'):
        print("You win!")
        cowsay.trex("NOOO! How could I lose... I'm filled with anger and now I've become a dinosaur! I WILL EAT YOU")
    case ('scissors', 'scissors'):
        print("Game is tied.")
        cowsay.cow("Oh... It's tie.")