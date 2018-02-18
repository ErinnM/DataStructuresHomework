#lab 04, part A
#Erin Dolecheck

#Collatz Conjecture
#Even - divide by 2
#Odd - multiply by 3, add 1

#Without Recursion
x=int(input("Enter a positive integer: "))
n=0
while True:
    if x%2==0:
        x=x/2
        #print(x)
        n=n+1
    else:
        x=(3*x)+1
        #print(x)
        n=n+1
    if x==1:
        print(n, "steps")
        break

#With Recursion

def collatzSteps(n):
    global z
    for i in range(n):
        if n==1:
            return(z)
            break
        else:
            z=z+1
            if n%2==0:
                return collatzSteps(int(n/2))
            else:
                return collatzSteps(int((n*3)+1))
    

n=int(input("Enter a positive integer: "))
global z
z=0
print(collatzSteps(n), "steps")

