# ☆*:･ﾟ✧ Sixel Image Converter ☆*:･ﾟ✧

This magical Python script transforms your beautiful images into the enchanting Sixel format, letting you display them in terminals that support Sixel graphics! It comes with two adorable conversion modules: a custom-made one and one that uses the amazing ImageMagick.

## 🎀 Dependencies 🎀

- **Python 3.x** (the cutest programming language!)
- **Pillow (PIL Fork)**: `pip install Pillow` (like a soft pillow for your images)
- **Wand (Optional, for the ImageMagick module)**: `pip install Wand` (a magic wand for image transformations!)
  - Needs ImageMagick to be installed on your system too.

## ૮꒰˵• ﻌ •˵꒱ა Usage ૮꒰˵• ﻌ •˵꒱ა

```bash
python main.py <module> <filepath>
```

- `<module>`:  
    - `self`: Uses the custom-made Sixel conversion module (like a handmade gift!).
    - `magick`: Uses the ImageMagick-based conversion module (powered by magical spells!).
- `<filepath>`: The path to the image file you want to transform (like a treasure map!).

## ૮₍´˶• . • ⑅ ₎ა Example ૮₍´˶• . • ⑅ ₎ა

To convert a picture named `image.png` using the custom-made module:

```bash
python main.py self image.png 
```

To convert the same picture using ImageMagick:

```bash
python main.py magick image.png
```

The script will print the Sixel code to your terminal (like a secret message!). You can redirect this to a file or pipe it to a terminal that supports Sixel graphics to see the image in its full kawaii glory!


## (๑˃ᴗ˂)ﻭ Modules (๑˃ᴗ˂)ﻭ

### `self` (Custom Sixel Converter)

This module uses the Pillow library to handle the image and create the Sixel code directly. It's like a little artist painting with pixels!

### `magick` (ImageMagick Sixel Converter)

This module uses the powerful ImageMagick library (with the Wand Python binding) for Sixel conversion. ImageMagick is like a wizard, making the Sixel code even more magical and detailed!

## (இ﹏இ`｡) Notes (っ °Д °;)っ

- Make sure your terminal emulator supports Sixel graphics to see the converted images (like having a special screen for magic!). 
- The `magick` module needs ImageMagick to be installed and set up on your system (like having a wizard's tower!). 
- The quality and details of the Sixel code might be different depending on the module you choose and the image you're converting (like using different art styles!).


## ૮₍ ˃ ⤙ ˂ ₎ა License ૮₍ ˃ ⤙ ˂ ₎ა

[Specify your chosen license here, e.g., MIT License] 
```
