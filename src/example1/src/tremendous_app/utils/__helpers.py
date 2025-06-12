import os
import pathlib

import numpy as np


def select_random_meme(
    meme_database_dir: pathlib.Path,
) -> pathlib.Path:
    """Select random meme from specified directory.

    :param meme_database_dir: directory containing tremendously awesome memes.
    :type meme_database_dir: pathlib.Path
    :raises RuntimeError: raises error if no memes are found in meme_database_dir.
    :return: path to one selected meme.
    :rtype: pathlib.Path
    """
    memes = os.listdir(meme_database_dir)
    num_memes = len(memes)
    if num_memes == 0:
        raise RuntimeError(
            f"Found {num_memes} in {meme_database_dir}! This is a tremendous problem!"
        )
    return (
        meme_database_dir
        / memes[np.random.randint(num_memes)]
    )

def get_mandle_bounds():
   zoom_center_real = np.random.uniform(-2, 1)
   zoom_center_imag = np.random.uniform(-1.5, 1.5)
   zoom_size = np.random.uniform(0.1,0.5)
   xmin = zoom_center_real - zoom_size
   xmax = zoom_center_real + zoom_size
   ymin = zoom_center_imag - zoom_size
   ymax = zoom_center_imag + zoom_size
   return xmin, xmax, ymin, ymax
   
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iterations):
   x = np.linspace(xmin, xmax, width)
   y = np.linspace(ymin, ymax, height)
   X, Y = np.meshgrid(x, y)
   C = X + 1j*Y
   Z = np.zeros_like(C)
   div_time = np.zeros(C.shape, dtype=int)
   for i in range(max_iterations):
       Z = Z**2 + C
       mask = (abs(Z) > 2) & (div_time == 0)
       div_time[mask] = i
   return div_time
