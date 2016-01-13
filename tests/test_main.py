import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from main import Building
from model import Person, Staff, Fellow, Room, Office, LivingSpace

living_space_names = ['Rm1', 'Rm2', 'Rm3', 'Rm4', 'Rm5', 'Rm6', 'Rm7', 'Rm8', 'Rm9', 'Rm10']
office_names = ['Hogwarts', 'Valhalla', 'Oculus', 'Krypton', 'Shire', 'Narnia', 'Camelot', 'Mordor', 'Round Table', 'Midgar']
input_file = "employees.txt"

class Test(unittest.TestCase):
    """Test"""
    def setUp(self):
        self.amity = Building(office_names, living_space_names, input_file)
        self.ls_unallocated = self.amity.allocate_room(self.amity.fellows, self.amity.living_spaces)[1]
        self.allocated_offices, self.office_unallocated = self.amity.allocate_room(self.amity.all_employees, self.amity.offices)


    def test_can_pre_populate(self):
        """
        Test if offices and living space can be prepopulated
        """
        self.assertIsInstance(self.amity.offices[4], Room)
        self.assertEquals('Shire', self.amity.offices[4].name)
        self.assertEquals(len(self.amity.offices), 10)
        self.assertEquals('Rm1', self.amity.living_spaces[0].name)
        self.assertEquals(len(self.amity.living_spaces), 10)
        self.assertEquals('<type \'bool\'>', str(type(self.amity.living_spaces[0].is_full())))
        self.assertIsNotNone(self.amity.offices[6].get_occupants())

    def test_can_access_employees_from_input(self):
        """
        Tests if employee details in input file are accessed and objects created
        """
        self.assertIsNotNone(self.amity.all_employees)
        self.assertIsInstance(self.amity.all_employees[0], Person)
        self.assertEquals('<type \'str\'>', str(type(self.amity.all_employees[0].name)))
        self.assertEquals('<type \'bool\'>', str(type(self.amity.all_employees[0].is_allocated_office)))

    def test_employees_entities_are_valid(self):
        """
        Tests if the types of employees are correct the Y or N are taken in for fellow
        """
        self.assertIsInstance(self.amity.fellows[0], Fellow)
        self.assertEquals('Y', self.amity.fellows[0].is_interested)

    def test_allocate_room(self):
        """
        Tests if the allocation of room works receiving randomized room and randomized person
        """
        self.assertIsNotNone(self.amity.allocate_room(self.amity.all_employees, self.amity.offices)[0].keys())
        self.assertIsInstance(self.amity.offices[0], Office)
        self.assertIsInstance(self.amity.living_spaces[0], LivingSpace)

    def test_print_room_allocation(self):
        """
        Tests if the allocation of room is presented in the stipulated format
        """
        self.assertEquals('<type \'list\'>', str(type(self.allocated_offices.keys()[:])))
        self.assertEquals('<type \'str\'>', str(type(self.allocated_offices.keys()[0])))

    def test_print_unallocated_employees(self):
        """
        Tests if the unallocated employees are appended
        """
        self.assertEquals('<type \'list\'>', str(type(self.office_unallocated)))
        self.assertEquals(self.office_unallocated, [])
        self.assertIsInstance(self.ls_unallocated[0], Fellow)

    def test_allocation_of_one_room(self):
        """
        Tests if Printing Occupants of one room can be accessed to be printed
        """
        self.assertIsInstance(self.allocated_offices["Shire"][0], Person)


if __name__ == '__main__':
    unittest.main()