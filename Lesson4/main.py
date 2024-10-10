from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

# red channel
coordinates1 = (50, 0, image.width, image.height)
image1 = red.crop(coordinates1)

coordinates2 = (25, 0, image.width-25, image.height)
image2 = red.crop(coordinates2)

image_red = Image.blend(image1, image2, 0.3)

# blue channel
coordinates3 = (0, 0, image.width-50, image.height)
image3 = blue.crop(coordinates3)

coordinates4 = (25, 0, image.width-25, image.height)
image4 = blue.crop(coordinates4)

image_blue = Image.blend(image3, image4, 0.3)

# green channel
coordinates5 = (25, 0, image.width-25, image.height)
image_green = green.crop(coordinates5)

#merge image
final_image = Image.merge("RGB", (image_red, image_green, image_blue))
final_image.thumbnail((80, 80))
final_image.save("final_image.jpg")