class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print('its a %s, %s' % (self.name, self.description))

    def __str__(self):
        return "%s" % (self.name)
