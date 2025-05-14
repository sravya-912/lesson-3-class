import cv2
image = cv2.imread("sunset.jfif")

start_point = (0, 0)

end_point = (250, 250)


color = (0, 255, 0)

thickness = 9

image = cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()

start_point = (5, 5)

end_point = (220, 220)


color = (255, 0, 0)

thickness = 2

image = cv2.rectangle(image, start_point, end_point, color, thickness)

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()

center_coordinates = (120,100)

radius = 30
color = (255, 0, 0)

thickness = 2

image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow(window_name, image)
cv2.waitkey(0)
cv2.destroyAllWindows()

import cv2
image = cv2. imread (path)

# font
font = cv2. FONT_HERSHEY_SIMPLEX
# orgin
org = (50, 50)
# fontScale
fontscale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'openCV', org, font, fontscale, color, thicknes)

cv2.imshow(window name. image)
cv2.waitKey(0)
cv2.destroyALLWindows()