#Erin Dolecheck, Lab07
#Stack

class stackItem:
    def __init__(self,value,index):
        self.value=value
        self.index=index
        self.next=None
        self.prev=None
        
class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def add(self,value):
        si=stackItem(value,self.length)
        if self.length==0: self.head=si
        else:
            si.prev=self.tail
            self.tail.next=si
        self.tail=si
        self.length+=1

    def remove(self): #LIFO
        if self.length==0: print("Stack is empty.")
        else: #remove last item in the stack
            self.tail=self.tail.next
            self.length=self.length-1

    def __str__(self):
        out=str(self.head.value)
        x=self.head
        for i in range(self.length-1):
            x=x.next
            out+=", "+str(x.value)
        return out

newStack=Stack()
newStack.remove()
newStack.add(7)
newStack.add(3)
newStack.add(14)
newStack.add(1)
newStack.add(21)
newStack.add(0)
newStack.add(0)
newStack.add(56)
print(newStack)
newStack.remove()
print(newStack)
