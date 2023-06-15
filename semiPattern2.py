def semipattern2(number):
    k=2*number-2
    for i in range(0,number):
        
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for k in range(0,i+1):
            print("* ",end="")
        print('')

semipattern2(5)