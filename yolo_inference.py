from ultralytics import YOLO

# We use the largest model to have the best accuracy
# model = YOLO('yolov8x')

# Let's test our trained model
model = YOLO('models/best.pt')

# Run the model
results = model.predict('input_videos/08fd33_4.mp4', save=True)
print(results[0])

# Print the value of each bounding boxes for the first frame
for box in results[0].boxes:
    print(box)