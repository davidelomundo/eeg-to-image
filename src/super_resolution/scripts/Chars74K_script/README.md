Chars74K_script
=================

This folder contains a small Python script to resize PNG images from the Chars74K dataset.

Usage
-----

1. Install dependencies:

```bash
pip install Pillow
```

2. Place the source PNG images under the `Chars74K` directory (or change `INPUT_DIR` in the script).

3. Run the script:

```bash
python3 main.py
```

What the script does
--------------------

- Skips images smaller than 196x196.
- Produces three output folders:
  - `Chars74K_fixed` — resized to 192x192
  - `Chars74K_x2` — resized to 96x96 (labeled with `x2` suffix)
  - `Chars74K_x4` — resized to 48x48 (labeled with `x4` suffix)