import streamlit as st
import cv2
import math
import cvzone
import numpy as np
from ultralytics import YOLO
from PIL import Image
from streamlit_image_comparison import image_comparison

model = YOLO("yolov8n.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
"traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
"dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
"handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
"baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
"fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
"carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant", "bed",
"dining table", "toilet", "tv monitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
"microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
"teddy bear", "hair drier", "toothbrush"
]

st.title("YOLO Object Detection")

img = st.file_uploader("Choose any image", accept_multiple_files=False)

def predict(img):
    data = Image.open(img)
    img_array = np.array(data)
    
    result = model(img_array)
    
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            
            conf = math.ceil((box.conf[0])*100)/100
            cls = int(box.cls[0])
            curr_cls = classNames[cls]
            
            cvzone.cornerRect(img_array, (x1, y1, w, h))
            cvzone.putTextRect(img_array, f'{curr_cls} {conf}', (max(0, x1), max(35, y1)))
    
    return Image.fromarray(img_array)

if img is not None:
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Detect"):
        result_img = predict(img)
        image_comparison(
            img1 = Image.open(img),
            img2 = result_img
        )