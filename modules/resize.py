from PIL import Image
from modules.terminal_size import TerminalSize

class ImageResizer:
    def __init__(self, image_path):
        self.image_path = image_path

    def resize(self):
        img = Image.open(self.image_path)

        term_size = TerminalSize()
        term_width, term_height = term_size.get_terminal_size_pixels()

        if img.width > term_width or img.height > term_height:
            limiting_dimension = min(term_width, term_height)

            if img.width < img.height:
                new_width = limiting_dimension
                new_height = int(limiting_dimension * (img.height / img.width))
            else:
                new_height = limiting_dimension
                new_width = int(limiting_dimension * (img.width / img.height))

            resized_img = img.resize((new_width, new_height))
            img.close()
            return resized_img
        else:
            copied_img = img.copy()
            img.close()
            return copied_img