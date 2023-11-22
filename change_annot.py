import cv2
import os


# Function to read YOLOv4 Darknet format annotations
def read_darknet_annotations(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    annotations = []
    for line in lines:
        values = line.split()
        # Extract values for each annotation
        obj_class = int(values[0])
        x_center, y_center, box_width, box_height = map(float, values[1:])

        # Append annotation to the list
        annotations.append({
            'class': obj_class,
            'x_center': x_center,
            'y_center': y_center,
            'width': box_width,
            'height': box_height
        })

    return annotations

# Path to your annotations file in YOLOv4 Darknet format
# annotations_file_path = 'fire_smoke_human.v14i.darknet/test/frame_0449_png.rf.ce2b025d777c9a0295cdd904befa0ef0.txt'
# image_path = 'fire_smoke_human.v14i.darknet/test/frame_0449_png.rf.ce2b025d777c9a0295cdd904befa0ef0.jpg'

# Read annotations
# annotations = read_darknet_annotations(annotations_file_path)



def change_class_order(annotations, original_order, new_order):
    mapping = {original_order[i]: new_order[i] for i in range(len(original_order))}
    for annotation in annotations:
        # Map the old class labels to the new ones
        annotation['class'] = mapping[annotation['class']]
    return annotations
# Function to display detections on images
def display_detections(image_path, annotations):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    for annotation in annotations:
        x_center = int(annotation['x_center'] * width)
        y_center = int(annotation['y_center'] * height)
        box_width = int(annotation['width'] * width)
        box_height = int(annotation['height'] * height)

        # Calculate top-left and bottom-right coordinates of the bounding box
        x1 = int(x_center - box_width / 2)
        y1 = int(y_center - box_height / 2)
        x2 = int(x_center + box_width / 2)
        y2 = int(y_center + box_height / 2)

        # Display the bounding box on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"Class: {annotation['class']}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with detections
    cv2.imshow('Image with Detections', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def write_darknet_annotations(file_path, annotations):
    with open(file_path, 'w') as file:
        for annotation in annotations:
            line = f"{annotation['class']} {annotation['x_center']} {annotation['y_center']} {annotation['width']} {annotation['height']}\n"
            file.write(line)

# Original and new class orders
original_classes = [0, 1, 2]
new_classes = [0, 2, 1]
root_folder = 'fire_smoke_human.v14i.darknet/valid'

for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            print("Processing:", file_path)

            # Read annotations
            annotations = read_darknet_annotations(file_path)

            # Change the order of the classes
            modified_annotations = change_class_order(annotations, original_classes, new_classes)
            write_darknet_annotations(file_path, modified_annotations)




# annotations = read_darknet_annotations(annotations_file_path)
# display_detections(image_path, annotations)