import random

colors = ["Green", "Yellow", "Red"]

while True:
    traffic = random.choice(colors)
    print(f"Traffic light: {traffic}")

    if traffic == "Green":
        print("GO!")
    elif traffic == "Yellow":
        print("Slow Down")
    elif traffic == "Red":
        print("Stop")
        break