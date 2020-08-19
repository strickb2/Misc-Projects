#!/usr/bin/env python

import random

list = ["Rock","Paper","Scissors"]
opp = random.choice(list)
print "Select an option:\n" + "1: Rock\n" + "2. Paper\n" + "3. Scissors"
n = raw_input()
while True:
    if n == "1":
        print "You chose Rock\n" + "Opponent chose " + opp
        if opp == "Rock":
            print "Tie!"
        elif opp == "Paper":
            print "You lose!"
        elif opp == "Scissors":
            print "You win!"
        break
    if n == "2":
        print "You chose Paper\n" + "Opponent chose " + opp
        if opp == "Rock":
            print "You win!"
        elif opp == "Paper":
            print "Tie!"
        elif opp == "Scissors":
            print "You lose!"
        break
    if n == "3":
        print "You chose Scissors\n" + "Opponent chose " + opp
        if opp == "Rock":
            print "You lose!"
        elif opp == "Paper":
            print "You win!"
        elif opp == "Scissors":
            print "Tie!"
        break
    else:
        print "Try again!"
        n = raw_input()
        continue