#Lab 04, Parts B and C
#Erin Dolecheck

import time
n=int(input("Enter which Fibonacci number you would like to calculate: "))

#Without Recursion
start=time.clock()
x=y=1
if n<2:
    print("1")
else:
    for i in range(n-1):
        fib=x+y
        x=y
        y=fib
    print(x)
end=time.clock()
wor=end-start       #wor-without recursion
print(wor, "seconds without recursion.")

#With Recursion
def fibrecursion(n):
    if n<2:
        return(1)
    else:
        return fibrecursion(n-1)+fibrecursion(n-2)
    
start2=time.clock()
print(fibrecursion(n-1))
end2=time.clock()
wr=end2-start2      #wr-with recursion
print(wr, "seconds with recursion.")

#Dynamic Programming 
key=[1,1]
for i in range(n):
    key.append(0)
def fibdynamic(n):
    if key[n]==0:
        key[n]=fibdynamic(n-1)+fibdynamic(n-2)
    return key[n]

start3=time.clock()
print(fibdynamic(n-1))
end3=time.clock()
wdp=end3-start3     #wdp-with dynamic programming
print(wdp, "seconds with dynamic programming.")

#Which is fastest?
if wor<wr and wor<wdp:
    print('Without recursion is fastest.')
if wr<wor and wr<wdp:
    print('Recursion is fastest.')
else:
    print("Dynamic programming is fastest.")

