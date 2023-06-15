def fibonacciSeries(number):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(1,number+1):
        temp=a+b
        a=b
        b=temp
        if(temp<=number):
            print(temp,end=" ")

    print()