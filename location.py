import Npc
class Location():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        
    def description(self):
        raise NotImplementedError("subclasss")

class Entrance(Location):
    def description(self):
        return """
        This seems to be the entrance room, its dark, mystical, weird magical totems are around
        and there is an ominous feeling about this place...
        """

class Exit(Location):
    def description(self):
        return """
        Its cold in here...there seems to be a trap door... the room is otherwise empty
        """

class Pre_Exit(Location):
    def description(self):
        return """
        "Woah that door doesnt look like its going to open without a key \n there is a red gem... and what seems to be fairies... maybe i should go talk to them"
        """

class Ghost_Room(Location):
    def description(self):
        return """
        "There seems to be a Ghost of fire in this hallway blocking off an exit..."
        """

class Rock_Room(Location):
    def description(self):
        return """
        Nice a red rupee!, there is a massive stone to my south that i cant get past, something is behind it \n but to me west there is a jail room... its getting scary in here
        """

class Gauntlet_room(Location):
    def description(self):
        return """
        There seems to be a gauntlet floating on a stone, it seems so mystical and there is writing on the stone \n it reads...'Gauntlet of Destruction'
        """

class KeyRoom(Location):
    def description(self):
        return """
        Woah there is a magical key, it looks important... something tells me i should'nt have made it this far.
        """

class GhostTile(Location):
    def __init__(self, x, y):
        self.ghost = Npc.Ghost
        super().__init__(x, y)

class elfTile(Location):
    def __init__(self, x, y):
        self.elf = Npc.Elf()
        super().__init__(x, y)

    def description(self):
        return """
        You're in the Jail. the aura of this place doesnt make you feel good.
        There is an Elf in the Jail Cell
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Rupee".format(i, item.type, item.value))
        while True:
            user_input = input("Choose an item or press 0 to exit: ")
            if user_input in ['0']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller,buyer,to_swap)
                except ValueError:
                    print("Invalid Choice")
    
    def swap(self, seller, buyer, item):
        if item.value > buyer.rupee:
            print("That amount of Rupee isn't gonna cut it! I need 3!")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.rupee = seller.rupee + item.value
        buyer.Rupee = buyer.rupee - item.value
        print("Hehehe, thanks kid, enjoy the staff")

    def check_if_trading(self, player):
        while  True:
            print("Would you like to (B)uy the staff? or (Q)uit")
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['B', 'b']:
                self.trade(buyer=player, seller=self.elf)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return"""
        An old Elf sits in the back of his cell,
        He looks willing to trade.
        """

class Fairy(Location):
    def __init__(self, x, y):
        self.fairy = Npc.Fairy
        super().__init__(x, y)











    
locationGrid = [
    [None,Gauntlet_room(1,0),None,None],
    [Entrance(0,1),Ghost_Room(1,1),Rock_Room(2,1),elfTile(3,1)],
    [Pre_Exit(0,2),None,KeyRoom(2,2),None],
    [Exit(0,3),None,None,None]   
]

world_dsl = """
|  |HR|  |  |
|SR|GR|RR|NR|
|IR|  |KR|  |
|VR|  |  |  |
"""
room_type = { "VR": Exit,
"SR": Entrance,
"GR": Ghost_Room,
"HR": Gauntlet_room,
"RR": Rock_Room,
"NR": elfTile,
"KR": KeyRoom,
"IR": Pre_Exit,
"  ": None}

world_map = []

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            roomtype = room_type[dsl_cell]
            row.append(roomtype(x,y) if roomtype else None)
        world_map.append(row)


def is_dsl_valid(dsl):
    if dsl.count("|SR|") != 1:
        return False
    if dsl.count("|VR|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("l") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

def where_abouts(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return locationGrid[y][x]
    except IndexError:
        return None 
    