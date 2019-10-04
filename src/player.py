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

    def addInventory(self, inventory):
        self.inventory.append(inventory)
        print(f'You have added {inventory} to your inventory')

    def dropInventory(self, inventory):
        if len(self.inventory) == 0:
            return 'No inventory to drop'
        else:
            for i in range(0, len(self.inventory)):
                if (inventory == self.inventory[i]):
                    print(f'You have dropped {[self.inventory[i]]} item')
                    self.inventory.pop(i)
                    break
        