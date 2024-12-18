# Calculator program
import pygame
import os
import time
from sys import exit

os.system('cls')
os.system('color a')
pygame.mixer.init()

pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)

def exit_program():
    input("Press enter to exit program...")
    os.system('cls')
    print("Thank you for using this calculator")
    print("Exiting program...")
    time.sleep(1.5)
    exit()

def go_back():
    while True:
        usrInput = input("Go back to the operator menu? (y/n): ")
        if usrInput == "y":
            os.system('cls')
            break
        if usrInput == "n":
            exit_program()
        else:
            print(f"'{usrInput}' is an invalid entry...")
            time.sleep(1)
            os.system('cls')

def add():
    os.system('cls')
    print("You have selected addition")
    time.sleep(1.5)
    floatOne = float(input("Enter the first number: "))
    floatTwo = float(input("Enter the second number: "))
    total = floatOne + floatTwo

    print(f"{floatOne} + {floatTwo} = {round(total, 4)}")

def sub():
    os.system('cls')
    print("You have selected subtraction")
    time.sleep(1.5)
    floatOne = float(input("Enter the first number: "))
    floatTwo = float(input("Enter the second number: "))
    total = floatOne - floatTwo

    print(f"{floatOne} - {floatTwo} = {round(total, 4)}")

def mul():
    os.system('cls')
    print("You have selected multiplication")
    time.sleep(1.5)
    floatOne = float(input("Enter the first number: "))
    floatTwo = float(input("Enter the second number: "))
    total = floatOne * floatTwo

    print(f"{floatOne} * {floatTwo} = {round(total, 4)}")

def div():
    os.system('cls')
    print("You have selected division")
    time.sleep(1.5)
    floatOne = float(input("Enter the first number: "))
    floatTwo = float(input("Enter the second number: "))
    total = floatOne / floatTwo

    print(f"{floatOne} / {floatTwo} = {round(total, 4)}")

print('Calculator program.')
time.sleep(1)
print("Initializing...")
time.sleep(2)
os.system('cls')

while True:
    operator = input("Select an operator (+ - * /): ")
    if operator == "+":
        add()
        go_back()
    elif operator == "-":
        sub()
        go_back()
    elif operator == "*":
        mul()
        go_back()
    elif operator == "/":
        div()
        go_back()
    else:
        os.system('cls')
        print(f"'{operator}' is an invalid entry...")
        go_back()

