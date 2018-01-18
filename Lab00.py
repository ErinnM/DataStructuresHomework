# Erin Dolecheck
#Lab 00

#Part A
print("Hello World")

#Part B

#Part C
import math
r=int(input("Radius: "))
volume=(4/3)*math.pi*r**2
print(volume)

#Part D
#Can we do more with recursion? I think it's interesting but I'm not completely
#understanding it. 

#Part E
for i in range(3,50):
    if i%2==1:
        if i%3==1 or i%3==2:

            
            print(i)
    #this is not correct yet. It's only checking divisibility by 2 and 3
    #there are still numbers that aren't prime printin
