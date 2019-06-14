# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:28:59 2019

@author: Jiastin
"""
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(item):
        self.items.insert(0,item)
    def dequeue():
        return self.items.pop()
    def size():
        return len(self.items)
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.isEmpty()
q.enqueue(8.4)
q.dequeue()
q.dequeue()
q.size()

from pythonds.basic.queue import Queue

player=['Aaron','Drew','Russel','Ben','Patrick','Eli']
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name) #move the names from the list to the queue

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue() #person eliminated

    return simqueue.dequeue() #person from whom the game restarts

print(hotPotato(player,7))

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0
    #decide if the printer is working    
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    #decide if the printer has work to do
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate
    #decide how the printer works
    def tick(self):
        if currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                currentTask=None
import random
class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currentTime):
        return currentTime-self.timestamp
from pythonds.basic.queue import queue
def simulation(numSeconds,pagesPerMinute):
    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]
    for currentSecond in range(numSeconds):
        if newPrintTask(): 
            task=Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):#There is new task when the printer is not busy
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f seconds %3d tasks remaining."%(averageWait, printQueue.size()))
def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
for i in range(10):
    simulation(3600,5)
    


        
