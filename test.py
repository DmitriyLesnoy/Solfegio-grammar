A=[8,3,6,2,4,9,5,7,1,]

for j in range((len(A)-1)):
    for i in range((len(A)-1)):
        if A[i]>A[i+1]:
            x=A[i]
            A[i]=A[i+1]
            A[i+1]=x


print(A)
