import cv2
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import Dropdown
from IPython.display import display

def display_image(title, image):
  plt.figure(figsize=(6,6))
  if len(image.shape) == 2:
    plt.imshow(image, cmap='gray')
  else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.title(title)
  plt.axic('off')
  plt.show()

def process(choice, gray_image):
  if choice == 'Sobel':
    sx = cv2.Sobel(gray_image, cv2.CV_32F, 1, 0)
    sy = cv2.Sobel(gray_image, cv2.CV_32F, 0, 1)
    result = cv2.bitwise_or(sx.astype(np.uint8), sy.astype(np.uint8))
    display_image("Sobel Edge Detection", edges)
  
  elif choice == 'Canny':
    edges = cv2.Canny(gray_image, 100, 200)
    display_image("Canny Edge Detection", edges)

  elif choice == 'Laplacian':
    edges = cv2.Laplacian(gray_image, cv2.CV_64F)
    display_image("Laplacian Edge Detection", np.abs(lap).astype(np.uint8))

  elif choice=="Gaussian":
    blur = cv2.GaussianBlur(gray_image, (5,5), 0)
    display_image("Gaussian Blur", blur)

  elif choice=="Median":
    blur = cv2.medianBlur(gray_image, 5)
    display_image("Median Blur", blur)
  
#load image from Drive

from google.colab import drive
drive.mount('/content/drive')
image = cv2.imread('/content/drive/MyDrive/swan scenery.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image("Original Grayscale Image", gray)

dropdown = Dropdown(
    options=['Sobel', 'Canny', 'Laplacian', 'Gaussian', 'Median'],
    description = "Select:"
)

def on_change(change):
  process(change["new"], gray)

dropdown.observe(on_change, names="value")
display(dropdown)
