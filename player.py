import location
import item
import Npc
class Player:
    def __init__(self, name):
        self.name = name        
        self.inventory =[]
        self.x = 0
        self.y = 1
        self.rupee = 0
        self.allow_player_in_gauntlet = False
        self.hasGauntlet = False
        self.allowplayerinroom = False
    
    # prints the inentory for the user    
    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print("--> " + str(item))
        print("--> Rupees: {}".format(self.rupee))

#this set of move methods allows the player to move through an x and y grid by adding or taking 1 from x or y
    def move(self, mx, my):
        self.x += mx
        self.y += my

    def move_north(self):
        self.move(mx=0, my= -1)

    def move_south(self):
        self.move(mx=0, my= +1)

    def move_east(self):
         self.move(mx=1, my=0)

    def move_west(self):
        self.move(mx=-1, my=0)


#buy method to interact with the Elf
    def Buy(self):
        room = location.where_abouts(self.x, self.y)
        room.check_if_trading(self)
# this searches for the staff so that the user can go into the ghost room
    def search_for_staff(self):
        for x in self.inventory:
            if x == "Staff of Ice":
                return True
        
    # adds the gauntlet 
    def pick_up_gauntlet(self):
        self.inventory.append("Gauntlet of Destruction")
        location.Gauntlet_room.destroy
        print("Gauntlet of Destruction aquired!")
        location.Rock_Room.hasGauntlet = True
        self.hasGauntlet = True

    def destroy_Rock(self):
        print("Finally, Ive destoyed the rock! And an Exit is revaled, I'm going in!")
        self.move_south()

    def pick_up_rupee(self):
        print("Rupee Aquired!")
        self.rupee += 1
    
    def collect_key(self):
        print("The Wizards key Aquired!")
        self.allowplayerinroom = True
        self.inventory.append("The Wizards Key")



