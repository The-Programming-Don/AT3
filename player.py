class Player:
    def __init__(self, name):
        self.name = name  
        self.current_room = ""  
        self.inventory =[]
        self.x = 0
        self.y = 1
        
    def print_inventory():
        return print(Player.inventory)

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def move_north(self):
        self.move(mx=0, my=-1)

    def move_south(self):
        self.move(mx=0, my=1)

    def move_east(self):
         self.move(mx=1, my=0)

    def move_west(self):
        self.move(mx=-1, my=0)



