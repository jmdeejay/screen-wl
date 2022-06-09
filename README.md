# screen-wl
Add animations, games & informations to an oled screen (128X64 I2C SSD1306)

## Description
I connected a rpi pico micro-controller on the additional unused jsp connector on a Work Louder® [creator board](https://worklouder.cc/creator-board/).
Then I had additional power (CPU/RAM) to do advanced animations & add fun functionalities on a small oled screen.

## Available modes
- Robot animation
- Nyan cat animation
- Temperature + date + time
- Mario animation
- Random pictures from folder
- Memory usage (mostly for debugging)
- Game of life
- Starfield
- Matrix
- Mazes
- Invaders
- Mandelbrot

## Code in action
[![Watch the video](https://img.youtube.com/vi/I2ijPdWcYmc/hqdefault.jpg)](https://www.youtube.com/watch?v=I2ijPdWcYmc)

## Material used
- Created a custom jsp to usb type B connector.
- [rpi pico](https://www.amazon.ca/-/fr/Raspberry-microcontr%C3%B4leur-flexible-RP2040-horloge/dp/B08TQSDP28/ref=sr_1_7?__mk_fr_CA=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1D8EETAK0RJBB&keywords=rpi+pico&qid=1654741366&sprefix=rpi+pico%2Caps%2C73&sr=8-7)
- [oled screen](https://www.amazon.ca/-/fr/gp/product/B0891N9X3Q/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) (128X64 I2C SSD1306)

## Wiring
<p align="center">
  <img src="https://user-images.githubusercontent.com/9083510/172753418-b93e3baf-a838-4a99-a54f-9dcc7bec4ddb.png" alt="schema" />
</p>

### Tool to generate new animations / images: img2bytearray.py
Usage: `python img2bytearray.py /path/to/image name extension nbrImage width height`

This tool will convert for you automatically your images into bytearrays.
Images must be converted into bytearrays in order to work in the code.
You just need to copy-paste the result in a new python file.
You can look in the `/img/` folder for existing examples of generated code.
