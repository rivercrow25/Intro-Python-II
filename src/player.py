# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def pick_up(self, item):
        self.inventory.append(item)
        print('picked up %s' % item.name)
        return self.inventory

    def drop_item(self, item):
        self.inventory.remove(item)
