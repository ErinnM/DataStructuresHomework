#Lab 02 class 2/2, 2/5

import random
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
    sort(triageRoom,key=patient.triageNumer)
    

class Patient:
    def __init__(self):
        self.triageNumber=random.randInt(0,100)
        self.name=names[random.randInt(0,len(names)-1)]+ " "+\
                   names[random.randInt(0,len(names)-1)]
        self.arrivalTime=time
        self.treatmentTime random.randrange(15,20)
    def exit(self):
        #remove patient from simulation
        pass
