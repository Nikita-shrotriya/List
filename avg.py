marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,89]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+(marks[i][j])
        average=sum//5
        j=j+1
print("average of",i+1,"year",average)