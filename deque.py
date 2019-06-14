# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 05:07:48 2019

@author: Jiastin
"""
class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
#palindrome checker
from pythonds.basic.deque import Deque
def palChecker(aString):
    charDeque=Deque()
    stillEqual=True
    for ch in aString:
        charDeque.addRear(ch)
    while charDeque.size()>1 and stillEqual:
        first=charDeque.removeFront()
        last=charDeque.removeRear()
        if first!=last:
            stillEqual=False
    return stillEqual
    
