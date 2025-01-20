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


@app.route('/api/data/all', methods=['GET'])
def get_all_cars():
    cars_data = get_cars_data()
    return jsonify(cars_data)

@app.route('/api/data/<int:id>', methods=['GET'])
def get_car_details(id):

    conn = sqlite3.connect('./../db/data.sqlite')
    cursor = conn.cursor()


    cursor.execute("SELECT car_cropped_image, licence_plate_cropped_image FROM cars WHERE id = ?", (id,))
    data = cursor.fetchone()

    conn.close()

    if data:
        car_image_path, plate_image_path = data
        return send_file(car_image_path), send_file(plate_image_path)
    else:
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=False)
