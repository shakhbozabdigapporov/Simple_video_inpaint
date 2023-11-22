# from PIL import Image

# # Open the image
# img = Image.open('frame_0000.png')

# # Convert the image to grayscale
# img = img.convert('L')

# # Save the grayscale image
# img.save('grayscale_image.jpg')

# # Display the grayscale image (optional)
# img.show()


# from PIL import Image

# # Load the grayscale image
# grayscale_image = Image.open('grayscale_image.jpg')

# # Load the thermalized version of the grayscale image
# thermalized_image = Image.open('thermalized_image.png')

# # Calculate the colormap difference
# def calculate_colormap_difference(grayscale_img, thermalized_img):
#     colormap_difference = {}

#     grayscale_pixels = grayscale_img.getdata()
#     thermalized_pixels = thermalized_img.getdata()

#     for grayscale_color, thermalized_color in zip(grayscale_pixels, thermalized_pixels):
#         r_diff = thermalized_color[0] - grayscale_color
#         g_diff = thermalized_color[1] - grayscale_color
#         b_diff = thermalized_color[2] - grayscale_color

#         colormap_difference[grayscale_color] = (r_diff, g_diff, b_diff)

#     return colormap_difference

# colormap_difference = calculate_colormap_difference(grayscale_image, thermalized_image)

# # Print or inspect the colormap difference
# print(colormap_difference)








# import numpy as np
# import cv2

# gray8_image = cv2.imread("grayscale_image.jpg", cv2.IMREAD_ANYDEPTH)

# gray_image = np.zeros((120,160), dtype = np.uint8)
# gray_image = cv2.normalize(gray8_image, gray_image, 0, 255, cv2.NORM_MINMAX)
# gray_image = np.uint8(gray8_image)


# inferno_palette = cv2.applyColorMap(gray8_image, cv2.COLORMAP_INFERNO)
# cv2.imshow("gray", inferno_palette)
# cv2.waitKey(0)




# import cv2
# import numpy as np

# # Load the RGB image
# rgb_image = cv2.imread('frame_0000.png')

# # Create a thermal colormap
# thermal_colormap = cv2.applyColorMap(np.zeros_like(rgb_image), cv2.COLORMAP_HOT)

# # Convert the RGB image to grayscale
# gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

# # Normalize the grayscale image to the 0-255 range
# normalized_gray = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)

# # Apply the colormap to the normalized grayscale image
# thermal_image = cv2.applyColorMap(normalized_gray, cv2.COLORMAP_JET)

# # Save the thermal-like image
# cv2.imwrite('thermal_image.jpg', thermal_image)

# # Display the result (optional)
# cv2.imshow('Thermal Image', thermal_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
