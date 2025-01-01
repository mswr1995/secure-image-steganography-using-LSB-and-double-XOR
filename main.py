import sys
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

def encryptDecrypt(inpString):
    # Define XOR key
    # Any character value will work
    xorKey = 'A';

    # calculate length of input string
    length = len(inpString);

    # perform XOR operation of key
    # with every caracter in string
    for i in range(length):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:]);
        print(inpString[i], end="");


    return inpString;

def encryptDecrypt2(inpString):
    # Define XOR key
    # Any character value will work
    xorKey = 'B';

    # calculate length of input string
    length = len(inpString);

    # perform XOR operation of key
    # with every caracter in string
    for i in range(length):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:]);
        print(inpString[i], end="");


    return inpString;

# encryptDecrypt("Musawer")
# encryptDecrypt(encryptDecrypt2("musawer"))

#encoding function
def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
        m = 0
    elif img.mode == 'RGBA':
        n = 4
        m = 1

    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(m, n):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")


#decoding function
def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
        m = 0
    elif img.mode == 'RGBA':
        n = 4
        m = 1

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(m, n):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        # print("Hidden Message:", message[:-5])
        print(encryptDecrypt2(encryptDecrypt(message[:-5])))
    else:
        print("No Hidden Message Found")

# Encode("lena.png", encryptDecrypt2(encryptDecrypt("selam")), "lena2.png")
# Decode("lena2.png")