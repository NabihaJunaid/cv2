import cv2
import numpy as np
from google.colab import drive
from google.colab.patches import cv2_imshow

#mount google drive
drive.mount('/content/drive')

def apply_color_filter(image, filter_type):
  filtered_image = image.copy()

  if filter_type == "red_tint":
    filtered_image[:, :, 1] = 0 #green
    filtered_image[:, :, 0] = 0 #blue

  elif filter_type == "blue_tint":
    filtered_image[:, :, 1] = 0 #green
    filtered_image[:, :, 2] = 0 #red

  elif filter_type == "green_tint":
    filtered_image[:, :, 0] = 0 #blue
    filtered_image[:, :, 2] = 0 #red

  elif filter_type == "increase red":
    filtered_image[:, :, 2] = cv.add(filtered_image[:, :, 2], 50)
  
  elif filter_type == "decrease blue":
    filtered_image[:, :, 0] = cv2.sibstract(filtered_image[:, :, 0], 50)

  return filtered-image

#google drive image path
image_path = "/content/drive/MyDrive/swan scenery.jpg"

#read image
image = cv2.imread(image_path)

if image is None: 
  print("Error: Image not found")
else:
  while True:
    print("\nChoose filter:")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("i - increase red")
    print("d - decrease blue")
    print("q - quit")

    choice  = input("enter your choice:")

    if choice == "r":
      filter_type = "red_tint"
    elif choice == "b":
      filter_type = "blue_tint"
    elif choice == "g":
      filter_type = "green_tint"
    elif choice == "i":
      filter_type = "increase red"
    elif choice == "d":
      filter_type = "decrease blue"
    elif choice == "q":
      print("quitting...")
      break
    else:
      print("invalid choice")
      continue

filtered_image = apply_color_filter(image, filter_type)
cv2_imshow(filtered_image)
