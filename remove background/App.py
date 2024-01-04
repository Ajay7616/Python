import os
import cv2
import numpy as np
import mediapipe as mp

image_paths = [
    "img1.jpg",
    "img2.jpg"
]

image_index = 0
bg_image = cv2.imread(image_paths[image_index])

mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    height, width, channel = frame.shape
    
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = selfie_segmentation.process(RGB)
    mask = results.segmentation_mask
    condition = np.stack((results.segmentation_mask,) * 3, axis=2) > 0.5

    bg_image_resized = cv2.resize(bg_image, (width, height))
    output_image = np.where(condition, frame, bg_image_resized)

    cv2.imshow("Output", output_image)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        image_index = (image_index + 1) % len(image_paths)
        bg_image = cv2.imread(image_paths[image_index])

cap.release()
cv2.destroyAllWindows()