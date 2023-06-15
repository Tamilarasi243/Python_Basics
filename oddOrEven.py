def oddEven(number):
    if number%2==0:
        print(number, " Even number")
    else:
        print(number," Odd number")



'''
Traceback (most recent call last):
  File "d:\python\CollegeInfoSystem\mainnFun.py", line 1, in <module>
    from CollegeInfoSystem.Admission import Details
ModuleNotFoundError: No module named 'CollegeInfoSystem'
PS D:\python> & "C:/Program Files/Python311/python.exe" d:/python/CollegeInfoSystem/mainnFun.py
Traceback (most recent call last):
  File "d:\python\CollegeInfoSystem\mainnFun.py", line 2, in <module>
    from FeesDetails import Fees
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "d:\python\CollegeInfoSystem\FeesDetails.py", line 1, in <module>
    from .Admission import Details
ImportError: attempted relative import with no known parent package
PS D:\python> 
'''