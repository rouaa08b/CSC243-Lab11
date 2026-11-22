# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 22:37:02 2026

@author: User
"""

class Airlock:
    def __init__(self, code):
        self.code = str(code)
        self.__sealed = False
    def is_sealed(self):
        return self.__sealed
    def __lock_bolts(self):
        print ('Bolts locked.')
    def __unlock_bolts(self):
        print('Bolts unlocked.')
    def seal(self):
        if self.is_sealed() :
            print('Already sealed.')
        else:
            self.__lock_bolts()
            self.__sealed = True
            print('Airlock sealed.')
    def unseal(self):
        if not self.is_sealed() :
            print('Already open.')
        else:
            self.__unlock_bolts()
            self.__sealed = False
            print('Airlock open.')
    def __str__(self):
        if self.__sealed:
            return 'Airlock ' +self.code+': sealed'
        else:
            return 'Airlock ' +self.code+': open'