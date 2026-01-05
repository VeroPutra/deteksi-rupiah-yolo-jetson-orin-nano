from ultralytics import YOLO
import cv2

model = YOLO("Uang.pt")

cap = cv2.VideoCapture(0)  # USB camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO - Jetson USB Camera", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()