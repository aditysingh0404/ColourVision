import cv2
import numpy as np


def extract_color_features(image):
    b, g, r = cv2.split(image)

    average_b = np.mean(b)
    average_g = np.mean(g)
    average_r = np.mean(r)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv_image)

    average_h = np.mean(h)
    average_s = np.mean(s)
    average_v = np.mean(v)

    features = {
        "average_red": round(float(average_r), 2),
        "average_green": round(float(average_g), 2),
        "average_blue": round(float(average_b), 2),
        "average_hue": round(float(average_h), 2),
        "average_saturation": round(float(average_s), 2),
        "average_value": round(float(average_v), 2)
    }

    return features


def calculate_color_histogram(image):
    histogram = {}

    channels = {
        "Blue": 0,
        "Green": 1,
        "Red": 2
    }

    for color, channel in channels.items():
        hist = cv2.calcHist(
            [image],
            [channel],
            None,
            [256],
            [0, 256]
        )

        histogram[color] = hist

    return histogram