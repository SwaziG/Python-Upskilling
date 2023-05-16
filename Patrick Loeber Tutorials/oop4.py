# Encapsulation and Abstraction
# Encapsulation - mechanism of hiding data implementation (restrict access to getters and setters)

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None # _x is a "protected" attribute can be accessed from outside, but shouldn't (This is more common to see)
        self.__salary = None # __x is a "private" attribute can not be accessed from outside
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary
    
    # setter
    def set_salary(self, base_value):
        # check value, enforce constraints
        # if base_value < 20000:
        #     self._salary = 20000
        # if base_value > 35000:
        #     self._salary = 35000
        self._salary = self._calculate_salary(base_value)
    
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved <10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

    
se = SoftwareEngineer("Max", 25)
print(se.age, se.name)

for i in range(70):
    se.code()


se.set_salary(30000)
print(se.get_salary())
