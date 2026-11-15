EMNIST_script
=============

Small helper script that downloads the EMNIST (letters) split, converts dataset items to 96x96 PNG images, and also creates 48x48 versions.

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
- Downloads EMNIST into `./data` (if not already present).
- Produces two output folders:
  - `EMNIST_images_96x96` — images resized to 96x96 (from dataset transforms)
  - `EMNIST_images_48x48` — images resized to 48x48 (downsampled from 96x96)