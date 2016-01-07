# I'm using the two lines below to test. Comment them out then run to use
# import ipdb
# ipdb.set_trace()

"""importing from model.py"""
from model import Office, LivingSpace

"""
The following are lists
They are names of the Living spaces and the Offices at Dojo (we'll use them as Amity's)
One could edit them to desirable names
"""
living_space_names = ['Rm1', 'Rm2', 'Rm3', 'Rm4', 'Rm5', 'Rm6', 'Rm7', 'Rm8', 'Rm9', 'Rm10']
office_names = ['Hogwarts', 'Valhalla', 'Oculus', 'Krypton', 'Shire', 'Narnia', 'Camelot', 'Mordor', 'Round Table', 'Midgar']


class Building(object):
    """Building is the class for the whole building. Amity will be an instance of it, same as Dojo (for Nairobi)"""
    def __init__(self):
        self.living_space_names = living_space_names
        self.office_names = office_names
        self.offices = self.pre_populate("office")
        self.living_spaces = self.pre_populate("ls")

    def pre_populate(self, type_of_room):
        rooms = []
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            rooms = [LivingSpace(name) for name in living_space_names] #list of living spaces (objects)
        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            rooms = [Office(name) for name in office_names] #list of offices (objects)

        # return [type (i) for i in results] #confirms that the rooms are populated and are classes
        #return [i.name for i in rooms] #prints out the name attribute of the rooms
        return rooms
