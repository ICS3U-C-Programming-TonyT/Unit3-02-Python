#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 11, 2023
# This is program that'll allow the user to guess my number.


import constants


def main():
    user_number = int(input("Your guess of my number from (0-9):\n"))
    if user_number < 0 or user_number > 9:
        print("Guess a Valid Number.")
        main()
    elif user_number == constants.number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong")
        main()


if __name__ == "__main__":
    main()
