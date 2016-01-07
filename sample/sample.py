import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import Building

if __name__ == '__main__':
    amity = Building()
    print amity.living_spaces[2].name
    print amity.offices[1].name
    # print amity.rooms()
    print amity.employee[1].name
    print amity.staff[2].name
    print str(type(amity.fellow[3].name))
    print amity.fellow[4].is_interested
