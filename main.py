import imp
from player import Player
from item import Item
from location import Location

entrance = Location("entrance", "S" + "E", "This seems to be the entrance room, its dark, mystical, weird magical totems are around \n and there is an ominous feeling about this place...")
exit = Location("Exit room", "N", "Its cold in here...there seems to be a trap door... the room is otherwise empty")
pre_exit = Location("Lower dungeon", "N" + "S", "Woah there is a red gem... and what seems to be fairies... maybe i should go talk to them")
ghost_room = Location("Hallway", "W"+"E"+"N", "There is a scary ghost over there blocking the door, he looks rather timid though, I can try talking to him though... \n there is also a door just past him that isn't blocked")
gaunetlet_room = Location("Treasure room", "S", "There seems to be a gauntlet floating on a stone, it seems so mystical and there is writing on the stone \n it reads...'Gauntlet of Destruction'")
rock_room = Location("Dungeon's lair", "E" + "S"+ "W", "Nice a red rupee!, there is a massive stone to my south that i cant get past, something is behind it \n but to me west there is a jail room... its getting scary in here")
jail = Location("Jail", "W", "It's dark, wet and cold in here, i can see a jail cell in the back corner, something is in there too...")
key_room = Location("The Wizards Vault", "N", "Woah there is a magical key, it looks important... something tells me i should'nt have made it this far.")

rupee1 = Item("rupee")
rupee2 = Item("rupee")
rupee3 = Item("rupee")
key = Item("key")

