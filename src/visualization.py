import cv2
import matplotlib.pyplot as plt


def save_result(image, output_path, features, dominant_color):
    result = image.copy()

    text = f"Dominant Color: {dominant_color}"

    cv2.putText(
        result,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imwrite(output_path, result)


def save_histogram(image, output_path):
    colors = ("b", "g", "r")

    plt.figure()

    for i, color in enumerate(colors):
        histogram = cv2.calcHist(
            [image],
            [i],
            None,
            [256],
            [0, 256]
        )

        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig(output_path)
    plt.close()