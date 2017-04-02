import numpy
from PIL import Image as im
import numpy

class bitmap2ascii:
    def convert2gray(filename):
        try:
            file = im.open(filename)
            file.convert("L", colors= 8).save("gray" + filename)
        except:
            return "Not image or No such file"
    def convert2ascii(filename):
        pix = im.open(filename)
        w, h = pix.size
        i, j = 0
        while i == h:
            while j == w:
                pixdata = pix.getpixel(i, j)





test = bitmap2ascii.convert2ascii("포맷변환_test.bmp")
print(test)




