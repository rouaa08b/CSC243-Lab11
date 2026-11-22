# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:38:26 2026

@author: User
"""
class ScubaTank:
    def __init__ (self, label, bar):
        self.label = label
        self.__bar = bar
    def get_bar(self):
        return self.__bar
    def set_bar(self, bar):
        if self.__bar >= 0 and self.__bar<= 300 :
            self.__bar = bar 
        else :
            print('Invalid presssure.')
    def fill(self, amount):
       if amount>0 :
           self.__bar += amount
       else:
            print('Invalid amount')
    def release(self, amount):
        if amount<= 0 :
            print('Invalid amount.')
        elif amount > self.__bar :
            print('Not enough air.')
        else :
            self.__bar -= amount
    def __str__(self):
        return "Tank "+str(self.label)+": " + str(self.__bar) + " bar" 
        
def transfer_air(source, target, amount) :
    sc = source.get_bar()
    source.release(amount)
    if sc != source.get_bar() :
        target.fill(amount)
    
      

