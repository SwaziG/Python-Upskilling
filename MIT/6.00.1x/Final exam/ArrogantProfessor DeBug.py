# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:46:18 2022

@author: Mikey_I_G
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff):         
        return 'It is obvious that ' + Person.say(self, stuff)
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')


print(ae.say('the sky is blue'))
#eric says: It is obvious that eric says: the sky is blue

print(ae.lecture('the sky is blue'))
#It is obvious that eric says: the sky is blue