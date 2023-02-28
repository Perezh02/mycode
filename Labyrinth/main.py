#!/usr/bin/env python

print("""
Can you Escape the Labyrinth!

You find yourself in the entrance of a dark labyrinth. Your goal is to navigate through the labyrinth and find the treasure hidden at the end. Good luck!
 
 """)

import random

# Define the labyrinth map
labyrinth = {
    'entrance': {
        'description': 'You are standing at the entrance of the labyrinth. There are paths to the north and east.',
        'items': [],
        'exits': {'north': 'north1', 'east': 'east1'}
    },
    'north1': {
        'description': 'You are in a small room. There are paths to the south, east, and west.',
        'items': ['torch'],
        'exits': {'south': 'entrance', 'east': 'north2', 'west': 'west1'}
    },
    'north2': {
        'description': 'You are in a long hallway. There are paths to the west and east.',
        'items': ['key'],
        'exits': {'west': 'north1', 'east': 'north3'}
    },
    'north3': {
        'description': 'You are in a large room with a high ceiling. There are paths to the west and south.',
        'items': [],
        'exits': {'west': 'north2', 'south': 'north4'}
    },
    'north4': {
        'description': 'You are in a narrow hallway. There are paths to the north and south.',
        'items': [],
        'exits': {'north': 'north3', 'south': 'north5'}
    },
    'north5': {
        'description': 'You are in a small room with a trapdoor on the floor. There is a path to the north.',
        'items': [],
        'exits': {'north': 'north6'}
    },
    'north6': {
        'description': 'You are in a circular room with a spiral staircase leading up. There is a path to the south.',
        'items': [],
        'exits': {'south': 'north5', 'up': 'treasure'}
    },
    'west1': {
        'description': 'You are in a dark hallway. There are paths to the east and west.',
        'items': [],
        'exits': {'east': 'north1', 'west': 'west2'}
    },
    'west2': {
        'description': 'You are in a small room with a locked door to the west. There is a path to the east.',
        'items': [],
        'exits': {'east': 'west1', 'west': 'west3'}
    },
    'west3': {
        'description': 'You are in a room with a large statue of a dragon. There is a path to the east.',
        'items': ['sword'],
        'exits': {'east': 'west2'}
    },
    'treasure': {
        'description': 'Congratulations, you have found the treasure!',
        'items': [],
        'exits': {}
    }
}

# Define the player's starting location and inventory
player_location = 'entrance'
player_inventory = ['map']

# Define functions for handling game logic

def move_player(direction):
    """
    Move the player in the specified direction.
    """
    global player_location
    
    if direction in labyrinth[player_location]['exits']:
        player_location = labyrinth[player_location]['exits'][direction]
        print(labyrinth[player_location]['description'])
    else:
        print("You can't go that way.")
        
def get_item(item):
    global player_inventory
    if item in labyrinth[player_location]['items']:
        player_inventory.append(item)
        labyrinth[player_location]['items'].remove(item)
        print(f"You picked up the {item}.")
    else:
        print("There is no such item here.")

def use_item(item):
    global player_inventory
    if item in player_inventory:
        if item == 'torch':
            print("You light the torch and can now see in the dark.")
        elif item == 'key':
            print("You unlock the door.")
            labyrinth['west2']['exits']['west'] = 'treasure'
        elif item == 'sword':
            print("You swing the sword and feel powerful.")
        else:
            print("Nothing happens.")
    else:
        print("You don't have that item.")

def look():
    """
    Print the description of the player's current location and any items in the room.
    """
    print(labyrinth[player_location]['description'])

    if labyrinth[player_location]['items']:
        print("You see the following items:")
        for item in labyrinth[player_location]['items']:
            print(f"- {item}")
    else:
        print("There are no items here.")

while True:
    # Print available commands
    print("\nAvailable commands:")
    print("- go [direction]")
    print("- get [item]")
    print("- use [item]")
    print("- look")
    print("- quit")

    # Get player input
    command = input("> ").lower().split()

    # Handle different commands
    if len(command) == 2:
        verb, noun = command
        if verb == 'go':
            move_player(noun)
        elif verb == 'get':
            get_item(noun)
        elif verb == 'use':
            use_item(noun)
        else:
            print("Invalid command.")
    elif len(command) == 1:
        if command[0] == 'look':
            look()
        elif command[0] == 'quit':
            break  # Exit the loop
        else:
            print("Invalid command.")