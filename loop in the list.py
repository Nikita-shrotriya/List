#Loop Through a List
a=["nikki","rani","aayu","himmi"]
for i in a:
    print(i)

#Loop Through the Index Numbers
a=["nikki","rani","aayu","himmi"]
for i in range(len(a)):
    print(a[i])

#using a while loop
a=["nikki","rani","aayu","himmi"]
i=0
while i<len(a):
    print(a[i])
    i=i+1

#Looping Using List Comprehension
a=["nikki","rani","aayu","himmi"]
[print(i) for i in a]