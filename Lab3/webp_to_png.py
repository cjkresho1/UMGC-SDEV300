import os
from PIL import Image

if __name__ == '__main__':
    for file in os.listdir("./stateFlowerImages"):
        im = Image.open(f"./stateFlowerImages/{file}").convert("RGB")
        im.save(file.replace("webp", "png"), "png")
