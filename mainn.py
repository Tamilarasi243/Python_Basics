import oddOrEven
import armstrongNum
import primeNum
import fibonacci
import factorialNum
import palindromeNum
import pattern
import diamondPattern

number = int(input("Enter a number between 1 to 300 "))

oddOrEven.oddEven(number)
armstrongNum.armstrongNumber(number)  #153
primeNum.primeNumber(number)
print("fibonacci series")
fibonacci.fibonacciSeries(number)
print("factorial")
factorialNum.factorialNumber(number)
palindromeNum.palindromeNumber(number)
# pattern.semiDiamond(number)
diamondPattern.diamondPattern(number)