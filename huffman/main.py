from PIL import Image
import heapq
from collections import defaultdict


def dec_to_bin(x):
    return int(bin(x)[2:])


def encode_image(img, msg):
    length = len(msg)

    if length > 255:
        print("text too long! (don't exceed 255 characters)")
        return False
    
    if img.mode != 'RGBA':
        print("image mode needs to be RGB")
        return False
    

    encoded = img.copy()
    width, height = img.size
    index = 0
    d=0
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            # first value is length of msg
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                    asc=int(code[d],2)
                    print("1__",asc,alpha[d])
                    d +=1
            else:
                asc = r
#                if d==0:
#                    print(asc,row,col)
#                    d+=1
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded


def decode_image(img):
   
    width, height = img.size
    msg = ""
    index = 0
    hufflen=len(code)
#    print("**&&&&***",hufflen)
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            
            if row == 0 and col == 0:
                length = r
            elif index <= length:
#                print(r)
                d=dec_to_bin(r)
#                print("*******",d)
                for i in range(hufflen):
                    if int(code[i])==d:
                        t= ord(alpha[i])
#                        print("aaaaaaaaa")
                        msg +=chr(t)
                        break
            index += 1
    return msg




def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return heapq.heappop(heap)[1:]


data = "wakanda forever!"
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
#print ("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")

code=[]
alpha=[]
flen=len(frequency)
for l in data:
    for r in range(flen):
        if huff[r][0]==l:
            alpha.append(huff[r][0])
            code.append(huff[r][1])
 
#print(code,alpha)
#for i in range(len(code)):
#    d=int(code[i],2)
#    print(d)

           
for i in range(len(code)):
    for j in range(len(code)):
        if i!=j:
          
            if int(code[i])==int(code[j]):
#                    print('&&&&&',code[i],code[j],alpha[i],alpha[j])
                    if alpha[i]!=alpha[j]:
#                        print("&&")
                        c=int(code[i],2)
                        c=c*5
                        print(c)
                        c=dec_to_bin(c)
                        print(code[i])
                        code[j]=str(c)
#                        print("********",code[j])
                       
            
        
        
#print(alpha)
#for i in range(len(code)):
#    d=int(code[i],2)
#    print(d,code[i])

#bi=[]
#
#for i in range(len(code)):
#    c=int(code[i])
#    decimal = int(code[i], 2);
#    bi.append(decimal)
#    
#print(bi)

#print(huff)
#for i in range(len(code)):
#    print(alpha[i],code[i])
    
original_image_file = "image.png"

img = Image.open(original_image_file)

print(img, img.mode,img.size)  

encoded_image_file = "enc_" + original_image_file


print(len(data))     
    

img_encoded = encode_image(img, data)



if img_encoded:
    
    img_encoded.save(encoded_image_file)
    print(encoded_image_file,"saved!!\n")
    
    
    import os
    os.startfile(encoded_image_file)
    




encoded_image_file = "enc_image.png"

img2 = Image.open(encoded_image_file)
hidden_text = decode_image(img2)
print("Hidden text:\n",hidden_text)


