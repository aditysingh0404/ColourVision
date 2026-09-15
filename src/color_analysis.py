def find_dominant_color(features):
    colors = {
        "Red": features["average_red"],
        "Green": features["average_green"],
        "Blue": features["average_blue"]
    }

    dominant_color = max(colors, key=colors.get)

    return dominant_color