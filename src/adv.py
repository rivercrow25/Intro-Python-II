from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
is_started = True
is_playing = False
while is_started:
    player_name = input(
        "welcome to the cave of the mad god! to start enter your name: ")
    print('to quit at any time type quit when prompted for what to do')
    player = Player(player_name, room['outside'])
    is_playing = True
    while is_playing:
        print("you're current location is %s" % (player.current_room.current))
        action = input('what do you want to do? you can go to an area by typing n for north, s for south, e for east or w for west or you can type help for a description of the current room: ')
        if str(action).lower() == 'help':
            print(player.current_room.description)
        elif str(action).lower() == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action).lower() == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action).lower() == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                pass
            else:
                'not a valid option, try again'
        elif str(action) == 's':
            if len(player.current_room.s_to):
                player.current_room = player.current_room.s_to
                pass
            else:
                print('not a valid option, try again')
        elif str(action).lower() == 'quit':
            is_playing, is_started = False, False
