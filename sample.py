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

from main.main import Building

living_space_names = ['Rm1', 'Rm2', 'Rm3', 'Rm4', 'Rm5', 'Rm6', 'Rm7', 'Rm8', 'Rm9', 'Rm10']
office_names = ['Hogwarts', 'Valhalla', 'Oculus', 'Krypton', 'Shire', 'Narnia', 'Camelot', 'Mordor', 'Round Table', 'Midgar']

if len(sys.argv) > 1:
    file_name = sys.argv[1]

else:
    file_name = "employees.txt"

if __name__ == '__main__':
    amity = Building(office_names, living_space_names, file_name)
    amity.print_office_allocation()
    amity.print_living_space_allocation()
    amity.print_unallocated_employees()
    amity.print_allocation_for_one_room('Shire')
    amity.print_allocation_for_one_room('Rm1')
