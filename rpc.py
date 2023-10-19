import random


def main():
    valid = ["rock", "paper", "scissors"]
    user_score = 0
    bot_score = 0
    round = 0

    print("To end the game tape: exit")
    print("""        ------------------------------------------------------------------------
                    Welcome to Rock 🗿 Paper 📄 Scissors ✂ !
                            To end the game tape: exit
                                    Let's Go!!!
        ------------------------------------------------------------------------""")

    while True:
        print(f"                ---------------------Round #{round}---------------------")
        # take user input
        user = input("Your Turn! : ").lower()

        # check if end the program
        if user == "exit":
            break
        # check if user input is valid if not repromt the user for input until it's valid
        if user not in valid:
            print("Invalid input... \nValid: [rock/paper/scissors/exit]")
            continue

        round += 1

        bot = random.choice(valid)

        result = checker(user, bot)
        if result == True:
            print("                                 U won the round!")
            user_score += 1
        elif result == False:
            print("                                U lost the round...")
            bot_score += 1

        print(f"                            Scores: Yours: {user_score} | Bot: {bot_score}")


def checker(user, bot):
    if user == bot:
        print("                                no one wins this.")
    else:
        if user == "rock" and bot == "scissors":
            return True
        elif user == "paper" and bot == "rock":
            return True
        elif user == "scissors" and bot == "paper":
            return True
        else:
            return False


main()
