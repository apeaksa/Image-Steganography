import heapq
from collections import defaultdict

HEADER_SIZE = 54
DELIMITER = "$"

def dec_to_bin(x):
    return int(bin(x)[2:])


class Encrypt(object):
    def __init__(self):
        self.image_byte_counter = 0
        self.new_image_data = ''
        self.original_image = ''
        self.msg= ''

    def open_image(self):
        with open(ImageFile, "rb") as f:
            self.original_image = ''.join(map(chr, f.read()))
    def read_header(self):
        for x in range(0, HEADER_SIZE):
            self.new_image_data += self.original_image[x]
            self.image_byte_counter +=1
    def hide_text_size(self):
         c= len(self.msg)
         asc= str(c)
#        print("*********",c)
         asc += DELIMITER
         self.do_steg(asc)

    def do_steg(self, text):
        for ch in range(0, len(text)+1):
            if ch==0:
#                print("&&&&&&&&&",code[ch])
                g=int(code[ch])/5
#                print("&&&&&&&&&",code[ch])
                current_char=int(g)
            else:
                current_char = int(code[ch],2)
            current_char_binary = '{0:016b}'.format(current_char)
#            c=ord(current_char)
            print("-----",current_char,current_char_binary,alpha[ch])
            
            for bit in range(0, len(current_char_binary)):
                new_byte_binary = ''
                
                current_image_binary = '{0:016b}'.format(ord(self.original_image[self.image_byte_counter]))

                new_byte_binary = current_image_binary[:7]

                new_byte_binary += current_char_binary[bit]

                new_byte = chr(int(new_byte_binary, 2))

                self.new_image_data += new_byte
                self.image_byte_counter += 1
    def copy_rest(self):
        self.new_image_data += self.original_image[self.image_byte_counter:]

    def close_file(self):
        with open(StegImageFile, "wb") as out:
            out.write(bytearray(map(ord, self.new_image_data)))

    def run(self, text):
        self.msg= text
        self.open_image()
        self.read_header()
#        self.hide_text_size()
        self.do_steg(self.msg)
        self.copy_rest()
        self.close_file()

    def hide_(self, Texte, image, encode):
        global TextToHide, ImageFile, StegImageFile
        TextToHide = Texte
        ImageFile = image
        StegImageFile = encode
        stega_instance = Encrypt()
        stega_instance.run(TextToHide)
        


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

data = "we were both young when i first saw you."
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)

code=[]
alpha=[]
x=len(data)
alpha.append(str(x))
x=dec_to_bin(x)
code.append(str(x))
flen=len(frequency)
for l in data:
    for r in range(flen):
        if huff[r][0]==l:
            alpha.append(huff[r][0])
            code.append(huff[r][1])

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

print(code,alpha)
                    
ls=Encrypt();        
ls.hide_(data,"image.jpeg","encoded.jpeg")        
        
 