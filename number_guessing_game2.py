#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: September 2019
# This lets the user guess a number

import random


def main():
    # random number
    number = random.randint(0, 9)

    # input
    guess = int(input("pick a number between 0 and 9: "))

    # process
    if guess == number:
        # output
        print()
        print("Correct, my number was", number)

    # process
    else:
        # output
        print()
        print("Incorrect, try again?")
        print("The correct number was", number)


if __name__ == "__main__":
    main()
