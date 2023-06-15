def palindromeNumber(number):
    n=number
    reverseNum=""
    while number!=0:
        result=number%10
        reverseNum=reverseNum+str(result)+""
        number = int(number/10)

    if n==int(reverseNum):
        print(n," is Palindrome")
    else:
        print(n," not a Palindrome")

palindromeNumber(121)
