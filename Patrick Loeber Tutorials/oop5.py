class SoftwareEngineer:
    def __init__(self):
        self._salary = None # _x is a "protected" attribute can be accessed from outside, but shouldn't (This is more common to see)

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value
    
    @salary.deleter
    def salary(self):
        del self._salary 

se = SoftwareEngineer()
se.salary = 30000
print(se.salary)
del se.salary
print(se.salary)