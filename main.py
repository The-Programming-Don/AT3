from curses import halfdelay
from ssl import Options
from player import Player
from item import Item
from location import Location

#instanciating locations
entrance = Location("entrance", "S, E", "This seems to be the entrance room, its dark, mystical, weird magical totems are around \n and there is an ominous feeling about this place...")
exit = Location("Exit room", "N", "Its cold in here...there seems to be a trap door... the room is otherwise empty")
pre_exit = Location("Lower dungeon", "N" + "S", "Woah there is a red gem... and what seems to be fairies... maybe i should go talk to them")
ghost_room = Location("Hallway", "W, E, N", "There is a scary ghost over there blocking the door, he looks rather timid though, I can try talking to him though... \n there is also a door just past him that isn't blocked")
gaunetlet_room = Location("Treasure room", "S", "There seems to be a gauntlet floating on a stone, it seems so mystical and there is writing on the stone \n it reads...'Gauntlet of Destruction'")
rock_room = Location("Dungeon's lair", "E, S, W", "Nice a red rupee!, there is a massive stone to my south that i cant get past, something is behind it \n but to me west there is a jail room... its getting scary in here")
jail = Location("Jail", "W", "It's dark, wet and cold in here, i can see a jail cell in the back corner, something is in there too...")
key_room = Location("The Wizards Vault", "N", "Woah there is a magical key, it looks important... something tells me i should'nt have made it this far.")




#Creating the 2D array in which all locations are mapped out
locationGrid = [
    [0,1,0,0],
    [1,1,1,1],
    [1,0,1,0],
    [1,0,0,0]   
]
locationGrid[0][1] = gaunetlet_room
locationGrid[1][0] = entrance
locationGrid[1][1] = ghost_room
locationGrid[1][2] = rock_room
locationGrid[1][3] = jail
locationGrid[2][0] = pre_exit
locationGrid[2][2] = key_room
locationGrid[3][0] = exit


#function makes it easy to aslways know what rooms are avaliable based on current location
def directions_avaliable():
    if player.current_room == gaunetlet_room:
        options = gaunetlet_room.rooms_avaliable
    if player.current_room == entrance:
        options = entrance.rooms_avaliable
    if player.current_room == ghost_room:
        options = ghost_room.rooms_avaliable
    if player.current_room == rock_room:
        options = rock_room.rooms_avaliable
    if player.current_room == jail:
        options = jail.rooms_avaliable
    if player.current_room == pre_exit:
        options = pre_exit.rooms_avaliable
    if player.current_room == key_room:
        options = key_room.rooms_avaliable
    if player.current_room == exit:
        options = exit.rooms_avaliable


    return options


#instanciating items
rupee1 = Item("rupee")
rupee2 = Item("rupee")
rupee3 = Item("rupee")
key = Item("key")




# The frist user input
introduction = input("Hello, Enter the name of your character: ")

player = Player(introduction)
player.current_room = entrance

#nextRoom  = input(f"Where you like to go now?: {player.current_room.rooms_avaliable}")

