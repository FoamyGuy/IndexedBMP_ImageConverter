from PIL import Image
import sys

img = Image.open(sys.argv[1])
newimg = img.convert(mode='P', palette=Image.ADAPTIVE, colors=256)

new_file_name = "%s.bmp" % sys.argv[1]
newimg.save(new_file_name, "BMP")