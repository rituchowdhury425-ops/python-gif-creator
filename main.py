from PIL import Image
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
        images.append(img)

# Create GIF
if images:
    output_path = os.path.join(output_folder, "animation.gif")

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=500,  # Time each image is displayed (milliseconds)
        loop=0         # 0 = Loop forever
    )

    print("GIF created successfully!")
else:
    print("No images found in the 'images' folder.")