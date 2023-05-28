"""The functions from pythonpool.

This file is not tested for style to preserve the original code.
https://www.pythonpool.com/check-if-number-is-prime-in-python/
"""

import math

def isprime_1(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def isprime_2(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True

def isprime_3(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0:
        return False
    if num < 9:
        return True
    if num%3 == 0:
        return False
    a = int(num**0.5)
    b = 5
    while b <= a:
        print ('\t',b)
        if num%b == 0:
            return False
        if num%(b+2) == 0:
            return False
        b=b+6
    return True

def isprime_4(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

def isprime_5(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1

def isprime_6(num):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    a=[]
    for i in range (1, num+1):
        if (num/i).is_integer():
            a.append(i)
    if len(a)==2:
        return True
    else:
        return False

def isprime_7(no, i = 2):
    """Determines if a number is prime.

    Not tested for style to preserve the original code.
    Adapted from https://www.pythonpool.com/check-if-number-is-prime-in-python/
    """
    if no == i:
        return True
    elif no % i == 0:
        return False
 
    return isprime_7(no, i + 1)
