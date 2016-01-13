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


class Building(object):
    """
    Building is the class for the whole building.
    Amity will be an instance of it, same as Dojo (for Nairobi)
    """
    def __init__(self, office_names, living_space_names, input_file):
        self.living_space_names = living_space_names
        self.office_names = office_names
        self.input_file = input_file
        self.offices = self.pre_populate("office")
        self.living_spaces = self.pre_populate("ls")
        self.all_employees = self.access_employees()[0]
        self.staff = self.access_employees()[1]
        self.fellows = self.access_employees()[2]

    def pre_populate(self, type_of_room):
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            #list of living spaces (objects)
            rooms = [LivingSpace(name) for name in self.living_space_names]

        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            #list of offices (objects)
            rooms = [Office(name) for name in self.office_names]

        else:
            rooms = [] # Corner case
        return rooms

    def access_employees(self):
        """Access the people in file"""
        employees = []
        fellows = []
        staff = []
        with open(self.input_file) as myfile:
            content = myfile.read().splitlines() #contents in one list
        myfile.close()
        for line in xrange(1, len(content)):
            # Each line as a list, then split it into words as iems in list
            person = content[line].split('.')[0].split()
            name = person[0] + " " + person[1]
            role = person[2]
            #Create Person with the items as arguments, the first two join to make one name
            if role == 'Fellow':
                wants_accomodation = person[3]
                employee = Fellow(name, wants_accomodation)
                if wants_accomodation == 'Y':
                    fellows.append(employee)
            elif role == 'Staff':
                employee = Staff(name)
                staff.append(employee)
            employees.append(employee)
        random.shuffle(employees) #For random picking of employees
        random.shuffle(fellows)
        #Returns a list of all employees, call either of the indices to have a list of them
        return [employees, staff, fellows]

    def allocate_room(self, employees, room):
        """Allocates the room receiving randomized person and room type"""
        allocated_room = {} # Holds allocated room
        count = 0
        room_index = 0
        for emp_index in range(0, len(employees)):
            count += 1
            allocated_room.update(
                {
                    room[room_index].name : room[room_index].add_person(employees[emp_index])
                })
            if room[room_index].is_full():
                room_index += 1
                if room_index >= len(room): #len(room)
                    print "DISCLAIMER:\nRooms are full\nThe following",
                    print len(employees) - (emp_index + 1),
                    print "person(s) have missed slots:"
                    for emp_index in range((emp_index + 1), len(employees)):
                        print employees[emp_index].name + ", ",
                    print "\n"
                    break
        return allocated_room

    def get_list_of_office_allocations(self):
        """
        Office Allocations
        Below, allocated room is returned
        It is a dictionary with room name as key, list of occupants as values
        NB: The list of occupants is also a list of strings (names of allocated employees)
        """
        allocated_offices = self.allocate_room(self.all_employees, self.offices)
        return allocated_offices

    def get_list_of_living_space_allocations(self):
        """
        Living Space Allocations
        Similar to get_list_of_office_allocations()
        """
        allocated_living_spaces = self.allocate_room(self.fellows, self.living_spaces)
        return allocated_living_spaces

    def print_allocation(self, allocated_rooms):
        """Presents the allocation of room in the stipulated format"""
        room_names = allocated_rooms.keys()
        for room_index in xrange(0, len(room_names)):
            if room_names[room_index] in self.office_names:
                # Prints Name of office
                print room_names[room_index].upper() + " (OFFICE)"
                #Iterate through the list of occupants
                for occupants in allocated_rooms[room_names[room_index]]:
                    print " " + occupants.name + ",",
                print ""
            else:
                # Prints Name of Living Spaces
                print room_names[room_index].upper() + " (LIVING SPACE)"
                for occupants in allocated_rooms[room_names[room_index]]:
                    print " " + occupants.name + ",",
                print ""
        print "\n"

    def print_office_allocation(self):
        """Prints out the offices"""
        print "Offices allocations: \n",
        self.allocated_offices = self.get_list_of_office_allocations()
        self.print_allocation(self.allocated_offices)

    def print_living_space_allocation(self):
        """Prints out the living spaces"""
        print "Living Spaces allocations: \n",
        self.allocated_living_spaces = self.get_list_of_living_space_allocations()
        self.print_allocation(self.allocated_living_spaces)

    def print_unallocated_employees(self):
        """Prints unallocated employees"""
        if len(self.get_list_of_office_allocations()[1]) == 0:
            print "None is unallocated"
        else:
            print "some are unallocated"

    def print_allocation_for_one_room(self, room_name):
        """Prints allocations for specified room"""
        if room_name in self.office_names: #Is the room name entered in the list of offices
            print "\nThis is an office"
            if room_name in self.allocated_offices.keys():
            #Is the room name entered in the list of allocated offices
                print room_name + ": "
                for occupants in self.allocated_offices[room_name]:
                    print occupants.name + ", ",
            else:
                print room_name + " is not allocated anyone."

        elif room_name in self.living_space_names:
            print "\nThis is an Living Space"
            if room_name in self.allocated_living_spaces.keys():
                print room_name + ": "
                for occupants in self.allocated_living_spaces[room_name]:
                    print occupants.name + ", ",
            else:
                print room_name + " is not allocated anyone."

        else:
            print "Room name is not valid"