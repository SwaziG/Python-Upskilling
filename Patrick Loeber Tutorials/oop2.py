'''
We are going to create a software Engineer lis with the following attributes:
position, name, age, level, salary
'''
se1 = ["Software Engineer", "Alfred", 25, "Mid Level", 35000]
se2 = ["Software Engineer", "Alice", 30, "Senior Level", 40000]
d1 = ["Designer","Phillip"]

##def code(se):
   ##print(f"{se[1]} is writing code...")

## code(se1) # this will print that Alfred is writing code
## code(d1) # this will print that Phillip is writing code, which should not be possible as he is a designer...

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
    
    # instance method | Have to write "self"
   def code(self):
      print(f"{self.name} is writing code...")

   def code_in_language(self, language):
      print(f"{self.name} is writing code in {language}...")

   def information(self): # this function has to be called to show the defined information
      information = f"name = {self.name}, age = {self.age}, level = {self.level}"
      return information
   # dunder method string printing
   def __str__(self): # this method allows us to print by just using the object name
      information = f"name = {self.name}, age = {self.age}, level = {self.level}"
      return information
   # dunder method to define what "==" checks
   def __eq__(self, other): # compares two objects
      return self.name == other.name and self.age == other.age

   @staticmethod # decorator - that de-links the self. portion of the class
   def entry_salary(age): # due to the lack of "self" this can only be used as a class attribute as age is already defined
      # this can be over ridden by @staticmethod.
      if age < 25:
         return 25000
      if age < 30:
         return 35000


# instance of the class
se1 = SoftwareEngineer("Alfred", 25, "Mid Level", 35000)
## print(se1.name, se1.age)
se2 = SoftwareEngineer("Alice", 30, "Senior Level", 40000)
## print(se2.name, se2.age)


## se1.code()
## se2.code()
## se1.code_in_language("Python")
## se2.code_in_language("C++")

## print(se1.information()) # Uses information function
## print(se2) # Uses the __str__ function, but doesn't need to be called if it is defined in the class

se3 = SoftwareEngineer("Alice", 30, "Senior Level", 40000) # same as se2 except different memory location

## print(se2 == se3) # will return false due to memory location, unless __eq__ is defined in class

## se1.entry_salary(24) # This is not possible as the function believes that two attributes are given, the 25 that was defined earlier and the 24 defined now

# What we can do is this:
print(SoftwareEngineer.entry_salary(28))

print(se1.entry_salary(24)) # with the @staticmethod, this prints