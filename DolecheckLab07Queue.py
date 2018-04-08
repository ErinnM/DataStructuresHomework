#Erin Dolecheck, Lab07
#Queue

class queueItem:
    def __init__(self, value, index):
        self.value=value
        self.index=index
        self.next=None
        self.prev=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def add(self, value):
        qi=queueItem(value, self.length)

        if self.length==0: self.head=qi
        else:
            qi.prev=self.tail
            self.tail.next=qi

        self.tail=qi
        self.length+=1

    def remove(self): #FIFO
        if self.length==0: print("Queue is empty.")
        else: #remove first item in queue
            self.head=self.head.next
            self.length=self.length-1

    def __str__(self):
        out=str(self.head.value)
        x=self.head
        for i in range(self.length-1):
            x=x.next
            out+=", "+str(x.value)
        return out


newQueue=Queue()
newQueue.remove()
newQueue.add(7)
newQueue.add(3)
newQueue.add(14)
newQueue.add(1)
newQueue.add(21)
newQueue.add(0)
newQueue.add(0)
newQueue.add(56)
print(newQueue)
newQueue.remove()
print(newQueue)
