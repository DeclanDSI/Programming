#!/usr/bin/python3

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    n = 360
    length = (2*3.14*r)/n
    polygon(t, length, n)

def arc(t, r, angle):
    n = 360
    length = (2*3.14*r)/n
    for i in range(angle):
        t.fd(length)
        t.lt(360/n)




bob = turtle.Turtle()
print(bob)

cont = None

while cont != "n":

    print("Print (1:) square or (2:) n-sided polygon or (3:) circle or (4:) arc?")
    opt = input()
    opt = int(opt)

    if opt == 1:
        print("\n\nEnter length: ")
        length = input()
        length = float(length)
        square(bob, length)
    elif opt == 2:
        print("\nEnter number of sides:")
        n = input()
        n = int(n)
        print("\n\nEnter length: ")
        length = input()
        length = float(length)
        polygon(bob, length, n)
    elif opt == 3:
        print("\nEnter radius:")
        r = input()
        r = float(r)
        circle(bob, r)
    elif opt == 4:
        print("\nEnter angle:")
        angle = input()
        angle = int(angle)
        print("\nEnter radius:")
        r = input()
        r = float(r)
        arc(bob, r, angle)
    else:
        print("Did not enter a valid option.")

    print("Continue and move turtle again? \"y\" or \"n\"?")
    cont = input()


