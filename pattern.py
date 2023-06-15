def semiDiamond(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print('')
    for i in range(number,1,-1):
        for j in range(1,i):
            print("*",end=" ")
        print('')
semiDiamond(5)