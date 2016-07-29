# !/usr/bin/python
# title          :main.py
# description    :Allocates persons to rooms in a building
# author         :Stanley Ndagi
# email          :stanley.ndagi@andela.com
# date           :20160108
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================
import inspect
import random
import os, sys
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

"""importing from model.py"""
from .person import Fellow, Staff
from .room import LivingSpace, Office

"""
The following are lists
They are names of the Living spaces and the Offices at Dojo
One could edit them to desirable names
"""


class Building(object):
    """
    Building is the class for the whole building.
    Dojo will be an instance of it
    """
    def __init__(self, office_names, living_space_names, input_file):
        self.living_space_names = living_space_names
        self.office_names = office_names
        self.input_file = input_file
        self.offices = self.pre_populate("office")
        self.living_spaces = self.pre_populate("ls")
        self.all_employees = self.access_employees()[0]
        self.fellows = self.access_employees()[1]
        self.office_unallocated = []
        self.ls_unallocated = []

    def pre_populate(self, type_of_room):
        if type_of_room == "ls":
            #class we are dealing with is LivingSpace that requires name
            #list of living spaces (objects)
            rooms = [LivingSpace(name) for name in self.living_space_names]

        elif type_of_room == "office":
            #class we are dealing with is Office that requires name
            #list of offices (objects)
            rooms = [Office(name) for name in self.office_names]

        return rooms

    def access_employees(self):
        """Access the people in file"""
        employees = []
        fellows = []
        staff = []
        content = []
        try:
            with open(self.input_file) as myfile:
                content = myfile.readlines() #contents in one list
        except Exception:
            print "Some random exception"
        if len(content) == 0:
            return [False, False]
        for line in content:
            # Each line as a list, then split it into words as iems in list
            person = line.split('.')[0].split()
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
            employees.append(employee)
        random.shuffle(employees) #For random picking of employees
        random.shuffle(fellows)
        #Returns a list of all employees, call either of the indices to have a list of them
        return [employees, fellows]

    def allocate_room(self, employees, room):
        """Allocates the room receiving randomized person and room type"""
        allocated_room = {} # Holds allocated room
        unallocated = []
        room_index = 0
        for index, employee in enumerate(employees):
            allocated_room.update(
                {
                    room[room_index].name : room[room_index].add_person(employee)
                })
            if room[room_index].is_full():
                room_index += 1
                if room_index >= len(room): #len(room)
                    for employee in employees[index :]:
                        unallocated.append(employee)
                    break
        return allocated_room, unallocated

    def get_list_of_office_allocations(self):
        """
        Office Allocations
        Below, allocated room is returned
        It is a dictionary with room name as key, list of occupants as values
        NB: The list of occupants is also a list of strings (names of allocated employees)
        """
        allocated_offices, self.office_unallocated = self.allocate_room(self.all_employees, self.offices)
        return allocated_offices

    def get_list_of_living_space_allocations(self):
        """
        Living Space Allocations
        Similar to get_list_of_office_allocations()
        """
        allocated_living_spaces, self.ls_unallocated = self.allocate_room(self.fellows, self.living_spaces)
        return allocated_living_spaces

    def print_allocation(self, allocated_rooms):
        """Presents the allocation of room in the stipulated format"""
        room_names = allocated_rooms.keys()
        for room_name in room_names:
            if room_name in self.office_names:
                # Prints Name of office
                print room_name.upper() + " (OFFICE)"
                #Iterate through the list of occupants
                for occupants in allocated_rooms[room_name]:
                    print " " + occupants.name + ",",
                print ""
            else:
                # Prints Name of Living Spaces
                print room_name.upper() + " (LIVING SPACE)"
                for occupants in allocated_rooms[room_name]:
                    print " " + occupants.name + ",",
                print ""
        print "\n"
        return allocated_rooms[room_name] #For testing purposes

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
        if self.office_unallocated == None:
            return 'NO'
        else:
            if len(self.office_unallocated) == 0:
                print "No one missed an Office Slot\n"
            if len(self.ls_unallocated) == 0:
                print "No one missed a Living Space Slot\n"
            if len(self.office_unallocated) > 0:
                print "DISCLAIMER:\nOffices are full!\n" \
                    "The following {} person(s) have missed slots:".format(len(self.office_unallocated))
                for emp in self.office_unallocated:
                    print emp.name + ", ",
            if len(self.ls_unallocated) > 0:
                print "DISCLAIMER:\nLiving Spaces are full!\n" \
                    "The following {} person(s) have missed slots:".format(len(self.ls_unallocated))
                for emp in self.ls_unallocated:
                    print emp.name + ", ",
            print "\n"

    def print_allocation_for_one_room(self, room_name):
        """Prints allocations for specified room"""
        if room_name in self.office_names: #Is the room name entered in the list of offices
            print "\nThis is an Office"
            if room_name in self.allocated_offices.keys():
            #Is the room name entered in the list of allocated offices
                print room_name + ": "
                for occupants in self.allocated_offices[room_name]:
                    print occupants.name + ", ",
                return 'Office allocated'
            else:
                print room_name + " is not allocated anyone."

        elif room_name in self.living_space_names:
            print "\nThis is a Living Space"
            if room_name in self.allocated_living_spaces.keys():
                print room_name + ": "
                for occupants in self.allocated_living_spaces[room_name]:
                    print occupants.name + ", ",
                return 'LS allocated'
            else:
                print room_name + " is not allocated anyone."

        else:
            print "Room name is not valid"
            return 'Invalid'
