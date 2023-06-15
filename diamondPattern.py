def diamondPattern(number):
    for i in range(0,number):
        for j in range(0,number-i-1):
            print(end=" ")
        for k in range(0,i+1):
            print("* ",end="")
        print('')


    for i in range(number-1,0,-1):
        k=i
        for j in range(k,number-1,1):
            print(end=" ")
            k=k+1
        for j in range(0,i,1):
            print(" *",end="")
        print('')
    
