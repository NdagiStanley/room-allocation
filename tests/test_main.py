import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from main import Building
from model import Person, Staff, Office, LivingSpace

class Test(unittest.TestCase):
    """docstring for ClassName"""
    amity = Building()

    def test_can_pre_populate(self):
        """
        Test if offices and living space can be prepopulated
        """
        self.assertEquals('Shire', self.amity.offices[4].name)
        self.assertEquals(len(self.amity.offices), 10)
        self.assertEquals('Rm1', self.amity.living_spaces[0].name)
        self.assertEquals(len(self.amity.living_spaces), 10)

    # def test_is_printing_details(self):
    #     """
    #     Test if Room details are being printed
    #     """
    #     pass

    def test_can_access_employees_from_input(self):
        """
        Tests if employee details in input file are accessed and objects created
        """
        self.assertIsNotNone(self.amity.employee)
        self.assertIsInstance(self.amity.employee[0], Person)
        self.assertEqual('<type \'str\'>', str(type(self.amity.employee[0].name)))


    def test_employees_entities_are_valid(self):
    	"""
    	Tests if the types of employees are correct the Y or N are taken in for fellow
    	"""
    	self.assertIsInstance(self.amity.staff[0], Staff)
        self.assertEqual('N' or 'Y', self.amity.fellow[0].is_interested)


    def test_allocate_room(self):
    	"""
        Tests if the allocation of room works receiving randomized room and randomized person
    	"""
    	self.assertIsNotNone(self.amity.allocate_room(self.amity.employee, self.amity.offices).keys())
    	self.assertIsInstance(self.amity.offices[0], Office)
    	self.assertIsInstance(self.amity.living_spaces[0], LivingSpace)

     #    self.assertEqual('N' or 'Y', self.amity.fellow[0].is_interested)




if __name__ == '__main__':
    unittest.main()