from wand.image import Image

class MagickSixelConverter:
    def __init__(self, image_data):
        self.image_data = image_data

    def generate_sixel(self):
        with Image(blob=self.image_data) as img:
            img.format = "sixel"
            sixel_data = img.make_blob()
        
        return sixel_data.decode("utf-8")