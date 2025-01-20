import time
from ultralytics import YOLO
import cv2
import easyocr
import numpy as np
import base64

# Initialize YOLO model
model = YOLO("./../../models/yolov8n.pt")

# Initialize EasyOCR
# You can specify the languages you want to support
reader = easyocr.Reader(['en'])

# image_path = input('Enter Path: ')
image_path = "./../images/image.png"

while True:
    # Load the image

    image = cv2.imread(image_path)

    # Perform prediction
    results = model.predict(source=image_path, show=True, conf=0.6)

    # Iterate over detected objects
    for result in results:
        # Iterate over class IDs and bounding box coordinates
        for class_id, box_tensor in zip(result.boxes.cls, result.boxes.xyxy):
            # Convert the class ID to a regular Python integer
            class_id = int(class_id)

            # Check if the detected object is a car (assuming class ID 2 represents cars)
            if class_id == 2 or 3 or 5 or 7:
                # Convert the bounding box tensor to a list of coordinates
                box_coordinates = box_tensor.tolist()

                # Extract the bounding box coordinates
                x_min, y_min, x_max, y_max = map(int, box_coordinates)

                # Extract the region of the car
                try:
                    car_region = image[y_min:y_max, x_min:x_max]
                    # Convert the car region to JPEG format (you can use other formats like PNG as well)

                    # Apply blackhat filtering to enhance contrast
                    kernel = np.ones((5, 5), np.uint8)
                    blackhat = cv2.morphologyEx(
                        car_region, cv2.MORPH_BLACKHAT, kernel)

                    # Perform text recognition on the preprocessed car region using EasyOCR
                    result = reader.readtext(blackhat)

                    # Check if EasyOCR successfully recognized any text
                    print(f'Result : {result}')
                    license_plate_text = result[0][1]
                    x_coordinates = [point[0] for point in result[0][0]]
                    y_coordinates = [point[1] for point in result[0][0]]
                    x_min_license = min(x_coordinates)
                    x_max_license = max(x_coordinates)
                    y_min_license = min(y_coordinates)
                    y_max_license = max(y_coordinates)
                    conf = result[0][2]
                    print(x_min_license, x_max_license, y_min_license, y_max_license, license_plate_text, conf)
                except:
                    pass

    # Wait for 2 seconds
    time.sleep(2)
