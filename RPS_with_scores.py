import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
yes = 'yes'
no = 'no'
keep_playing = True

valid_options = [rock, paper, scissors]

synonyms = {
    'rock': rock,
    'r': rock,
    '1': rock,
    'paper': paper,
    'p': paper,
    '2': paper,
    'scissors': scissors,
    's': scissors,
    '3': scissors,
    'yes': yes,
    'yep': yes,
    'yea': yes,
    'y': yes,
    'no': no,
    'nah': no,
    'n': no
}

wins = 'w'
losses = 'l'
draws = 'd'

score = {
    wins: 0,
    losses: 0,
    draws: 0
}


def play_rps():
    welcome()

    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    determine_result(cpu_choice, player_choice)


def welcome():
    print '\n--- Welcome to the Rock, Paper, Scissors game! ---\n'


def get_cpu_choice():
    cpu_choice = random.choice([rock, paper, scissors])
    print 'CPU has made its choice! (hint: %s)' % cpu_choice
    return cpu_choice


def get_player_choice():
    while True:
        player_choice = raw_input('Please make your choice: ').lower()
        if synonyms.get(player_choice, 'unknown') in valid_options:
            return synonyms[player_choice]


def determine_result(cpu_choice, player_choice):
    print "\nYou selected:\t\t'%s'" % player_choice
    print "Computer selected:\t'%s'" % cpu_choice

    if player_choice == cpu_choice:
        score[draws] += 1
        print 'Draw!'
    elif (player_choice == rock and cpu_choice == scissors) or \
            (player_choice == paper and cpu_choice == rock) or \
            (player_choice == scissors and cpu_choice == paper):
        score[wins] += 1
        print 'You won!'
    else:
        score[losses] += 1
        print 'You lost!'


def is_player_continuing():
    again = raw_input('\nPlay again? (y/n): ').lower()
    if synonyms[again] != yes:
        return False
    else:
        return True


def final_score():
    print '\nFinal score is:\nWins: %d, Draws: %d, Losses: %d' % (score[wins], score[draws], score[losses])


# Main flow
while keep_playing:
    play_rps()
    keep_playing = is_player_continuing()

final_score()
