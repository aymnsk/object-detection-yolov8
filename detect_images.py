import os
from ultralytics import YOLO
import cv2

# Load YOLOv8n model (lightweight, works well on 4GB RAM)
model = YOLO("yolov8n.pt")

# Input and output folders
input_folder = "images"
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

# Loop through all images
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        print(f"Processing {filename}...")

        # Run detection
        results = model(img_path)[0]  # first result

        # Plot results
        result_img = results.plot()

        # Save output image
        out_path = os.path.join(output_folder, filename)
        cv2.imwrite(out_path, result_img)

print("✅ Object detection completed. Check the 'results/' folder.")
