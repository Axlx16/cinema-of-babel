from PIL import Image
import numpy as np
import mapping
import time

 # Sets infinite size array
np.set_printoptions(threshold=np.inf)


# Removing Dictionary Parameter
def charToNum(char):
    if char in mapping.mapping_dict:
        return mapping.mapping_dict[char]
    else:
        return 999 

def numToChar(num):
    if num in mapping.inv_mapping_dict:
       return mapping.inv_mapping_dict[num]
    else:
       return "™" # Unmapped character space 


def textToImage(text, width, height):
    full_array_size = 3 * width * height   
    
    # Reading textfile and truancing extra characters
    with open("textfiles/moviescript.txt", 'r') as f:
        text = f.read() 
        text_length = len(text)
        if (text_length > full_array_size):
            text = text[:-(text_length - full_array_size)] 
        else:
            pass
    
    # Converts text from textfile into numpy array 
    image_list = list(text)
    image_array = np.array(image_list)
    
    # Resizing Array to image dimensions
    image_array = np.reshape(image_array, (height, width, 3))
    
    # Applying charToNum() to array
    image_array = np.stack(np.vectorize(charToNum)(image_array), axis=0)
    
    # Converting array and saving image
    im_new = Image.fromarray((image_array).astype(np.int32), mode='RGB')
    im_new = im_new.save("images/imagefromtext.jpg")
    

def GET_NUM_ARRAY(image):
    img = Image.open(image)
    img = img.convert("RGB")
    imgarr = np.array(img)
    return imgarr 
    # Temporary a better way of returning an array should be found
    #with open("textfiles/arrayfromtext.txt", 'w') as f:
       # f.write(str(imgarr))


def arrayToText(imgarr):
    # Opening image and creating numpy array
    #img = Image.open(image)
    #imgarr = np.array(img)
    
    #with open("textfiles/arrayfromtext.txt", 'w') as f:
    #    f.write(str(imgarr))
        
        

    
    # Converting each number and joining them together to create string
    imgarr = np.ravel(imgarr)
    moviescript = ""
    for num in imgarr:
        moviescript += str(numToChar(num))
        
    # Writing string to textfile
    with open("textfiles/moviescript.txt", 'w') as f:
        f.write(moviescript)


if __name__ == "__main__":
    print("[" + str(time.ctime(time.time())) + "]")
    imageToText("images/360p.jpg")
    textToImage("moviescript.txt", 480, 360)
    print("[" + str(time.ctime(time.time())) + "]")
