from art import logo, vs
from game_data import data
import random
from replit import clear

def choice():
    """Get the choices from the data and assign choices for user and computer"""
    choice_A = random.choice(data)
    choice_B = random.choice(data)
    if choice_A == choice_B:
        choice_B = random.choice(data)
    print(f"Compare A: {choice_A['name']}, {choice_A['description']} from {choice_A['country']}")
    print(vs)
    print(f"Against B: {choice_B['name']}, {choice_B['description']} from {choice_B['country']}")
    user_choice = input("Who has more followers : Type 'A' or 'B' >>>")
    if user_choice.upper() == 'A':
        user_choice = choice_A
        other_choice = choice_B
    else:
        user_choice = choice_B
        other_choice = choice_A 
    return user_choice, other_choice  

def play_game():
    print(logo)
    is_continue = True
    count = 0
    while is_continue:
        user_choice , other_choice = choice()
        if user_choice["follower_count"] >= other_choice["follower_count"]:
            count += 1
            print(f"You are right. Your current score is {count}")
            is_continue = True
        else:
            print("You lost")
            print(f"Your choice {user_choice['name']} has {user_choice['follower_count']}")
            print(f"Other choice {other_choice['name']} has {other_choice['follower_count']}")
            print(f"The number of True Answers is : {count}")
            if input("Do you want to play again : Type 'y' or 'n' >>>").lower() == "n":
                is_continue = False
            else:
                play_game()

if __name__ == "__main__":
    clear()
    play_game()

        

    


