'''
We are going to create a software Engineer lis with the following attributes:
position, name, age, level, salary
'''
se1 = ["Software Engineer", "Alfred", 25, "Mid Level", 35000]
se2 = ["Software Engineer", "Alice", 30, "Senior Level", 40000]

'''
Creating a class allows for more complex data systems
'''
# class - a blueprint of the data structure
class SoftwareEngineer: # Using the capital is common practice and convention.
   
   # class attribute - can be used on the class it's self 
   alias = "Keyboard Magician"
   
   def __init__(self, name, age, level, salary): # now that we have given the attributes, we need to make sure that our instance has the correct attributes
      # instance attributes (object) - Are specific to each instance called ie. se1 and se2
      self.name = name
      self.age = age
      self.level = level
      self.salary = salary


# instance of the class
se1 = SoftwareEngineer("Alfred", 25, "Mid Level", 35000)
print(se1.name, se1.age)
se2 = SoftwareEngineer("Alice", 30, "Senior Level", 40000)
