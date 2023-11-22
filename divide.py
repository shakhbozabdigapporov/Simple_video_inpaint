# import cv2
# import os

# # Open the video file
# video_path = '7_CLIP-20231018T135907-20231018T140907_CH06.mp4'
# cap = cv2.VideoCapture(video_path)

# # Create a directory to store the frames
# output_directory = 'frames/7_CLIP-20231018T135907-20231018T140907_CH06/'
# os.makedirs(output_directory, exist_ok=True)

# frame_count = 0

# # Read and save frames
# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     frame_count += 1
#     frame_filename = f"{output_directory}/frame_{frame_count:04d}.jpg"
#     cv2.imwrite(frame_filename, frame)

# # Release the video file and clean up
# cap.release()
# cv2.destroyAllWindows()


import os
from moviepy.editor import VideoFileClip
import imageio
from tqdm import tqdm

# Replace with the path to your video file
video_file = "GSC_fire_smoke_human/fire_output_results/outside/gsc2_5.avi"

# Load the video using MoviePy
video_clip = VideoFileClip(video_file)

# Set the start and end times for the subclip (in seconds)
start_time = 0
end_time = video_clip.duration  # Use the full duration of the video

# Extract the subclip
subclip = video_clip.subclip(start_time, end_time)

# Create a directory to save the frames
output_directory = "GSC_fire_smoke_human/fire_output_results/fire_images"
os.makedirs(output_directory, exist_ok=True)

# Iterate over the frames of the subclip and save them as images
frame_count = int(subclip.duration * subclip.fps)
for i, frame in tqdm(enumerate(subclip.iter_frames(fps=30, dtype="uint8")), total=frame_count):
    frame_filename = os.path.join(output_directory, f"frame_{i:04d}.png")
    imageio.imsave(frame_filename, frame)

# Close the video clip
video_clip.reader.close()

print("Frames extracted and saved as images.")









# """When reconstructing a video with full number of frames"""

# import cv2
# import os

# # Input directory containing image frames
# input_directory = 'frames'

# # Output video file
# output_video = 'reconstructed_video.mp4'

# # Get the list of image files in the directory
# frame_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.jpg')]

# # Sort the frame files
# frame_files.sort()

# # Get the first frame to obtain image dimensions
# first_frame = cv2.imread(frame_files[0])
# height, width, layers = first_frame.shape

# # Initialize VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to change this codec based on your system
# out = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

# # Write frames to the video
# for frame_file in frame_files:
#     frame = cv2.imread(frame_file)
#     out.write(frame)

# # Release the video writer
# out.release()


# """When skipping frame"""


# import cv2
# import os

# # Input directory containing image frames
# input_directory = 'frames'

# # Output video file
# output_video = 'reconstructed_video.mp4'

# # Get the list of image files in the directory
# frame_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith('.jpg')]

# # Sort the frame files
# frame_files.sort()

# # Get the first frame to obtain image dimensions
# first_frame = cv2.imread(frame_files[0])
# height, width, layers = first_frame.shape

# # Initialize VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to change this codec based on your system
# out = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

# # Write frames to the video, skipping one frame after each frame
# skip_frame = False
# for frame_file in frame_files:
#     frame = cv2.imread(frame_file)
#     if not skip_frame:
#         out.write(frame)
#     skip_frame = not skip_frame

# # Release the video writer
# out.release()


