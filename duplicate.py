a=[5,4,3,5,6,7,8,9,5,6,7,4]
l=[]
for i in a:
    if a[i] not in l:
        l.append(a[i])
print(l)