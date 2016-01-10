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
        self.employees = self.access_employees()[0]
        self.staff = self.access_employees()[1]
        self.fellows = self.access_employees()[2]
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
            # Each line as a list, then split it into words as iems in list
            person = content[x].split('.')[0].split()
            name = person[0] + " " + person[1]
            role = person[2]
            #Create Person with the items as arguments, the first two join to make one name
            if role == 'Fellow':
                wants_accomodation = person[3]
                employee = Fellow(name, wants_accomodation)
                fellows.append(employee)
            elif role == 'Staff':
                employee = Staff(name)
                staff.append(employee)
            else:
                print "You have not entered details in the format of two names [tab] Fellow / Staff [tab] is_interested"
            employees.append(employee)
        random.shuffle(employees) #For random picking of employees
        random.shuffle(fellows)
        #Returns a list of all employees, call either of the indices to have a list of them

        return [employees, staff, fellows]


    def allocate_room(self, employees, room):
        """Allocates the room receiving randomized person and room type"""
        allocated_room = {} # Holds allocated room
        unallocated_employees = []

        for emp_index in xrange(0, len(employees)): # len(self.employee)
            for room_index in xrange(0, len(room)): # iterates through the room
                if room[room_index].is_full():
                    unallocated_employees.append(employees[emp_index].name)
                elif not room[room_index].is_full():
                    if isinstance(room[room_index], LivingSpace):
                        allocated_room.update(
                            {
                                room[room_index].name : LivingSpace.add_person(room[room_index], employees[emp_index].name)
                            })
                    else:
                        allocated_room.update(
                            {
                                room[room_index].name : Office.add_person(room[room_index], employees[emp_index].name)
                            })

                    break
        # print unallocated_employees
        return allocated_room


    def get_list_of_office_allocations(self):
        """Office Allocations"""
        """
        Below, allocated room is returned
        It is a dictionary with room name as key, list of occupants as values
        NB: The list of occupants is also a list of strings (names of allocated employees)
        """
        allocated_offices = self.allocate_room(self.employees, self.offices)
        return allocated_offices

    def get_list_of_living_space_allocations(self):
        """Living Space Allocations"""
        """Similar to get_list_of_office_allocations()"""
        allocated_living_spaces = self.allocate_room(self.fellows, self.living_spaces)
        return allocated_living_spaces


    def print_allocation(self, room_allocation):
        """Presents the allocation of room in the stipulated format"""
        allocated_rooms = room_allocation
        room_names = allocated_rooms.keys() # Room names as a list
        for room in room_names:
            print room +" ,",
        print "\n"

        for room_index in xrange(0, len(room_names)):
            if room_allocation == self.get_list_of_office_allocations():
                # Prints Name of office
                print room_names[room_index].upper() + " (OFFICE)"
            else:
                # Prints Name of Living Spaces
                print room_names[room_index].upper() + " (LIVING SPACE)"

            #Iterate through the dictionary's values (list of occupants)
            for occupants in allocated_rooms.values()[room_index]:
                # Prints the elements of occupants
                print " " + occupants + ",",
            print ""
        print "\n"


    def print_office_allocation(self):
        """Print out the offices first"""
        print "Offices allocated: ",
        self.print_allocation(self.get_list_of_office_allocations())

    def print_living_space_allocation(self):
        """Print out the living spaces now"""
        print "Living Spaces allocated: ",
        self.print_allocation(self.get_list_of_living_space_allocations())

