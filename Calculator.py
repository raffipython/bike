# -*- coding: utf-8 -*-
class Calculator():
    def __init__(self):
        self.result = 0
        self.iteration = 1
        
    def addition(self, number):
        self.result = self.result + number
    
    def substraction(self, number):
        self.result = self.result - number 
        
c = Calculator()
print(c.result)

c.addition(100)
print(c.result)

c.substraction(1)
print(c.result)
