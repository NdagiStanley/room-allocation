import inspect
import os
import sys
import unittest
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.building import Building
from models.person import Person, Staff, Fellow
from models.room import Room, Office, LivingSpace

living_space_names = ['Rm1', 'Rm2', 'Rm3', 'Rm4', 'Rm5', 'Rm6', 'Rm7', 'Rm8',
    'Rm9', 'Rm10']
office_names = ['Hogwarts', 'Valhalla', 'Oculus', 'Krypton', 'Shire', 'Narnia',
    'Camelot', 'Mordor', 'Round Table', 'Midgar']
input_file = "files/employees.txt"
empty_file = "files/empty_file.txt"

class Test(unittest.TestCase):
    """Setup before the Test"""
    def setUp(self):
        self.dojo = Building(office_names, living_space_names, input_file)
        self.allocated_offices, self.office_unallocated \
            = self.dojo.allocate_room(self.dojo.all_employees,
                self.dojo.offices)
        self.allocated_living_spaces, self.ls_unallocated \
            = self.dojo.allocate_room(self.dojo.fellows,
                self.dojo.living_spaces)
        self.dojo.print_office_allocation()
        self.dojo.print_living_space_allocation()


    def test_can_pre_populate(self):
        """
        Test if offices and living space can be prepopulated
        """
        self.assertIsInstance(self.dojo.offices[4], Room)
        self.assertEquals('Shire', self.dojo.offices[4].name)
        self.assertEquals(len(self.dojo.offices), 10)
        self.assertEquals('Rm1', self.dojo.living_spaces[0].name)
        self.assertEquals(len(self.dojo.living_spaces), 10)
        self.assertEquals('<type \'bool\'>',
            str(type(self.dojo.living_spaces[0].is_full())))
        self.assertIsNotNone(self.dojo.offices[6].get_occupants())

    def test_can_access_employees_from_input(self):
        """
        Tests if employee details in input file are accessed and objects created
        """
        self.assertIsNotNone(self.dojo.all_employees)
        self.assertIsInstance(self.dojo.all_employees[0], Person)
        self.assertEquals('<type \'str\'>',
            str(type(self.dojo.all_employees[0].name)))
        self.assertEquals('<type \'bool\'>',
            str(type(self.dojo.all_employees[0].is_allocated_office)))
        self.dojo = Building(office_names, living_space_names, empty_file)
        self.assertEquals(False, self.dojo.access_employees()[0])

    def test_employees_entities_are_valid(self):
        """
        Tests if the types of employees are correct
        the Y or N are taken in for fellow
        """
        self.assertIsInstance(self.dojo.fellows[0], Fellow)
        self.assertEquals('Y', self.dojo.fellows[0].is_interested)

    def test_allocate_room(self):
        """
        Tests if the allocation of room works
        receiving randomized room and randomized person
        """
        self.assertIsNotNone(self.dojo.allocate_room(self.dojo.all_employees,
            self.dojo.offices)[0].keys())
        self.assertIsNotNone(self.dojo.allocate_room(self.dojo.fellows,
            self.dojo.living_spaces)[0].keys())
        self.assertIsInstance(self.dojo.offices[0], Office)
        self.assertIsInstance(self.dojo.living_spaces[0], LivingSpace)

    def test_get_list_of_office_allocations(self):
        """
        Tests if the allocation of Office is okay
        """
        self.assertIsNotNone(self.dojo.get_list_of_office_allocations())

    def test_get_list_of_living_space_allocations(self):
        """
        Tests if the allocation of Living Space is okay
        """
        self.assertIsNotNone(self.dojo.get_list_of_living_space_allocations())

    def test_print_room_allocation(self):
        """
        Tests if the allocation of room is presented in the stipulated format
        """
        self.assertEquals('<type \'list\'>',
            str(type(self.allocated_offices.keys()[:])))
        self.assertEquals('<type \'str\'>',
            str(type(self.allocated_offices.keys()[0])))
        self.assertEquals('<type \'list\'>',
            str(type(self.allocated_living_spaces.keys()[:])))
        self.assertEquals('<type \'str\'>',
            str(type(self.allocated_living_spaces.keys()[0])))
        print self.allocated_living_spaces
        self.assertIsInstance(self.dojo.print_allocation(
            self.allocated_living_spaces)[0], Fellow)
        self.assertIsInstance(self.dojo.print_allocation(
            self.allocated_offices)[0], Person)

    def test_print_unallocated_employees(self):
        """
        Tests if the unallocated employees are appended
        """
        self.assertEquals('<type \'list\'>', str(type(self.office_unallocated)))
        self.assertEquals(self.office_unallocated, [])
        self.assertIsInstance(self.ls_unallocated[0], Fellow)
        self.assertIsNone(self.dojo.print_unallocated_employees())

    def test_allocation_of_one_room(self):
        """
        Tests if Printing Occupants of one room can be accessed to be printed
        """
        self.assertIsInstance(self.allocated_offices["Shire"][0], Person)
        self.assertIsInstance(self.allocated_living_spaces["Rm1"][0], Fellow)
        self.assertEquals('Invalid',
            self.dojo.print_allocation_for_one_room('abcd'))
        self.assertEquals('Office allocated',
            self.dojo.print_allocation_for_one_room('Hogwarts'))
        self.assertEquals('LS allocated',
            self.dojo.print_allocation_for_one_room('Rm1'))


if __name__ == '__main__':
    unittest.main()
