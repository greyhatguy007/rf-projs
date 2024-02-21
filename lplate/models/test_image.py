import cv2
import easyocr
import numpy as np
import sqlite3
from datetime import datetime
import base64
from ultralytics import YOLO

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Connect to SQLite database
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS cars
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TIMESTAMP,
                   licence_plate_number TEXT,
                   location TEXT,
                   car_cropped_image TEXT,
                   licence_plate_cropped_image TEXT)''')

# Load the image
image_path = "./../image.png"
image = cv2.imread(image_path)
model = YOLO("yolov8n.pt")
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
                print(x_min_license, x_max_license, y_min_license,
                      y_max_license, license_plate_text, conf)

                # Get current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Define the license plate region (full bounding box)
                license_plate_region = car_region[y_min_license:y_max_license,
                                                  x_min_license:x_max_license]

                # Convert images to base64 strings
                _, car_cropped_image_encoded = cv2.imencode('.jpg', car_region)
                car_cropped_image_base64 = base64.b64encode(
                    car_cropped_image_encoded).decode('utf-8')
                _, license_plate_cropped_image_encoded = cv2.imencode(
                    '.jpg', license_plate_region)
                license_plate_cropped_image_base64 = base64.b64encode(
                    license_plate_cropped_image_encoded).decode('utf-8')

                # Insert data into SQLite database
                cursor.execute('''INSERT INTO cars
                                  (timestamp, licence_plate_number, location, car_cropped_image, licence_plate_cropped_image)
                                  VALUES (?, ?, ?, ?, ?)''',
                               (timestamp, license_plate_text, image_path, car_cropped_image_base64, license_plate_cropped_image_base64))
                conn.commit()
            except Exception as e:
                print("Error:", e)
