#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

import os

# importing Image class from PIL package 
from PIL import Image 
 
# creating a object 
im = Image.open(r"YOU WIN.jpg")
lose = Image.open(r"you lose.jpeg")

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========

Get to the garden with a key and a badge
Avoid the monsters!

Commands:
  go [direction]
  get [item]
  teleport [room]
  help
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east' : 'Diningroom',
                  'west' : 'Closet',
                  'north' : 'Downstairs'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                  'south' : 'Closet',
                  'west' : 'Downstairs'
                },
            'Diningroom' : {
                  'west' : 'Hall',
                  'south' : 'Garden'
                },
            'Garden' : {
                'north' : 'Diningroom',
                'west' : 'Rocket'
                },
            'Closet' : {
                'east' : 'Diningroom',
                'item' : 'sword',
                'north' : 'Kitchen'
                },
            'Downstairs' : {
                'up' : 'Upstairs',
                'east' : 'Kitchen',
                'south' : 'Hall',
                'down' : 'Basementstairs'
                },
            'Upstairs' : {
                'down' : 'Downstairs',
                'west' : 'Upperhall'
                },
            'Upperhall' : {
                'east' : 'Upstairs',
                'north' : 'Office',
                'south' : 'Uppercloset'
                },
            'Basementstairs' : {
                'up' : 'Downstairs',
                'north' : 'Jail',
                'east' : 'Jail',
                'west' : 'Jail'
                },
            'Jail' : {
                
                },
            'Office' : {
                'south' : 'Upperhall',
                'item' : 'key'
                },
            'Uppercloset' : {
                'north' : 'Upperhall',
                },
            'Rocket' : {
                'east' : 'Garden',
                'up' : 'Moonrocket'
                },
            'Moonrocket' : {
                'down' : 'Rocket',
                'north' : 'Moon',
                'up' : 'Marsrocket'
                },
            'Moon' : {
                'south' : 'Moonrocket',
                'item' : 'portal'
                },
            'Marsrocket' : {
                'down' : 'Moonrocket',
                'north' : 'Mars'
                },
            'Mars' : {
                'south' : 'Marsrocket',
                'item' : 'badge'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  
  if len(move) < 2 and not move == ['help']:
      continue
  if len(move) > 2:
      continue

  #if they type 'go' first

 
 
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

    #if they type 'teleport' first
  if move[0] == 'teleport' and 'portal' in inventory:
      #set the current room to the new room
      currentRoom = move[1].title()

      #if they type 'help' first
  if move[0] == 'help':
      if not 'sword' in inventory:
          print('''
Go to the Closet and get the sword.
The Closet is west of the Hall.
''')
      elif 'sword' in inventory and not 'key' in inventory:
          print('''
Go to the Office and get the key.
The Office is north of the Upperhall.
''')
      elif 'sword' in inventory and 'key' in inventory and not 'portal' in inventory:
          print('''
Go to the Moon and get the portal.
The Moon is north of the Moonrocket.
To launch the Rocket, type "go up"
''')
      elif 'sword' in inventory and 'key' in inventory and 'portal' in inventory and not 'badge' in inventory:
          print('''
Go to Mars and get the badge.
Mars is north of the Marsrocket.
''')
      elif 'sword' in inventory and 'key' in inventory and 'portal' in inventory and 'badge' in inventory:
          print('''
Go to the Garden to escape the house.
''')


#player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and not 'sword' in inventory and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    lose.show()
    break

#Player loses if they get stuck in the jail
  if currentRoom == 'Jail':
      print('You got stuck in the jail... GAME OVER!')
      lose.show()
      break

#Player wins if they get to the garden with a key and a potion

  


#if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  if currentRoom == 'Garden' and 'key' in inventory and 'badge' in inventory:
      print('You escaped the house... YOU WIN!')
      im.show()
      break

    