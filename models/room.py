"""
Model for the rooms at the building (Amity)
"""
class Room(object):
    """Room represents a Room in the building"""

    def __init__(self, name):  # It has to have a name
        self.name = name
        self.max_occupants = 4
        self.occupants = []


    def add_person(self, person):
        """Adds a member to the room"""
        self.occupants.append(person)
        return self.occupants

    def is_full(self):
        """Returns boolean, is the room full?"""
        if len(self.occupants) == self.max_occupants:
            return True
        else:
            return False

    def get_occupants(self):
        """Returns the occupants in a given room"""
        return self.occupants


class Office(Room):
    """Office is a Room (inherits from Room)"""
    def __init__(self, name):
        # Room initialize with its Room.__init__
        super(Office, self).__init__(name)
        self.max_occupants = 6

class LivingSpace(Room):
    """LivingSpace is a Room"""
    def __init__(self, name):
        # Room initialize with its Room.__init__
        super(LivingSpace, self).__init__(name)
