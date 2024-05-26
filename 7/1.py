from PIL import Image
im = Image.open('pets0/Cat.jpg')
im.show()
print(im.format, im.size, im.mode)

