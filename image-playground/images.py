from PIL import Image, ImageFilter

img = Image.open('./city.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("grey.png", 'png')
