def printprimenumbers(n):
    for x in range(2,n):
        primenumber=True
        for j in range(2,x):
            if x%j==0:
                primenumber=False
                break
        if primenumber:
            print(x)

printprimenumbers(20)




	
