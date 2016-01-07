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
    print amity.living_spaces
    print amity.offices