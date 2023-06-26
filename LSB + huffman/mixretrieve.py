import binascii

HEADER_SIZE = 54
DELIMITER = "$"

def dec_to_bin(x):
    return int(bin(x)[2:])

class Decrypter:
    def __init__(self):
        self.StegImageFile = ''
        # self.fh = open(StegImageFile, 'rb')
        self.number_of_chars_in_text = 0
        self.original_text = ''

    def read_header(self):
        self.fh = open(StegImageFile, 'rb')
        for i in range(0, HEADER_SIZE):
            byte = self.fh.read(1)

    def get_char(self,ch):
        new_byte = ''

        for bit in range(0, 16):
            byte = self.fh.read(1)
            new_byte += str(ord(byte) & 0x01)

        
#        print("*****",new_byte)
        if ch==0:
            n = int(new_byte, 2)
#            print('&&&&&&&&&&&',n)
            c=str(n*5)
#            print('&&&&&&&&&&&',c)
            c=int(c,2)
#            print('&&&&&&&&&&&',c)
            return c
        else:
             a=int(new_byte)
            
             for i in range(len(code)):
                 if a == int(code[i]):
                     print(a,code[i],alpha[i])
                     return alpha[i]
                
                 
            

    def get_text_size(self):
        txt_len = self.get_char(0)
        self.number_of_chars_in_text = txt_len
#        print(txt_len)

    def read_stega_text(self):
        decoded_chars = 0;
        while decoded_chars < self.number_of_chars_in_text:
#            print("yoooooooo")
            self.original_text += self.get_char(1)
            decoded_chars += 1

    def close_file(self):
        self.fh.close();

    def get_text(self):
        self.read_header()
        self.get_text_size()
        self.read_stega_text()
        self.close_file()
        return self.original_text

    def reveal_(self, stego):
        global StegImageFile
        StegImageFile = stego
        dec_instance = Decrypter()
        text = dec_instance.get_text()
        print ("Hidden text is:",text)

        
ch=0      
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
 
ls=Decrypter();         
ls.reveal_("encoded.jpeg")  