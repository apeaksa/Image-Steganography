from PIL import Image
from main import decode_image

encoded_image_file = "enc_image.png"

img2 = Image.open(encoded_image_file)
hidden_text = decode_image(img2)
print("Hidden text:\n",hidden_text)
