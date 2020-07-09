class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print('its a %s' % (self.description))

    def __str__(self):
        return "%s" % (self.name)
