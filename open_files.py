from moviepy.editor import VideoFileClip

# Replace 'input_file.mov' with the path to your .mov file
input_file_path = 'smoke_sample_videos/smoke3.mov'

# Replace 'output_file.mp4' with the desired path for the output .mp4 file
output_file_path = 'smoke_sample_videos/output_smoke3.mp4'

# Load the .mov file
video = VideoFileClip(input_file_path)

# Write the .mp4 file
video.write_videofile(output_file_path, codec='libx264')

# Close the file when done to release the resources
video.close()



