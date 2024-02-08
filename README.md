# Slot Machine

This program is a simple slot machine made using the Python programming language along with Pygame.

## Description

The program has been testes with three reels (although it could be modified to work with more). 
The window is set at three symbols by three symbols, but it can be changed to other dimensions.
The slot machine has one payline going through the center of the window. When three of the same symbols show up 
on the payline, the player is rewarded based on the paytable provided. I made a sprite sheet of 15 symbols that can be used.
Reels, weights and a paytable can be entered in slots.py in order to change the slot machine.

## Getting Started

### Dependencies

* Python
* Pygame
* Random
* Sys

### Installing

* You can download the folder in this repository and it should work right off the bat if you have pygame installed.
There are preset reels, weights and a paytable in the program, but all of it can be changed to anything. I am working 
on a program that can create a random set of reels, weights and a paytable with a given expected value that could be used 
with this program (should be finished soon). There is a minimum bet, maximum bet and bet increment set as well that can be changed 
to anything.


### Executing program

* When you run the program, you can see the minumum bet in the top left corner. You can also see your balance in 
the top right corner. When you click on the "up" arrow key, the bet amount will go up by the set bet increment. When 
you click on the "down" arrow key, the bet amount will go down by the set bet increment. When you click on the spin 
button, the reels will randomize and if you get a winning combination, the program will give you the expected payout. 
I have also added the functionality to run the slot multiple times (set at 10,000 spins as default) in order to test 
an expected value.


## Help

If you cannot get the program to work you can always send me a message.