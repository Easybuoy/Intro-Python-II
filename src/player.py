# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory

    def setRoom(self,room):
        self.room = room

    def getRoom(self):
        return self.room

    def onTake(self, inventory):
        print(f'You have added {inventory} to your inventory')
    
    def onDrop(self, inventory):
        print(f'You have dropped {inventory} inventory')


    def addInventory(self, inventory):
        self.inventory.append(inventory)
        self.onTake(inventory)

    def dropInventory(self, inventory):
        if len(self.inventory) == 0:
            print('No inventory to drop')
            return
        else:
            for i in range(0, len(self.inventory)):
                if (inventory == self.inventory[i]):
                    self.onDrop(inventory)
                    self.inventory.pop(i)
                    break
                else:
                    print(f"{inventory} not found in  inventory")
        