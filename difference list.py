list1=[1,2,4,6,7]
list2=[1,4,3,5,6]
a=[]
i=0
while i<len(list1):
    if i in list2:
        pass
    else:
        a.append(i)
    i=i+1
print(a)