import streamlit as st
import cv2
import math
import cvzone
import numpy as np
from ultralytics import YOLO
from PIL import Image

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

def process_frame(frame):
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            curr_cls = classNames[cls]
            cvzone.cornerRect(frame, (x1, y1, w, h), l=9)
            cvzone.putTextRect(frame, f'{curr_cls} {conf}', (max(0, x1), max(35, y1)), 
                               scale=1, thickness=1)
    return frame

def live_camera():
    col1, col2, col3, col4, col5 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open camera.")
        return
    
    stframe = st.empty()
    run = col3.checkbox('Start Detection')
    
    if not run:
        col13.caption("check to start your camera")
    
    while run:
        ret, frame = cap.read()
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        processed_frame = process_frame(frame)
        stframe.image(processed_frame)
    
    cap.release()

def from_video():
    video = st.file_uploader("Choose video to upload", type=["mp4", "avi", "mov"])
    col1, col2, col3, col4, col5 = st.columns(5)
    
    if video is not None:
        
        if st.button("Detect Objects in Video"):
            tfile = st.empty()
            tfile.write("Processing video...")
        
            temp_file = video.name + ".mp4"
            with open(temp_file, "wb") as f:
                f.write(video.getbuffer())
        
            video_capture = cv2.VideoCapture(temp_file)
            if not video_capture.isOpened():
                st.error("Error: Could not open video file.")
                return
        
            stframe = st.empty()
        
            while video_capture.isOpened():
                ret, frame = video_capture.read()
            
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                processed_frame = process_frame(frame)
                stframe.image(processed_frame)
        
            video_capture.release()
            tfile.write("Processing complete!")
    else:
        col3.write("Upload a video file to begin.")

st.subheader("Select detection mode")
detection_mode = st.radio("", ('From Video', 'Live Camera'), horizontal=True)
st.divider()

if detection_mode == 'From Video':
    from_video()
elif detection_mode == 'Live Camera':
    live_camera()