# !/usr/bin/python
# title          :main.py
# description    :Allocates persons to rooms in a building
# author         :Stanley Ndagi
# email          :stanley.ndagi@andela.com
# date           :20160108
# version        :0.0.1
# python_version :2.7.10
# ==============================================================================
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
    amity.print_room_allocation()
