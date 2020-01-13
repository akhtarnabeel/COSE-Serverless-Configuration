"""handler_img"""

from PIL import Image
from wand.image import Image as WImage

def handler(event, context):
	image1 = Image.open("img.jpg")
	image1.rotate(45)
	image2 = Image.open("img.jpg")
	image2.rotate(90)
	newImage = Image.blend(image1, image2, 0.5)
	return event['event']