import requests
from io import BytesIO
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Function to download the image from the API
def download_image_from_api(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        # Read the image data
        image_data = response.content
        return Image.open(BytesIO(image_data))

# API endpoint where the image is stored
image_url = "https://www.example.com/image.jpg"  # Replace this with API endpoint

# Create the Tkinter window
root = Tk()
root.title("Image Downloader")

# Download the image
image = download_image_from_api(image_url)

# Convert the image for displaying in Tkinter
if image:
    image_tk = ImageTk.PhotoImage(image)
    label = Label(root, image=image_tk)
    label.image = image_tk  # To prevent the image from being garbage collected
    label.pack()
else:
    label = Label(root, text="Failed to download image")
    label.pack()

root.mainloop()

