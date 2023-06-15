def primeNumber(number):
    if number==0 or number==1:
        print(number," not a Prime")
    elif number==2:
        print(number," is a Prime")
    else:
        flagg=0
        for i in range(2,int(number/2)):
            if number%i==0:
                flagg += 1
                break
        if flagg==0:
            print(number," is a Prime")
        else:
            print(number," is not a prime")


