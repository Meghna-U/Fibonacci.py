n=int(input("Enter how many terms of fibonacci series: "))
i=1
a1=0
a2=1
print(a1)
print(a2)
while i<=n-2:
    sum=a1+a2
    print(sum)
    a1=a2
    a2=sum
    i+=1
    
