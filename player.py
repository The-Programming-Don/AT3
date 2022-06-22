import location
class Player:
    def __init__(self, name):
        self.name = name        
        self.inventory =[]
        self.x = 0
        self.y = 1
        self.rupee = 0
        
    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print("--> " + str(item))
        print("Rupees: {}".format(self.gold))

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

    def Buy(self):
        room = location.where_abouts(self.x, self.y)
        room.check_if_trading(self)



