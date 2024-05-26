from PIL import Image, ImageFilter

for i in range(1, 6):
    img = Image.open(f'in/{i}.jpg')
    input_image = img.filter(ImageFilter.CONTOUR)
    input_image.save(f"out/{i}.jpg")
