import os
from torchvision.datasets import MNIST
from torchvision import transforms
from PIL import Image


def convert_grayscale_to_rgb(image: Image.Image) -> Image.Image:
    """Convert a single-channel (grayscale) PIL image to RGB (3 channels)."""
    return image.convert("RGB")


def download_mnist(data_dir: str):
    """Download MNIST train and test datasets and return them.

    The transform used here leaves the images as tensors; conversion to PIL is
    performed when saving.
    """
    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = MNIST(root=data_dir, train=True, download=True, transform=transform)
    test_dataset = MNIST(root=data_dir, train=False, download=True, transform=transform)

    return train_dataset, test_dataset


def save_images(dataset, folder: str, resize=None, original_size: bool = False, suffix: str | None = None):
    """Save images from a torchvision dataset to disk.

    - `resize`: tuple with target size (width, height) or None to keep original.
    - `original_size`: if True, save the image without resizing.
    - `suffix`: optional suffix to append to the filename (e.g. 'x2').
    """
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    to_pil = transforms.ToPILImage()

    for idx, (image, label) in enumerate(dataset):
        pil_img = to_pil(image)
        pil_img = convert_grayscale_to_rgb(pil_img)

        if original_size:
            image_name = f"{idx}.png"
        else:
            if resize is not None:
                pil_img = transforms.Resize(resize)(pil_img)
            if suffix:
                image_name = f"{idx}{suffix}.png"
            else:
                image_name = f"{idx}.png"

        image_path = os.path.join(folder, image_name)
        pil_img.save(image_path)


if __name__ == "__main__":
    data_dir = "./mnist_data"

    folders = {
        "train_28x28": "./mnist_images/train",
        "test_28x28": "./mnist_images/test",
        "train_14x14": "./mnist_x2/train",
        "test_14x14": "./mnist_x2/test",
        "train_7x7": "./mnist_x4/train",
        "test_7x7": "./mnist_x4/test",
    }

    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)

    train_dataset, test_dataset = download_mnist(data_dir)

    # Save original 28x28 (converted to RGB)
    save_images(train_dataset, folders["train_28x28"], original_size=True)
    save_images(test_dataset, folders["test_28x28"], original_size=True)

    # Save resized versions (14x14 with suffix "x2")
    save_images(train_dataset, folders["train_14x14"], resize=(14, 14), suffix="x2")
    save_images(test_dataset, folders["test_14x14"], resize=(14, 14), suffix="x2")

    # Save further downsampled versions (7x7 with suffix "x4")
    save_images(train_dataset, folders["train_7x7"], resize=(7, 7), suffix="x4")
    save_images(test_dataset, folders["test_7x7"], resize=(7, 7), suffix="x4")

    print("MNIST dataset images have been saved at multiple resolutions:")
    for key, path in folders.items():
        print(f"{key}: {path}")
