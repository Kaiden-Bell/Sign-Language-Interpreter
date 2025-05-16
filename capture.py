import cv2
import os
from pathlib import Path


SIGN_CLASS = 'A' # MUST BE CHANGED FOR EACH SIGN
SAVE_DIR = f'data/fingerspellings/{SIGN_CLASS}/'


if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = os.path.join(SAVE_DIR, f'{SIGN_CLASS}_{count}.jpg')
        cv2.imwrite(img_path, frame)
        print(f"[INFO] Saved: {img_path}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
