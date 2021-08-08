from mandelbrot import stability
import numpy as np
from PIL import Image


def main():
    w, h = 900, 600

    w_step = 3 / w
    h_step = 2 / h

    stability_count = [stability(complex(i, j))
                       for j in np.arange(1, -1, -h_step)
                       for i in np.arange(-2, 1, w_step)]

    pixels = np.array(stability_count, dtype=np.uint8)
    pixels[pixels < 200] = 255
    pixels[pixels == 200] = 0

    img = Image.frombuffer('L', size=(w, h), data=pixels)
    img.save('mandelbrot.jpg')


if __name__ == '__main__':
    main()
