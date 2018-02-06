#Erin Dolecheck

#Lab 02/03 in class 2/2, 2/5

import random
import time
names=["joey", "bobby","sueann","loretta","grant","jenny","billy","cletus",\
       "hunter","gunner","rose","tucker","amy","charlotte","duke","ricky",\
       "bo","luke","jesse"]
 
waitingRoom=[]
triageRoom=[]
examRoom=[]
examRoomSize=6
doctors=6

def callNurse():
    """move patients from waiting to triage"""
    triageRoom.append(waitingRoom.pop(0))
    #sort(triageRoom,key=patient.triageNumer)
    

class Patient:
    def __init__(self):
        self.triageNumber=random.randrange(0,100)
        #self.name=names[random.randInt(0,len(names)-1)]+ " "+\
 #                  names[random.randInt(0,len(names)-1)]
        self.arrivalTime=time.clock
        self.treatmentTime=random.randrange(15,20)
    def exit(self):
        #remove patient from simulation
        pass

def main():
    p=Patient()
    waitingRoom.append(p)
    
    #do this when a new patient enters
    callNurse()
    doctors=6
    triageOrder=[]
    
    for i in range(len(waitingRoom)):
         if doctors==0:
            triageOrder.append(p.triageNumber)
            triageOrder.sort() #this will contain patients still waiting to see
            print(triageOrder) #a doctor, sorted least urgent to most urgent
            
         if doctors>=1:
            #want to check the highest triage number in the list against new
            #patients triage number
            a=len(triageOrder)
            if triageOrder[a-1]>=p.triageNumber:
                #old patient sees doctor
                doctors=doctors-1
            else: #new patient sees doctor
                examRoom.append(triageRoom.pop(0))
                doctors=doctors-1
       
    
    
    print(waitingRoom)
    print(triageRoom)
    

main()
