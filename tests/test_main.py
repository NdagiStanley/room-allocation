import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from main import Building

class Test(unittest.TestCase):
    """docstring for ClassName"""

    def test_pre_populate(self):
        """
        Test if offices and living space can be prepopulated
        """
        self.amity = Building()
        self.assertEquals('Shire', self.amity.offices[4].name)
        self.assertEquals(len(self.amity.offices), 10)
        self.assertEquals('Rm1', self.amity.living_spaces[0].name)
        self.assertEquals(len(self.amity.living_spaces), 10)

if __name__ == '__main__':
    unittest.main()