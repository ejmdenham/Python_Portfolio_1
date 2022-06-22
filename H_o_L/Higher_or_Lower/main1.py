from game_data import data
from art import logo, vs
import random
from replit import clear


def rand_2_int_generator(list):
    searching = True
    while searching:
        rand_A = random.randrange(len(list))
        rand_B = random.randrange(len(list))
        if rand_A != rand_B:
            return [rand_A, rand_B]
        else:
            rand_2_int_generator(list)


def Game(list, num=0):
    clear()
    print(logo)

    insta = rand_2_int_generator(list)
    num_correct = num
    aFollowers = list[insta[0]]["follower_count"]
    bFollowers = list[insta[1]]["follower_count"]

    print(f'Compare A: {list[insta[0]]["name"]}, a {list[insta[0]]["description"]} from {list[insta[0]]["country"]}.')
    print(vs)
    print(f'Compare B: {list[insta[1]]["name"]}, a {list[insta[1]]["description"]} from {list[insta[0]]["country"]}.')

    if aFollowers > bFollowers:
        most_followers = "A"
    else:
        most_followers = "B"

    guess = str(input("Who do you think has more followers on instagram? Type 'A' or 'B': "))

    if guess.capitalize() == most_followers:
        num_correct += 1
        print(f"Correct! Your current Score is {num_correct}")
        insta.sort()
        list.pop(insta[1])
        list.pop(insta[0])
        Game(list, num_correct)
    else:
        clear()
        print(logo)
        print(f"Sorry... that was incorrect.\nYou lost with a score of {num_correct}")
        replay = input("Would you like to play again? 'Y' or 'N'?")
        if replay.capitalize() == "Y":
            Game(list)
        else:
            pass

Game(data)
