import cv2 #this loads openCV,used to process images
import numpy as np #this loads numpy,helps with math and arrays.
import matplotlib.pyplot as plt #this helps us display images like a chart.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello from Flask on Render!"

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=10000) 

#Read the image
image = cv2.imread("image_assignment.jpg")

#resize to fit screen
image = cv2.resize(image,(1000,int(image.shape[0]*1000/image.shape[1])))

#convert BGR(openCV default) to RGB(for matplotlib).
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#show the image using matplotlib
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")#hides X and Y axis
plt.show()

#manually crop the visiting card(bottom-right part)
card = image[500:650,630:900] #[y1:y2,x1:x2]

#show the cropped card
card_rgb = cv2.cvtColor(card,cv2.COLOR_BGR2RGB)
plt.imshow(card_rgb)
plt.title("Reference:Visiting Card")
plt.axis("off")
plt.show()

#measure card size in pixels
card_height,card_width,_ = card.shape

#known size in mm
real_width_mm = 88
real_height_mm = 50

#compute pixel-to-mm ratio
pixels_per_mm_x = card_width / real_width_mm
pixels_per_mm_y = card_height / real_height_mm

print("pixels per mm(X):",pixels_per_mm_x)
print("pixels per mm(Y):",pixels_per_mm_y)

#manually crop ruler(adjust coordinates as needed)
ruler = image[225:300,186:547]#[y1:y2,x1,x2]

#show object
ruler_rgb = cv2.cvtColor(ruler,cv2.COLOR_BGR2RGB)
plt.imshow(ruler_rgb)
plt.title("Ruler")
plt.axis("off")
plt.show()

#Measure in pixels
ruler_height_px,ruler_width_px,_ = ruler.shape

#convert to mm using reference card ratio
ruler_width_mm = ruler_width_px / pixels_per_mm_x
ruler_height_mm = ruler_height_px / pixels_per_mm_y

print("ruler Width(mm):",round(ruler_width_mm,2))
print("ruler height(mm):",round(ruler_height_mm,2))
