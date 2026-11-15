import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image
import numpy as np

# Output directories
OUTPUT_DIR_96 = 'EMNIST_images_96x96'
OUTPUT_DIR_48 = 'EMNIST_images_48x48'
os.makedirs(OUTPUT_DIR_96, exist_ok=True)
os.makedirs(OUTPUT_DIR_48, exist_ok=True)

# Transform to create 96x96 images from the dataset
TRANSFORM_96 = transforms.Compose([
    transforms.Resize((96, 96)),
    transforms.ToTensor()
])

def save_image_from_tensor(tensor, filepath):
    arr = tensor.detach().cpu().numpy().squeeze() * 255
    image = Image.fromarray(arr.astype(np.uint8), mode='L')
    image.save(filepath)

def process_emnist():
    # Choose LANCZOS resampling with fallback for older Pillow versions
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS

    # Download / prepare dataset
    emnist_dataset = datasets.EMNIST(root='./data', split='letters', train=True, download=True, transform=TRANSFORM_96)
    data_loader = DataLoader(emnist_dataset, batch_size=1, shuffle=False)

    for idx, (image, label) in enumerate(data_loader):
        try:
            # Save 96x96 image (already transformed)
            filename_96 = os.path.join(OUTPUT_DIR_96, f'image_{idx:05d}_label_{int(label.item())}.png')
            save_image_from_tensor(image, filename_96)

            # Create and save 48x48 by resizing the 96x96 array
            arr = image.detach().cpu().numpy().squeeze() * 255
            image_pil = Image.fromarray(arr.astype(np.uint8), mode='L')
            image_48 = image_pil.resize((48, 48), resample)
            filename_48 = os.path.join(OUTPUT_DIR_48, f'image_{idx:05d}_label_{int(label.item())}.png')
            image_48.save(filename_48)

            if idx % 1000 == 0:
                print(f'Saved {idx} images')
        except Exception:
            # Skip problematic items
            continue

if __name__ == '__main__':
    process_emnist()
    print('Completed.')
