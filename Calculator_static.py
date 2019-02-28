# -*- coding: utf-8 -*-
class Calculator():
    def __init__(self):
        self.result = 0
    
    @staticmethod
    def addition(number1, number2):
        result = number1 + number2
        print("{} + {} \t= {}".format(number1, number2, result))
   
    @staticmethod
    def substraction(number1, number2):
        result = number1 - number2
        print("{} - {} \t= {}".format(number1, number2, result))
 
c = Calculator()
c.addition(100, 99)
c.substraction(120, 2)
