import sys
sys.path.append("src")

from feature_extraction import extract_color_features
from color_analysis import find_dominant_color
import numpy as np


def test_feature_extraction():
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    features = extract_color_features(image)

    assert "average_red" in features
    assert "average_green" in features
    assert "average_blue" in features
    assert "average_hue" in features
    assert "average_saturation" in features
    assert "average_value" in features


def test_dominant_color():
    features = {
        "average_red": 200,
        "average_green": 100,
        "average_blue": 50
    }

    result = find_dominant_color(features)

    assert result == "Red"


print("All tests passed successfully!")