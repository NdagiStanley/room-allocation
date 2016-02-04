"""
    Model for the employees at Amity
"""
class Person(object):
    """Person represents an employee (Fellow and Staff)"""
    def __init__(self, name): #Every person has a name
        self.name = name
        self.is_allocated_office = False

class Staff(Person):
    """Staff is a Person"""
    def __init__(self, name):
        super(Staff, self).__init__(name)

class Fellow(Person):
    """Fellow is a Person"""
    def __init__(self, name, is_interested): #Either Y or N (to be read from file)
        super(Fellow, self).__init__(name)
        self.is_interested = is_interested
