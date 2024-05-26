from PIL import Image
im = Image.open('pets0/Cat.jpg')
im2 = im.reduce(3)
im3 = im2.transpose(Image.FLIP_LEFT_RIGHT)
im4 = im3.rotate(90)
im3.save('Cat2.jpg')
im4.save('Cat3.jpg')
