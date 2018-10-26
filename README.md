# Squill

Squill is a game where you write a program to control troops and battle your friend! 

Status: Works locally and looks less ugly than it did before but still lots of work to do before actually playable....

## Docs

You will code a JavaScript strategy file with one function called 'turn'. It will have the following signature: 

**turn(color, matrix, strength, x, y)**


Your function should return **heal()**, **attack(DIRECTION, NUMBER_OF_TROOPS)**, or **move(DIRECTION, NUMBER_OF_TROOPS)**


DIRECTION must be "U" "D" "L" or "R", for up/down/left/right.
NUMBER_OF_TROOPS should be an integer, indicating the number of troops you would like to move. You cannot move all your troops. It costs one troop to attack and you must have at least one troop protecting your territory. Therefore, you must have at least three troops to attack succesfully.


Below is the template of a strategy file.

**function turn(color, matrix, strength, x, y){ < YOUR CODE HERE >}**

Here is a very simple example of a valid file.

**function turn(color, matrix, strength, x, y){ return heal(); }**

All that should be in your file should be your function definition (and comments if desired).


Save your JS file and upload it when needed. When both you and your opponent have uploaded your files, you can hit 'Battle!' which will show you your results.

## An Important Note
**There are also some more rules, but I haven't gotten around to writing them.**
