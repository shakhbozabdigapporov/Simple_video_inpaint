import cv2
import os

# Path to the directory containing sequential images
image_folder = 'D:/test/sog_20231108_ver/main/results_inside/frame_18/image'

# Get the list of image files sorted by their names
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]  # Change the extension if your images are different

# Sort images by their filenames
images.sort(key=lambda x: int(x.split('.')[0]))

# Get the first image to obtain its dimensions
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
video_name = 'GSC_fire_smoke_human/gsc/output_results/smoke_output_result/inside_bg_11.avi'  # Change the video format if needed
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# Iterate through images and add them to the video
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Release the VideoWriter and destroy any OpenCV windows
video.release()
cv2.destroyAllWindows()
