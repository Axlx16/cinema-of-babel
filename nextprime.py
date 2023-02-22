from math import isqrt
import imgstd
import decimal

decimal.getcontext().prec = 100000000

# n is the number to be check whether it is prime or not
n = imgstd.m_original
 
# this flag maintains status whether the n is prime or not
prime_flag = 1

while (prime_flag == 1):
    if(n > 1):
        for i in range(2, isqrt(n) + 1):
            if (n % i == 0):
                prime_flag = 1
                n+=1
                break
       
        # Condition if n is prime 
        if (prime_flag == 0):
            print(str(n))
    else:
        pass
