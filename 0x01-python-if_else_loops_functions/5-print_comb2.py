#!/usr/bin/python3

for number in range(0, 128):

    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
