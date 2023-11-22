


import cv2

# Open the video file
video_file = 'fire_video_masks/vecteezy_fire-frame-on-black-background_3482670.mp4'  # Replace with your video file
cap = cv2.VideoCapture(video_file)

# Get the video's frame width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object for the rotated video
output_file = 'fire_video_masks/rotated_video_2.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec if needed
out = cv2.VideoWriter(output_file, fourcc, 30, (height, width))  # width and height swapped

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Rotate the frame counterclockwise
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Write the rotated frame to the output video
    out.write(rotated_frame)

    cv2.imshow('Rotated Video', rotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
