a=[23,14,56,12,19,9,15,25,31]
i=0
count=0
count1=0
while i<len(a):
    if a[i]%2==0:
        count=count+1
    else:
        count1=count1+1
    i=i+1
print("even num",count)
print("odd num",count1)
