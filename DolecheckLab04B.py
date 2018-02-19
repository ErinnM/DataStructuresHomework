#Lab 04, Part B
#Erin Dolecheck

#Without Recursion

import time

n=int(input("Enter which Fibonacci number you would like to calculate: "))
start=time.clock()
x=1
y=1
if n<2:
    print("1")
else:
    for i in range(n-1):
        fib=x+y
        x=y
        y=fib
    print(fib)
end=time.clock()
wor=end-start
print(wor, "seconds without recursion.")

#With Recursion

def fib(n):
    if n<2:
        return(1)
    else:
        return fib(n-1)+fib(n-2)
    
start2=time.clock()
print(fib(n-1))
end2=time.clock()
wr=end2-start2
print(wr, "seconds with recursion.")

if wor<wr:
    print('Without recursion is faster.')
else:
    print('With recursion is faster.')

#Dynamic Programming 
#I've been researching what this means, but I still don't completely understand
