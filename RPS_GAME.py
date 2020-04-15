#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:17:46 2020

@author: skbuddy
"""
import random

list1 = ['rock', 'paper', 'scissor']

print("It's a Rock Paper Scissor against computer")
print("\nWinning Rules of the Game are as follows:\n"
          + "\t Rock vs Paper    -> Paper wins\n"
          + "\t Rock vs Scissor  -> Rock wins\n"
          + "\t Paper vs Scissor -> Scissor wins")

while True:
    
    print("\nUser has three choice:")
    print("1. rock")
    print("2. paper")
    print("3. scissor")

    user_input = input("Your turn : > ")
    
    print("\nUser has choosen : " + user_input)
    user_input = user_input.lower()

    comp_choice = random.choice(list1)
    print("\nComputer Choice is :" + comp_choice + "\n" )
        
    print("\t "+ user_input + "\nVS\n\t"+ comp_choice  +"\n")
    
    if(user_input == comp_choice):
        print("<== It's a Tie ==>")
        
    elif(user_input == 'rock'):
        if(comp_choice == 'scissor'):
            print("<== User Wins ==>")  
        else:
            print("<== Computer Wins ==>")
    
    elif(user_input == 'paper'):
        if(comp_choice == 'rock'):
            print("<== User Wins ==>")
        else:
            print("<== Computer Wins ==>")
    
    elif(user_input == 'scissor'):
        if(comp_choice == 'paper'):
            print("<== User Wins ==>")
        else:
            print("<== Computer Wins ==>")
    
    ans = input("Do you want to play again ?(Y/N) : ")
    
    if(ans == 'n' or ans == 'N'):
        break

print("\nThanks for Playing Rock Paper Scissor Game!!!")
    
    