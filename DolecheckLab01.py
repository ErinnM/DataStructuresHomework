#Erin Dolecheck
#Lab 01

#Part A FizzBuzz
for i in range(1,11):
    if i%15==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)



#Part C Apples
prices=[14,6,9,7,8,10,3,9]
#prices=[23,54,18,9,43,13,20,12,14,15,25,32,43,40,39,27]
x=len(prices)
profits=[]

for i in range(x-1):
    profit=prices[i+1]-prices[i]
    profits.append(profit)

profits.sort()
y=len(profits)
print("The greatest possible profit is $",profits[y-1],".")



#this won't run and I can't figure out why
#Part B Reading Files        Falling Up by Shel Silverstein
text=open("FallingUp.txt","r")
line=1
for i in text.readlines():
    print(line,i)
    line=line+1




