from PIL import Image, ImageFilter

img = Image.open('in/1.jpg')

img = img.filter(ImageFilter.CONTOUR)
img.save("out/1.jpg")

img = img.filter(ImageFilter.CONTOUR)
img.save("out/2.jpg")

img = img.filter(ImageFilter.CONTOUR)
img.save("out/3.jpg")

img = img.filter(ImageFilter.CONTOUR)
img.save("out/4.jpg")

img = img.filter(ImageFilter.CONTOUR)
img.save("out/5.jpg")
