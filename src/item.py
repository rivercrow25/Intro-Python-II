class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        print('picked up %s' % (self.name))

    def describe(self):
        print('its a %s' % (self.description))

    def drop(self):
        print('dropped %s, its lost forever...' % (self.name))
