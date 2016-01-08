# I'm using the two lines below to test. Comment them out then run to use
# import ipdb
# ipdb.set_trace()

"""importing from model.py"""
from model import Office, LivingSpace, Fellow, Staff

import random

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
        self.employee = self.access_employees()[0]
        self.staff = self.access_employees()[1]
        self.fellow = self.access_employees()[2]


    def pre_populate(self, type_of_room):
        rooms = []
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            rooms = [LivingSpace(name) for name in living_space_names] #list of living spaces (objects)
        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            rooms = [Office(name) for name in office_names] #list of offices (objects)

        # return [type (i) for i in results] #confirms that the rooms are populated and are classes
        #return [i.max_occupants for i in rooms] #prints out the name attribute of the rooms
        # random.shuffle(rooms) #For random picking of rooms
        return rooms


    def access_employees(self):
        """Access the people in file"""
        employees = []
        fellows = []
        staff = []
        with open("employees.txt") as f:
            content = f.read().splitlines() #contents in one list
        f.close()
        for x in xrange(1, len(content)):
            """each line as a list, then split it into words as iems in list"""
            person = content[x].split('.')[0].split()
            """Create Person with the items as arguments, the first two join to make one name"""
            if person[2] == 'Fellow':
                employee = Fellow(person[0] + " " + person[1], person[3])
                fellows.append(employee)
            elif person[2] == 'Staff':
                employee = Staff(person[0] + " " + person[1])
                staff.append(employee)
            employees.append(employee)
        random.shuffle(employees) #For random picking of employees
        """returns a list of all employees, call either of the indices to have a list of them"""
        return [employees, staff, fellows]


    def allocate_room(self, employee, room):
        """Allocates the room receiving randomized room and randomized person"""
        allocated_room = {} # Holds allocated office

        for y in xrange(0, len(employee)):
            for x in xrange(0, len(room)): # iterates through the offices
                if room[x].is_full() == False:
                    if isinstance (room[x], LivingSpace ):
                        allocated_room.update({ room[x].name : LivingSpace.add_person(room[x], employee[y].name) })
                    else:
                        allocated_room.update({ room[x].name : Office.add_person(room[x], employee[y].name) })

                    break

        return allocated_room

    def allocate_living_space(self):
        """Allocates the room receiving randomized room and randomized person"""
        allocated_living_space = {}




