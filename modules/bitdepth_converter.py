from PIL import Image
from io import BytesIO

class ImageConverter:
    def __init__(self):
        pass

    def convert_to_8bit(self, image_data):
        try:
            img = Image.open(BytesIO(image_data))
            if img.mode == "RGBA":
                img = img.convert("RGB")  
            img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
            return img
        except Exception as e:
            print(f"Error converting image: {e}")
            return None