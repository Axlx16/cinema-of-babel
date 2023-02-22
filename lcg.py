# YOU ARE CURRENTLY GETTING AN ERROR BECAUSE YOU ARE NOT MULITPLYING BY 3 SOMEWHERE
# PROBLEM FOR HAVING NUMBERS OVER 255 IN THE SCRAMBILING PROCESS

# IMPORTANT: https://stackoverflow.com/questions/2911432/reversible-pseudo-random-sequence-generator import image
import numpy as np
import math
import imgstd
import imagetools

def getDigits(num):
    # Potential for floating point error? First number is max of 255 so it shouldn't be an issue
    return math.trunc(math.log10(num))


def arrayToNum(array):
    # For each element in array that is not 3 digits in length add 0's in front
    # This means adding the appriate amount of 0's to the num before it
    # In function that converts the number back to an image we need TO MAKE SURE THAT THE LENGTH OF THE FIRST NUMBER IS ACCOUNTED FOR
    
      
    # Numpy defaults to uint 8 (0,255) so to avoid overflow make it 32 bit integer
    array.astype(np.int32)
    array = array + 1
    array = array.ravel()
    
    for i in range(array.size):
        #print(str(i))
        #print(array[i])
        elem_digits = getDigits(array[i])  #math.trunc(math.log10(array[i]))
        if i > 0 and (elem_digits == 2):
           pass
        elif i > 0 and (elem_digits == 1):
            array[i-1] = int(array[i-1]) * 10

        elif i > 0 and (elem_digits == 0):
            array[i-1] = int(array[i-1]) * 100
        else:
            # SHOULD ONLY PRINT FOR FIRST NUMBER IN ARRAY
            #print("Invalid value in array")
            pass

    combined_num = int(''.join([str(x) for x in array.tolist()]))
    return combined_num
    # RUN THIS THROUGH THE LCG WITH THE m and a VARAIBLES SET TO THE CORRECT Values
    # THEN PROCESS THE NUMBER IN GROUPS OF 3 AND RETURN THE ARRAY BACK TO THE IMAGE CREATOR
            
    
def numToArray(num, modulo):
    

    str_num = str(num)
    
    num_zeros = (3 - len(str_num) % 3) % 3

    str_num = ((num_zeros - 1) * '0') + str_num # LOGIC IS WRONG FIX TEMP FIX FOR JUST DUCK.JPG
    
    
    chunks = [int(''.join(str_num[i:i+3])) for i in range(0, len(str_num), 3)]
    arr = np.array(chunks, dtype=int)
    
    ## Doesn't work because the array has some extra digits added to it which we first need to remove
    ## Likely you still need to the math thing to find out how much you need to remove
    #chars = list(str(num))
    #
    ## Pad with zeros if necessary to make length a multiple of 3
    #num_zeros = (3 - len(chars) % 3) % 3
    #

    #for i in range(num_zeros):
    #    chars = chars.insert(0, ['0'])
    #
    ## Split into chunks of 3 and convert to NumPy array of integers
    #chunks = [int(''.join(chars[i:i+3])) for i in range(0, len(chars), 3)]
    #arr = np.array(chunks, dtype=int)
    
    # Resizing array
    arr = np.reshape(arr, (144, 144, 3))
    arr = arr - 1
    if (modulo == True):
        arr = arr % 256
    return arr


# This is for the "forward" direction of passing the image
def lcg(a, c, m, x): 
    x0 = (a * x + c) % m 
    return x0


# Extended euclidean algorithm that will be used for reversing the lcg
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y


# This is for the backwards direction of making the text to an image
def reverse_lcg(a, c, m, x):
    gcd, v, w = gcdExtended(a,m)
    new_x = (x * v) % m
    return new_x

# EVERYTHING BELOW THIS SHOULD NOT BE RUN IN THIS FILE' 

## Running the lcg function
#
## Fixed Values for a and c
## Using c = 0 appraoch
## IMPORTANT THAT a MUST BE PRIME AND NOT DIVISIBLE BY M SO THAT THEIR GCD == 1
modulo = imgstd.m # Returns modulo from textfile
a = 1063 # For now a is just a random prime number (you can experiment with this) 
c = 0 # modulo & c are relatively prime
#x = arrayToNum()
#
#
#for i in range(8):
#    prev = lcg(a,c,modulo,x)
#    x = prev
#
## Might have to be moduloed at the end
#for i in range(8):
#    next = reverse_lcg(a, c, modulo, x)
#    x = next
#
#
##print(image.GET_NUM_ARRAY("images/duck.jpg"))
#print(numToArray(x))
