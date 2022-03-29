a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
b=[]
i=0
while i<len(a):
    c=0
    l=[]
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    l.append(a[i])
    l.append(c)
    if l not in b:
        b.append(l)
    i=i+1
print(b)
        
