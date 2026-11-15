import os
from PIL import Image

# Input / output directories and settings
INPUT_DIR = "Chars74K"
OUTPUT_DIR_192 = "Chars74K_fixed"
OUTPUT_DIR_96 = "Chars74K_x2"
OUTPUT_DIR_48 = "Chars74K_x4"
MIN_SIZE = 196

os.makedirs(OUTPUT_DIR_192, exist_ok=True)
os.makedirs(OUTPUT_DIR_96, exist_ok=True)
os.makedirs(OUTPUT_DIR_48, exist_ok=True)

def resize_and_save(image, output_path, size, resample):
    resized_image = image.resize(size, resample)
    resized_image.save(output_path)

def process_images():
    # Choose LANCZOS resampling; provide fallback for older Pillow versions
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS

    for root, _, files in os.walk(INPUT_DIR):
        for filename in files:
            if not filename.lower().endswith(".png"):
                continue
            image_path = os.path.join(root, filename)

            # Open image safely and skip if unreadable
            try:
                with Image.open(image_path) as img:
                    width, height = img.size

                    # Skip images smaller than MIN_SIZE x MIN_SIZE
                    if width < MIN_SIZE or height < MIN_SIZE:
                        continue

                    base_filename, ext = os.path.splitext(filename)

                    # Resize and save at 192x192
                    output_filename_192 = os.path.join(OUTPUT_DIR_192, filename)
                    resize_and_save(img, output_filename_192, (192, 192), resample)

                    # Resize to 96x96 (x2)
                    output_filename_96 = os.path.join(OUTPUT_DIR_96, f"{base_filename}x2{ext}")
                    resize_and_save(img, output_filename_96, (96, 96), resample)

                    # Resize to 48x48 (x4)
                    output_filename_48 = os.path.join(OUTPUT_DIR_48, f"{base_filename}x4{ext}")
                    resize_and_save(img, output_filename_48, (48, 48), resample)
            except Exception:
                # Skip corrupted or unreadable files
                continue

if __name__ == "__main__":
    process_images()
    print("Processing completed.")