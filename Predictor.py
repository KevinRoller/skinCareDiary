from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

class predictor():
    def __init__(self,path):
        self.model = YOLO(path)
    def __call__(self,img):    
        results = self.model.predict(
            img, classes=0)
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs

        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2RGB)
        count=0
        for box in boxes.xyxy:
            count+=1
            cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(
                box[3])), color=(0, 0, 255), lineType=cv2.LINE_AA, thickness=1)
        return img,count



