from model import Office, LivingSpace
"""importing from model.py"""

"""
The following are lists
They are names of the Living spaces and the Offices at Dojo (we'll use them as Amity's)
One could edit them to desirable names
"""
living_space_names = ['Rm0', 'Rm1', 'Rm2', 'Rm3', 'Rm4', 'Rm5', 'Rm6', 'Rm7', 'Rm8', 'Rm9']
office_names = ['Hogwarts', 'Valhalla', 'Oculus', 'Krypton', 'Shire', 'Narnia', 'Camelot', 'Mordor', 'Round Table', 'Midgar']


class Building(object):
    """Building is the class for the whole building. Amity will be an instance of it, same as Dojo (for Nairobi)"""
    def __init__(self):
        self.living_space_names = living_space_names
        self.office_names = office_names

    def pre_populate(self, type_of_room):
        results = []
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            results = [LivingSpace(name) for name in living_space_names] #list of living spaces (objects)
        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            results = [Office(name) for name in office_names] #list of offices (objects)

        return [i.name for i in results]

if __name__ == '__main__':
    amity = Building()
    print amity.pre_populate("ls")
    print amity.pre_populate("office")
