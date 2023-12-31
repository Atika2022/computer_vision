from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model

results = model(data="config.yaml", epochs=1)  # predict on an image
