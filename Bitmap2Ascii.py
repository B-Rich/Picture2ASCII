from PIL import Image as im

class bitmap2ascii:
    def convert(filename):

        try:
            file = im.open(filename)
            file.convert("L", colors= 16).save("gray_" + filename)

        except:
            return "Not image or No such file"

        pix = im.open("gray_" + filename)
        w, h = pix.size

        with open('Ascii_'+ filename + '.txt', 'w') as file:
            asciiList = ['@', '#', '=', '+', '-', '.', ' ']

            for i in range(h):
                for j in range(w):
                    loc = (j, i)
                    pixdata = pix.getpixel(loc)
                    if pixdata in range(11, 43):
                        asciipix = asciiList[0]
                        file.write(asciipix)
                    elif pixdata in range(43, 88):
                        asciipix = asciiList[1]
                        file.write(asciipix)
                    elif pixdata in range(88, 137):
                        asciipix = asciiList[2]
                        file.write(asciipix)
                    elif pixdata in range(137, 169):
                        asciipix = asciiList[3]
                        file.write(asciipix)
                    elif pixdata in range(169, 190):
                        asciipix = asciiList[4]
                        file.write(asciipix)
                    elif pixdata in range(190, 255):
                        asciipix = asciiList[5]
                        file.write(asciipix)
                    else:
                        asciipix = asciiList[6]
                        file.write(asciipix)

                        # lineMatrix.append(pixdata)

                file.write("\n")



