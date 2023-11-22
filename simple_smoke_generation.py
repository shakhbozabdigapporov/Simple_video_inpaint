import cv2, random, string
def resize(img, desi_w, desi_h):
    return cv2.resize(img, (int(desi_w), int(desi_h)), interpolation=cv2.INTER_AREA)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def get_roi_image(img, roi):
    roi_x, roi_y, roi_w, roi_h = roi
    roi_img = img[roi_y:roi_y + roi_h, roi_x: roi_x + roi_w]
    return roi_img

def simple_patching(fg, bg_roi_img, alpha=0.5, beta=0.2):

    fg = cv2.convertScaleAbs(fg, alpha=alpha, beta=beta)
    cv2.imshow("fg", fg)

    combined_img = cv2.addWeighted(bg_roi_img, 1, fg, 1, 0)
    # combined_img = cv2.add(bg_roi_img, fg)
    return combined_img



# def simple_patching(fg, bg_roi_img, alpha=0.5, beta=0.2):
#     fg = cv2.convertScaleAbs(fg, alpha=0.5, beta=0.5)  # Reducing the intensity of the foreground by half
#     cv2.imshow("fg", fg)

#     # Create a mask for the foreground
#     _, mask = cv2.threshold(cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY), 10, 255, cv2.THRESH_BINARY)
#     mask_inv = cv2.bitwise_not(mask)

#     # Combine foreground and background using the mask
#     fg_area = cv2.bitwise_and(fg, fg, mask=mask)
#     bg_area = cv2.bitwise_and(bg_roi_img, bg_roi_img, mask=mask_inv)
#     combined_img = cv2.add(fg_area, bg_area)

#     return combined_img


def resize_roi(fg_roi_image, bg_roi, obj_type = "fire"):
    if obj_type =="fire":
        img_h, img_w, _ = fg_roi_image.shape
        roi_x, roi_y, roi_w, roi_h = bg_roi
        roi_x_center = roi_x + roi_w/2

        new_img_h = roi_h
        new_img_w = (roi_h*img_w)/img_h

        new_fg_roi_image = resize(fg_roi_image, new_img_w, new_img_h)
        new_roi_x = roi_x_center-new_img_w/2
        new_roi_y = roi_y
        new_bg_roi = (int(new_roi_x), int(new_roi_y), int(new_img_w), int(new_img_h))
        return new_fg_roi_image, new_bg_roi

    if obj_type =="smoke":
        img_h, img_w, _ = fg_roi_image.shape
        roi_x, roi_y, roi_w, roi_h = bg_roi
        new_w = roi_w
        new_h = int(img_h * new_w / (img_w))
        new_img_w, new_img_h = new_w, new_h
        new_roi_x = roi_x
        new_roi_y = int(roi_y + (roi_h - new_h))
        new_roi = new_roi_x, new_roi_y, new_w, new_h
        new_img = resize(fg_roi_image, new_img_w, new_img_h)
        return new_img, new_roi

def select_roi(img, roi_name = "bg"):
    roi = cv2.selectROI(roi_name, img)
    return roi

def add_combined_roi_img(img, roi_img, roi):
    roi_x, roi_y, roi_w, roi_h = roi
    img[roi_y:roi_y + roi_h, roi_x: roi_x + roi_w] = roi_img
    return img


def config_video_saving(capture, output_path, fps=30):
    height, width, _ = capture.shape
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, size)
    return out


fg_path = r"fire_video_masks/rotated_video_2.mp4"
bg_path = r"frame_0018.png"
obj_type = "fire"
video_output_path = r"GSC_fire_smoke_human/gsc/output_results/fire_output_results/inside/gsc1_4.avi"

fps = 40
if obj_type == "smoke":
    alpha = 0.9
if obj_type == "fire":
    alpha = 0.7

fg_ratio = 2.5
fg_capture = cv2.VideoCapture(fg_path)
fg_, fg_image = fg_capture.read()
fg_image = resize(fg_image, int(fg_image.shape[1]/fg_ratio), int(fg_image.shape[0]/fg_ratio))
fg_roi = select_roi(fg_image, "fg")

bg_image = cv2.imread(bg_path)
bg_roi = select_roi(bg_image, "bg")
out = config_video_saving(bg_image, video_output_path, fps)

while fg_:
    fg_, fg_image = fg_capture.read()
    fg_image = resize(fg_image, int(fg_image.shape[1]/fg_ratio), int(fg_image.shape[0]/fg_ratio))
    bg_image_ori = bg_image.copy()
    try:
        fg_roi_image = get_roi_image(fg_image, fg_roi)
        new_fg_roi_image, new_bg_roi = resize_roi(fg_roi_image, bg_roi, obj_type=obj_type)
        new_bg_roi_image = get_roi_image(bg_image, new_bg_roi)
        combined_image = simple_patching(new_fg_roi_image, new_bg_roi_image, alpha=alpha)
        final_image = add_combined_roi_img(bg_image_ori, combined_image, new_bg_roi)
    except:
        bg_image= bg_image
    out.write(final_image)
    cv2.imshow("final_image", final_image)
    cv2.waitKey(1)



