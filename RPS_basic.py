import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
valid_options = [rock, paper, scissors]

print '--- Welcome to the Rock, Paper, Scissors game! ---\n'

cpu_choice = random.choice([rock, paper, scissors])
print 'CPU has made its choice! (hint: %s)' % cpu_choice

player_choice = ''
while player_choice not in valid_options:
    player_choice = raw_input("Please make your choice ('rock', 'paper', 'scissors'): ").lower()

print "\nYou selected:\t\t'%s'" % player_choice
print "Computer selected:\t'%s'" % cpu_choice

if player_choice == cpu_choice:
    print "Draw!"
elif (player_choice == rock and cpu_choice == scissors) or \
        (player_choice == paper and cpu_choice == rock) or \
        (player_choice == scissors and cpu_choice == paper):
    print "You won!"
else:
    print "You lost!"
