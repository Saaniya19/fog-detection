from ultralytics import YOLO

model = YOLO('runs/classify/train6/weights/best.pt')
results = model('fog-super-small-set/val/foggy', stream=True)

normal = 0
foggy = 0

for result in results:
    probs = result.probs.data
    if probs[0] > probs[1]:
        foggy += 1
    else:
        normal += 1

print(foggy)
print(normal)

