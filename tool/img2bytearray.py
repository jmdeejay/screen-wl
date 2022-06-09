from io import BytesIO
from PIL import Image
import sys


def convert_all_files ():
    for i in range (1, num_images):
        convert_file (i)

    array = name + " = ["
    for i in range (1, num_images):
        array += name + "_" + str(i) + "_buffer"
        if (i < num_images - 1): array += ", "
    array += "]"
    print(array)


def convert_file (file_number):
    image_name = name + "_" + str(file_number) + "." + extension
    im = Image.open(path + image_name).convert('1')
    im_resize = im.resize((x, y))
    buf = BytesIO()
    im_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()
    temp = len(str(x) + ' ' + str(y)) + 4
    result = str(byte_im[temp::])[2:][:-1].replace("\"", "\\\"")
    output = name + "_" + str(file_number) + "_buffer = bytearray(b\"" + result + "\")"
    print(output)


if (len(sys.argv) <= 6):
    print("Usage: python img2bytearray.py /path/to/image name extension nbrImage width height")
    # python img2bytearray.py ./nyan/ nyan jpg 12 48 48
else:
    path = str(sys.argv[1])
    name = str(sys.argv[2])
    extension = str(sys.argv[3])
    num_images = int(sys.argv[4]) + 1

    x = int(sys.argv[5])
    y = int(sys.argv[6])
    convert_all_files()
