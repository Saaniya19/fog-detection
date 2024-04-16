from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

# Train the model
model.train(data='C:/Users/saaniya.saraf/Documents/fog-super-small-set', epochs=50, imgsz=64)