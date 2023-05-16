
# inherits, extends, overrides
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, level, salary): # overrides the parent class
        super().__init__(name, age, salary) # Super allows us to use the __init__ from the parent class
        self.level = level
    
        def work(self):
            print(f"{self.name} is programming...")

    def debug(self):
        print(f"{self.name} is debugging...")
        


class Designer(Employee):
    
    def draw(self):
        print(f"{self.name} is drawing...")
    
    def work(self):
            print(f"{self.name} is designing...")



## se = SoftwareEngineer() # This will give an error as the SoftwareEngineering class has inherited the __init__ function from the parent class Employee...
se = SoftwareEngineer("Max", 25,"Junior",25000)
##    print(se.name, se.age)

d = Designer("Nancy", 31, 21000)
##    print(d.name, d.age)

## se.work()
## d.work()
## d.draw()
## se.debug()

# polymorphism

employees = [SoftwareEngineer("Max", 25,"Junior",25000),SoftwareEngineer("Tiff", 30,"Senior",35000),Designer("Nancy", 31, 21000)]



def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)