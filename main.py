import sys
from io import BytesIO
from pathlib import Path
from modules.resize import ImageResizer


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <module> <filepath>")
        sys.exit(1)

    module_name = sys.argv[1]
    image_file = sys.argv[2]
    save = sys.argv[3] if len(sys.argv) == 4 else None

    resizer = ImageResizer(image_file)
    resized_image = resizer.resize()
        
    with BytesIO() as output:
        resized_image.save(output, format="PNG")
        image_data = output.getvalue()

    if module_name == "self":
        from modules.sixel_encoder import SixelConverter
        processor = SixelConverter(image_data)
    elif module_name == "magick":
        from modules.magick import MagickSixelConverter
        processor = MagickSixelConverter(image_data)
    else:
        print("Invalid module name.")
        sys.exit(1)
    
    if save:
        save_path = "output/"
        if not Path(save_path).exists():
            Path(save_path).mkdir()
        with open(save_path + Path(image_file).stem + ".sixel", "w") as f:
            f.write(processor.generate_sixel())

    sixel_image = processor.generate_sixel()
    print(sixel_image, end="")
