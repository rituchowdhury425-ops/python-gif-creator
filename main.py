from PIL import Image, ImageOps
import os

# Folder names
image_folder = "images"
output_folder = "output"

# List to store images
images = []

# Read all images from the images folder
for file in sorted(os.listdir(image_folder)):
    if file.endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(image_folder, file)

        img = Image.open(path)

        # Resize while keeping aspect ratio
        img.thumbnail((150, 150))

        # Create a white background
        background = Image.new("RGB", (500, 500), "white")

        # Center the image
        x = (500 - img.width) // 2
        y = (500 - img.height) // 2

        background.paste(img, (x, y))

        images.append(background)

# Create GIF
if images:
    output_path = os.path.join(output_folder, "animation.gif")

    images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    duration=300,
    loop=0,
    optimize=True
)

    print("GIF created successfully!")
else:
    print("No images found in the 'images' folder.")