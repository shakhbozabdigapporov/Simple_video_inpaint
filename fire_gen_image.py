import cv2, random, string

def resize(img, desi_w, desi_h):
    return cv2.resize(img, (int(desi_w), int(desi_h)), interpolation=cv2.INTER_AREA)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def get_roi_image(img, roi):
    roi_x, roi_y, roi_w, roi_h = roi
    roi_img = img[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]
    return roi_img

def simple_patching(fg, bg_roi_img, alpha=3, beta=1):
    fg = cv2.convertScaleAbs(fg, alpha=alpha, beta=beta)
    combined_img = cv2.add(bg_roi_img, fg)
    return combined_img

def resize_roi(fg_roi_image, bg_roi, obj_type="fire"):
    if obj_type == "fire":
        img_h, img_w, _ = fg_roi_image.shape
        roi_x, roi_y, roi_w, roi_h = bg_roi
        roi_x_center = roi_x + roi_w/2

        new_img_h = roi_h
        new_img_w = (roi_h*img_w)/img_h

        new_fg_roi_image = resize(fg_roi_image, new_img_w, new_img_h)
        new_roi_x = roi_x_center - new_img_w/2
        new_roi_y = roi_y
        new_bg_roi = (int(new_roi_x), int(new_roi_y), int(new_img_w), int(new_img_h))
        return new_fg_roi_image, new_bg_roi

    if obj_type == "smoke":
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

def select_roi(img, roi_name="bg"):
    roi = cv2.selectROI(roi_name, img)
    return roi

def add_combined_roi_img(img, roi_img, roi):
    roi_x, roi_y, roi_w, roi_h = roi
    img[roi_y:roi_y + roi_h, roi_x: roi_x + roi_w] = roi_img
    return img

bg_path = r"frame_0007.png"  # Replace with your background image path
fg_path = r"decrypted_masks/fire16.png"  # Replace with your foreground image path
obj_type = "fire"  # Specify the object type ("smoke" or "fire")
output_path = 'GSC_fire_smoke_human/output_results/fire'

if obj_type == "smoke":
    alpha = 0.9
elif obj_type == "fire":
    alpha = 0.7

fg_image = cv2.imread(fg_path)
bg_image = cv2.imread(bg_path)

fg_roi = select_roi(fg_image, "fg")
bg_roi = select_roi(bg_image, "bg")

try:
    fg_roi_image = get_roi_image(fg_image, fg_roi)
    new_fg_roi_image, new_bg_roi = resize_roi(fg_roi_image, bg_roi, obj_type=obj_type)
    new_bg_roi_image = get_roi_image(bg_image, new_bg_roi)
    combined_image = simple_patching(new_fg_roi_image, new_bg_roi_image, alpha=alpha)
    final_image = add_combined_roi_img(bg_image.copy(), combined_image, new_bg_roi)

    cv2.imshow("Final Image", final_image)
    print(final_image)
    cv2.imwrite(f'GSC_fire_smoke_human/output_results/fire/fire12_1.png', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print("Error:", e)
