import cv2


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("Image could not be loaded.")

    return image


def resize_image(image, width=500):
    height, original_width = image.shape[:2]

    ratio = width / original_width
    new_height = int(height * ratio)

    resized = cv2.resize(image, (width, new_height))

    return resized