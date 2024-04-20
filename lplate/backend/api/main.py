from flask import Flask, jsonify, send_file
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Function to fetch data from the 'cars' table
def get_cars_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('./../db/data.sqlite')
    cursor = conn.cursor()

    # Execute a query to fetch data from the 'cars' table
    cursor.execute("SELECT * FROM cars")
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert data to JSON format
    cars_list = []
    for row in data:
        car = {
            "id": row[0],
            "timestamp": row[1],
            "license_plate_number": row[2],
            "location": row[3],
            "car_cropped_image": row[4],
            "license_plate_cropped_image": row[5]
        }
        cars_list.append(car)

    return cars_list

# Define a route to return JSON data for all cars
@app.route('/api/data/all', methods=['GET'])
def get_all_cars():
    cars_data = get_cars_data()
    return jsonify(cars_data)

# Define a route to return cropped car image and license plate image for a specific car ID
@app.route('/api/data/<int:id>', methods=['GET'])
def get_car_details(id):
    # Connect to the SQLite database
    conn = sqlite3.connect('./../db/data.sqlite')
    cursor = conn.cursor()

    # Execute a query to fetch data for the specified car ID
    cursor.execute("SELECT car_cropped_image, licence_plate_cropped_image FROM cars WHERE id = ?", (id,))
    data = cursor.fetchone()

    # Close the database connection
    conn.close()

    if data:
        car_image_path, plate_image_path = data
        # Return the images as files
        return send_file(car_image_path), send_file(plate_image_path)
    else:
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=False)
