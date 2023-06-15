def nPrimeNumber(number):
    #print(2,end=" ")
    flagg=0
    for i in range(2,number+1):
        for j in range(2,int(i/2)):
            if i%j==0:
                flagg=1
                break
        if flagg==0:
            print(i,end=" ")

nPrimeNumber(10)