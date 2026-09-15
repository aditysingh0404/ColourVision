import os

from preprocessing import load_image, resize_image
from feature_extraction import extract_color_features, calculate_color_histogram
from color_analysis import find_dominant_color
from visualization import save_result, save_histogram


def main():
    input_path = "data/input.jpg"
    output_path = "results/output.jpg"

    image = load_image(input_path)
    image = resize_image(image)

    features = extract_color_features(image)
    calculate_color_histogram(image)

    dominant_color = find_dominant_color(features)

    os.makedirs("results", exist_ok=True)

    save_result(
        image,
        output_path,
        features,
        dominant_color
    )

    save_histogram(
        image,
        "results/color_histogram.png"
    )

    print("\n--- Color Analysis Result ---")
    print(f"Average Red: {features['average_red']}")
    print(f"Average Green: {features['average_green']}")
    print(f"Average Blue: {features['average_blue']}")
    print(f"Average Hue: {features['average_hue']}")
    print(f"Average Saturation: {features['average_saturation']}")
    print(f"Average Value: {features['average_value']}")
    print(f"Dominant Color: {dominant_color}")
    print("\nResult saved to: results/output.jpg")
    print("Histogram saved to: results/color_histogram.png")


if __name__ == "__main__":
    main()