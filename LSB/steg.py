# Consts
HEADER_SIZE = 54
DELIMITER = "$"



class LSBEncrypter(object):
    def __init__(self):
        self.image_byte_counter = 0
        self.new_image_data = ''
        self.original_image = ''
        self.msg = ''

    def open_image(self):
        with open(ImageFile, "rb") as f:
            self.original_image = ''.join(map(chr, f.read()))
    def read_header(self):
        for x in range(0, HEADER_SIZE):
            self.new_image_data += self.original_image[x]
            self.image_byte_counter +=1
    def hide_text_size(self):
        sz = len(self.msg)
        s_sz = str(sz)
        s_sz += DELIMITER
        self.do_steg(s_sz)

    def do_steg(self, steg_text):
        for ch in range(0, len(steg_text)):

            current_char = steg_text[ch]
            current_char_binary = '{0:08b}'.format(ord(current_char))
#            c=ord(current_char)
#            print("-----",current_char,c,current_char_binary)
            for bit in range(0, len(current_char_binary)):
                new_byte_binary = ''
                
                current_image_binary = '{0:08b}'.format(ord(self.original_image[self.image_byte_counter]))

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

    def run(self, stega_text):
        self.msg = stega_text
        self.open_image()
        self.read_header()
        self.hide_text_size()
        self.do_steg(self.msg)
        self.copy_rest()
        self.close_file()

    def hide_(self, Texte, image, steg):
        global TextToHide, ImageFile, StegImageFile
        TextToHide = Texte
        ImageFile = image
        StegImageFile = steg
        stega_instance = LSBEncrypter()
        stega_instance.run(TextToHide)
        
        
ls=LSBEncrypter();        
ls.hide_("iron man","image1.jpeg","encoded.jpeg")        
        
 