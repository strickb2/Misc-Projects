#!/usr/bin/env python

import random

print "Type 1 to roll 1 dice and 2 to roll 2 die."
n = raw_input()
list = [1,2,3,4,5,6]
sum = []
roll = random.choice(list)
while True:
    if n == "1":
        print "You have rolled a " + str(roll)
        break
    elif n == "2":
        roll
        sum.append(roll)
        roll
        sum.append(roll)
        print "You have rolled a " + str(sum[0]) + " and a " + str(sum[1])
        print "The total is " + str(sum[0] + sum[1])
        break
    else:
        print "Try again!"
        n = raw_input()
        continue