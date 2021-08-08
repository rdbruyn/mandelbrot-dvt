from mandelbrot import stability, make_pixels
import numpy as np
from PIL import Image


def main():
    w, h = 1920, 1080

    w_step = 3 / w
    h_step = 2 / h

    stability_count = [stability(complex(i, j))
                       for j in np.arange(1, -1, -h_step)
                       for i in np.arange(-2, 1, w_step)]

    pixels = make_pixels(stability_count)
    img = Image.frombuffer('RGB', (w, h), pixels)
    img.save('mandelbrot_rgb.png')


if __name__ == '__main__':
    main()
