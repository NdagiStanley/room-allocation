"""
    Model for the rooms at Amity
"""
class Room(object):
    """Room represents a Room in Amity"""
    def __init__(self, name, members = []):
        self.name = name
        self.members = members

class Office(Room):
    """Office represents an Office"""
    def __init__(self):
        self.members = [6]

class LivingSpace(Room):
    """LivingSpace represents a LivingSpace"""
    def __init__(self):
        self.members = [4]


"""
    Model for the employees at Amity
"""
class Person(object):
    """Person represents an employee (Fellow and Staff)"""
    def __init__(self, name, OfficeAllocated = False):
        self.name = name
        self.OfficeAllocated = OfficeAllocated

class Staff(Person):
    def check_allocation_status(self):
        #checks status of the Staff in terms of Office allocation
        print "Name : " + self.name + "\t"
        print "Office : "
        if self.OfficeAllocated == False:
            print "NOT ALLOCATED \t"
        else:
            print self.OfficeAllocated + "\t"
    pass

class Fellow(Person):
    def __init__(self, LS_Allocated = False, Interested_in_LS = "N"):
        self.LS_Allocated = LS_Allocated
        self.Interested_in_LS = Interested_in_LS

    def check_allocation_status(self):
        #checks status of the Fellow in terms of Office and Living Space allocation
        print "Name : " + self.name + "\t"
        print "Office : "
        if self.OfficeAllocated == False:
            print "NOT ALLOCATED \t"
        else:
            print self.OfficeAllocated + "\t"
        print "Living Space : "
        if self.LS_Allocated == False:
            print "NOT ALLOCATED \t"
        else:
            print self.LS_Allocated + "\t"
    pass
