# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:44:12 2026

@author: User
"""

import Point
class Rectangle:
    def __init__(self, p,q):
        assert type(p) == Point and type(q)== Point, 'Bad input!'
        assert p.x <= q.x and p.y <= q.y, 'Bad input!'
        self.q = q
        self.p = p 
    def __str__(self):
        return "(p= " + str(self.p) + ", q=" + str(self.q) + ")"
    def get_width(self):
        return self.q.x - self.p.x
    def get_height(self):
        return self.q.y - self.p.y 
    def perimeter(self):
        return 2*(self.get_width() + self.get_height())
    def area(self):
        return self.get_width()*self.get_height()
    def contains(self, pt):
        assert type(pt) == Point , 'Bad Input!'
        if pt.x >= self.p.x and pt.x <= self.q.x and pt.y >= self.p.y and pt.y <= self.q.y:
            return True
        else :
            return False

