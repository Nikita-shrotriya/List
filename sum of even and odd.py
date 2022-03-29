a=[23,14,56,12,19,9,15,25,31]
i=0
sum=0
sum1=0
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
    else:
        sum1=sum1+a[i]
    i=i+1
print("sum of even num=",sum)
print("sum of odd num=",sum1)