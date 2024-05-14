from pathlib import Path
from ultralytics import YOLO
import cv2




def detect(image_path):
    opt = {
    #'weights': '/yolo_files/best.pt',
    'weights': 'D:\work\kaggle\signature-detection-verification\streamlit_app\yolo_files\\best.pt',
    'source': image_path,
    'img_size': 640,
    'conf_thres': 0.25,
    'iou_thres': 0.45,
    'device': '',
    'view_img': False,
    'save_txt': True,
    'save_conf': True,
    'save_crop': True,
    'nosave': True,
    'classes': 1,
    'agnostic_nms': False,
    'augment': False,
    'update': False,
    'project': 'results/yolov8/',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    }
    source, weights, view_img, save_txt, imgsz = opt['source'], opt['weights'], opt['view_img'], opt['save_txt'], opt['img_size']
    save_img = not opt['nosave'] and not source.endswith('.txt')  # save inference images

    # Directories
    #save_dir = increment_path(Path(opt['project']) / opt['name'], exist_ok=opt['exist_ok'])  # increment run
    #(save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir
    model = YOLO(weights)

    results = model([image_path])  # return a list of Results objects

    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        #result.show()  # display to screen
        result.save(filename='yolo_files/results/result.jpg')  # save to disk
        result.save_crop('yolo_files/cropped/')

    return True
