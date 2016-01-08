# !/usr/bin/python
# title          :main.py
# description    :Allocates persons to rooms in a building
# author         :Stanley Ndagi
# email          :stanley.ndagi@andela.com
# date           :20160108
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================
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
        self.allocated_office_names = self.office_names


    def pre_populate(self, type_of_room):
        rooms = []
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            rooms = [LivingSpace(name) for name in living_space_names] #list of living spaces (objects)
        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            rooms = [Office(name) for name in office_names] #list of offices (objects)

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
            # each line as a list, then split it into words as iems in list
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
        random.shuffle(fellows)
        """returns a list of all employees, call either of the indices to have a list of them"""

        return [employees, staff, fellows]


    def allocate_room(self, employee, room):
        """Allocates the room receiving randomized room and randomized person"""
        allocated_room = {} # Holds allocated office

        for y in xrange(0, len(self.employee)): # len(self.employee)
            for x in xrange(0, len(room)): # iterates through the offices
                if not room[x].is_full():
                    if isinstance(room[x], LivingSpace):
                        allocated_room.update({room[x].name : LivingSpace.add_person(room[x], employee[y].name)})
                    else:
                        allocated_room.update({room[x].name : Office.add_person(room[x], employee[y].name)})

                    break
        return allocated_room


    def print_room_allocation(self):
        """Presents the allocation of room in the stipulated format"""

        """Print out the offices first"""
        """
        Below, allocated room is returned
        It is a dictionary with room name as key, list of occupants as values
        NB: The list of occupants is also a list of strings (names of allocated employees)
        """
        allocated_offices = self.allocate_room(self.employee, self.offices)
        self.office_names = allocated_offices.keys() # Room names as a list
        print "Offices allocated: ",
        for office in office_names:
            print office +" ,",
        print "\n"

        for x in xrange(0, len(office_names)):
            print office_names[x].upper() + " (OFFICE)" # Prints Name of office
            """Iterate through the dictionary's values (list of occupants)"""
            for i in allocated_offices.values()[x]: # Prints the elements of occupants
                print " " + i + ",",
            print ""
        print "\n"

        """Print out the living spaces now"""
        allocated_living_spaces = self.allocate_room(self.fellow, self.living_spaces)
        self.living_space_names = allocated_living_spaces.keys() # Room names as a list
        print "Living Spaces allocated: ",
        for living_spaces in living_space_names:
            print living_spaces +" ,",
        print "\n"

        for x in xrange(0, len(living_space_names)):
            print living_space_names[x].upper() + " (LIVING SPACE)" # Prints Name of office
            """Iterate through the dictionary's values (list of occupants)"""
            for i in allocated_living_spaces.values()[x]: # Prints the elements of occupants
                print " " + i + ",",
            print ""

