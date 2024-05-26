from PIL import Image, ImageFilter

im = Image.open('pets0/Cat.jpg')
im2 = im.reduce(5)
im2 = im2.filter(ImageFilter.BLUR)
img = Image.open('pets0/Koshi.jpg')
img.paste(im2, (300,610))
img.show()