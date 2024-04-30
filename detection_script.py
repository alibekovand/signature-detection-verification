from ultralytics import YOLO

model = YOLO("detection\\train\weights\\best.pt")

results = model(source=0, show=True, conf=0.3, save=True)

#source = 'detection\\test1.jpg'
#results = model(source, conf=0.4, save=True)