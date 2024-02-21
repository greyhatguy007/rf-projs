import sqlite3
import cv2
import numpy as np
import base64

# Connect to SQLite database
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()


def get_images_by_id(id):
    try:
        # Retrieve data from database for the specified ID
        cursor.execute(
            "SELECT car_cropped_image, licence_plate_cropped_image FROM cars WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            # Decode base64 strings to image arrays
            car_cropped_image_base64 = row[0]
            license_plate_cropped_image_base64 = row[1]

            car_cropped_image_encoded = base64.b64decode(
                car_cropped_image_base64)
            car_cropped_image_np = np.frombuffer(
                car_cropped_image_encoded, np.uint8)
            car_cropped_image = cv2.imdecode(
                car_cropped_image_np, cv2.IMREAD_COLOR)

            license_plate_cropped_image_encoded = base64.b64decode(
                license_plate_cropped_image_base64)
            license_plate_cropped_image_np = np.frombuffer(
                license_plate_cropped_image_encoded, np.uint8)
            license_plate_cropped_image = cv2.imdecode(
                license_plate_cropped_image_np, cv2.IMREAD_COLOR)

            return car_cropped_image, license_plate_cropped_image
        else:
            print("No data found for ID:", id)
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None


def show_images(car_cropped_image, license_plate_cropped_image):
    if car_cropped_image is not None and license_plate_cropped_image is not None:
        cv2.imshow("Car Cropped Image", car_cropped_image)
        cv2.imshow("License Plate Cropped Image", license_plate_cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Images not found.")


# Specify the ID of the data you want to retrieve
id_to_retrieve = int(input("Enter ID to retrieve: "))

# Get images from database
car_image, license_plate_image = get_images_by_id(id_to_retrieve)

# Show images
show_images(car_image, license_plate_image)
