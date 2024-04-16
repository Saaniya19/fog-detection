from ultralytics import YOLO

model = YOLO('runs/classify/train6/weights/best.pt')
results = model('fog-super-small-set/val/normal')