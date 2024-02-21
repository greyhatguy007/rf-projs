import time
from ultralytics import YOLO

# Initialize YOLO model
model = YOLO("yolov8l.pt")

# Function to print predictions
def print_predictions(results):
    # Extract predictions for img1
    predictions = results.pandas().xyxy[0]

    # Iterate through predictions and print label and bounding box coordinates
    for _, row in predictions.iterrows():
        label = row['name']
        coordinates = (row['xmin'], row['ymin'], row['xmax'], row['ymax'])
        print(f"Label: {label}, Coordinates: {coordinates}")

# Main loop
while True:
    # Perform prediction
    results = model.predict(source="http://192.168.29.170:8080/video", show=True, conf=0.4)
    
    # Print predictions
    print_predictions(results)
    
    # Wait for 2 seconds
    time.sleep(2000)

