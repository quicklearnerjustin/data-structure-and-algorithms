# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 05:17:28 2019

@author: Jiastin
"""


class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def nextData(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

#Unordered lists
class UnorderedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        count=0
        current=self.head
        while current!=None:
            count=count+1
            current=current.getNext()
    def search(self,item):
        current=self.head
        Found=False
        while not Found and current!=None:
            if current.getData()==item:
                Found=True
            else:
                current=current.getNext()
        return Found
    def remove(self,item):
        current=self.head
        previous=None
        Found=False
        while not Found: #find the item
            if current.getData()==item:
                Found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None: #if the item is the first item
            self.head=current.getNext() #make the second item the head
        else: #if the item is in the middle
            previous.setNext(current.getNext()) #directly connect the previous item to the following

#ordered list
class OrderedList: #the numbers are increasing
    def __init__(self):
        self.head=None
    def search(self,item):
        current=self.head
        Found=False
        Stop=False
        while current!=None and not Found and not Stop:
            if current.getData()==item:
                Found=True
            else:
                if item<current.getData():
                    Stop=True
                else:
                    current=current.getNext()
        return Found
    def add(self,item):
        Stop=False
        current=self.head
        previous=None
        #find the position
        while current!=None and not Stop: 
            if current.getData()>=item:
                Stop=True
            else:
                previous=current
                current=current.getNext()
        #insert the item
        temp=Node(item) 
        if previous==None: #if the item is inserted at front
            temp.setNext(self.head) #make the head the second
            self.head=temp #make the item the head
        else: #if the item is inserted in the middle
            temp.setNext(current) #connect the item to the following item
            previous.setNext(temp) #connect the previous item to the item
                
                
        