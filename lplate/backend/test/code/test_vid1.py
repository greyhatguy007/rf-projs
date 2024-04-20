import cv2
import easyocr
import numpy as np
import sqlite3
from datetime import datetime
import base64
from ultralytics import YOLO
import time

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Connect to SQLite database
conn = sqlite3.connect('./../../db/data.sqlite')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS cars
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TIMESTAMP,
                   licence_plate_number TEXT,
                   location TEXT,
                   car_cropped_image TEXT,
                   licence_plate_cropped_image TEXT)''')

# Initialize YOLO model
model = YOLO("./../../models/yolov8n.pt")

# Video path
video_path = "./demo.mp4"
video_capture = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not video_capture.isOpened():
    print("Error: Unable to open video.")
    exit()

# Start time
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        break

    # Perform prediction
    results = model.predict(source=frame, conf=0.6)

    # Iterate over detected objects
    for result in results:
        # Iterate over class IDs and bounding box coordinates
        for class_id, box_tensor in zip(result.boxes.cls, result.boxes.xyxy):
            # Convert the class ID to a regular Python integer
            class_id = int(class_id)

            # Check if the detected object is a car (assuming class ID 2 represents cars)
            if class_id == 2 or class_id == 3 or class_id == 5 or class_id == 7:
                # Convert the bounding box tensor to a list of coordinates
                box_coordinates = box_tensor.tolist()

                # Extract the bounding box coordinates
                x_min, y_min, x_max, y_max = map(int, box_coordinates)

                # Extract the region of the car
                try:
                    car_region = frame[y_min:y_max, x_min:x_max]

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
                    _, car_cropped_image_encoded = cv2.imencode(
                        '.jpg', car_region)
                    car_cropped_image_base64 = base64.b64encode(
                        car_cropped_image_encoded).decode('utf-8')
                    _, license_plate_cropped_image_encoded = cv2.imencode(
                        '.jpg', license_plate_region)
                    license_plate_cropped_image_base64 = base64.b64encode(
                        license_plate_cropped_image_encoded).decode('utf-8')

                    # Check if the vehicle has been detected in the last 90 seconds
                    cursor.execute(
                        "SELECT timestamp FROM cars WHERE licence_plate_number = ? ORDER BY timestamp DESC LIMIT 1", (license_plate_text,))
                    last_detection = cursor.fetchone()

                    if last_detection:
                        last_timestamp = datetime.strptime(
                            last_detection[0], '%Y-%m-%d %H:%M:%S')
                        elapsed_time = (datetime.now() -
                                        last_timestamp).total_seconds()
                        if elapsed_time < 90:
                            print(
                                "Vehicle already detected within the last 90 seconds. Skipping entry.")
                            continue

                    # Insert data into SQLite database
                    cursor.execute('''INSERT INTO cars
                                      (timestamp, licence_plate_number, location, car_cropped_image, licence_plate_cropped_image)
                                      VALUES (?, ?, ?, ?, ?)''',
                                   (timestamp, license_plate_text, video_path, car_cropped_image_base64, license_plate_cropped_image_base64))
                    conn.commit()
                except Exception as e:
                    print("Error:", e)

    # Check if the elapsed time is over 90 seconds
    if time.time() - start_time > 90:
        print("Exiting after 90 seconds.")
        break

# Release the video capture object and close the database connection
video_capture.release()
conn.close()
