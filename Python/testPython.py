#!/bin/python3

def print_slashes():
    print("/         /         /")
    print("/         /         /")
    print("/         /         /")
    print("/         /         /")
 

def print_halfSquare():
    
    print("+ - - - - + - - - - +")
    print_slashes()


def print_square():
    print_halfSquare()
    print_halfSquare()
    print("+ - - - - + - - - - +")

print_square()
