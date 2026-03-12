from ultralytics import YOLO

model = YOLO("yolo26l.pt")
results = model.predict('input_videos/sample.mp4', save=True) 
print(results[0])
print("===========================================")
for i in results[0].boxes:
    print(i)

