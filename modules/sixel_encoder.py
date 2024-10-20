import time
from modules.bitdepth_converter import ImageConverter

class SixelConverter:
    def __init__(self, image_data, dither=False):
        self.start_time = time.time()
        bitdepth_converter = ImageConverter()
        self.image_data = bitdepth_converter.convert_to_8bit(image_data)
        self.dither = dither
        self.img = self.image_data
        self.img = self.img.convert("RGB")
        if self.dither:
            self.dither_image()
        self.all_pixels = self.extract_all_pixels()
        self.unique_pixels = self.extract_unique_pixels()
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

    def dither_image(self):
        self.img = self.img.convert("PA")
        self.img = self.img.convert("RGB")

    
    def extract_unique_pixels(self):
        unique_pixels = {}
        unique_pixel_set = set()
        for pixel in self.all_pixels:
            if pixel not in unique_pixel_set:
                unique_pixel_set.add(pixel)
                unique_pixels[pixel] = len(unique_pixels)
        return unique_pixels

    def extract_all_pixels(self):
        all_pixels = []
        width, height = self.img.size
        for row in range(height):
            for col in range(0, width, 6):
                for i in range(col, min(col + 6, width)):
                    r, g, b = self.img.getpixel((i, row))
                    r_percent = int((r / 255) * 100)
                    g_percent = int((g / 255) * 100)
                    b_percent = int((b / 255) * 100)

                    all_pixels.append((r_percent, g_percent, b_percent))
        return all_pixels

    def generate_sixel(self):
        image_data_list = []
        width, _ = self.img.size
        image_string = (
            '\x1bPq"1;1;{};{}'.format(self.img.size[0], self.img.size[1])
        )
        for pixel in self.unique_pixels:
            image_string += (
                "#{};2;{};{};{}".format(
                    self.unique_pixels[pixel], pixel[0], pixel[1], pixel[2]
                )
            )

        sixel_characters = [
            "0b000001",
            "0b000010",
            "0b000100",
            "0b001000",
            "0b010000",
            "0b100000",
        ]
        sixel_index = 0
        i = 1
        last_color = None
        last_sixel = None
        for current_pixel in self.all_pixels:
            sixel_index = 0 if sixel_index == 6 else sixel_index
            color_index = self.unique_pixels[current_pixel]
            sixel = chr(int(sixel_characters[sixel_index], 2) + 63)

            match i % (width * 6):
                case 0:
                    match last_color == color_index and last_sixel == sixel:
                        case True:
                            image_string += "{}$-".format(sixel)
                        case False:
                            image_string += "#{}{}$-".format(
                                color_index, sixel
                            )
                    sixel_index += 1
                case _ if i % width == 0:
                    match last_color == color_index and last_sixel == sixel:
                        case True:
                            image_string += "{}$".format(sixel)
                        case False:
                            image_string += "#{}{}$".format(
                                color_index, sixel
                            )
                    sixel_index += 1
                case _:
                    match last_color == color_index and last_sixel == sixel:
                        case True:
                            image_string += "{}".format(sixel)
                        case False:
                            image_string += "#{}{}".format(
                                color_index, sixel
                            )
            i += 1
            last_color = color_index
            last_sixel = sixel
        image_string += "\x1b\\"

        image_data_list.append(image_string)
        return image_data_list[0]