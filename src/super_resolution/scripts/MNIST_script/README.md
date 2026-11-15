MNIST_script
=============

This script downloads the MNIST dataset, converts grayscale images to RGB, and saves them at multiple resolutions.

Install:
```bash
pip install Pillow torchvision
```

Usage
-----
```bash
python3 main.py
```

What it does
------------
- Downloads MNIST into `./mnist_data` (if not present).
- Converts dataset images from grayscale to RGB (3 channels).
- Saves images into these folders:
  - `mnist_images/train` and `mnist_images/test` — original 28x28 RGB
  - `mnist_x2/train` and `mnist_x2/test` — resized 14x14 with `x2` suffix
  - `mnist_x4/train` and `mnist_x4/test` — resized 7x7 with `x4` suffix