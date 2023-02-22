# This is the file where all the scripts will be run

import imagetools
import lcg

def userImage(image):
    
    # Converting image to array then to a number
    myarray = imagetools.GET_NUM_ARRAY(image)
    array_num = lcg.arrayToNum(myarray)
    #print(array_num) 
    # Performing lcg operation on number
    iterations = 5

    #for i in range(iterations):
    #    next = lcg.lcg(lcg.a, 0, lcg.modulo, array_num)
    #    array_num = next

    # Converting new number to array then text
    myarray = lcg.numToArray(array_num, False)

    imagetools.arrayToText(myarray)



def userText(text):
    num_array = imagetools.textToArray(text, 144, 144)
    array_num = lcg.arrayToNum(num_array)
    
    iterations = 5  # (Should be same as the one in the other function)
    
    
    #for i in range(iterations):
    #    next = lcg.reverse_lcg(lcg.a, 0, lcg.modulo, array_num)
    #    array_num = next

    # Converting new number to array then text
    myarray = lcg.numToArray(array_num, True)

    imagetools.arrayToImage(myarray)


userImage("images/duck.jpg")


with open("textfiles/moviescript.txt", 'r') as f:
   userText(f)



