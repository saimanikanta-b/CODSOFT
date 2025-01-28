import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
known_image_path = "C:\\Users\\SAI MANIKANTA\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-10-04 222112.jpg"
try:
    known_face = DeepFace.represent(known_image_path, model_name="ArcFace", enforce_detection=False)[0]
    print("Face representation obtained successfully!")
except ValueError as e:
    print(f"Error: {e}")
known_face = DeepFace.represent(known_image_path, model_name="ArcFace")[0]
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        detected_face = frame[y:y + h, x:x + w]
        try:
            result = DeepFace.verify(detected_face, known_image_path, model_name='ArcFace')
            if result["verified"]:
                name = "Mani"
            else:
                name = "Unknown"
        except Exception as e:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Face Detection and Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()