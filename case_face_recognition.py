import face_recognition
import cv2

names = [
    "wanghuiwen",
]


images = []
for name in names:
    filename = "./face/" + name + ".png"
    image = face_recognition.load_image_file(filename)
    images.append(image)

unknown_image = face_recognition.load_image_file("./resource/wanghuiwen.jpeg")


face_encodings = []
for image in images:
    encoding = face_recognition.face_encodings(image)[0]
    face_encodings.append(encoding)

unknown_face_encodings = face_recognition.face_encodings(unknown_image)

face_locations = face_recognition.face_locations(unknown_image)
for i in range(len(unknown_face_encodings)):
    unknown_encoding = unknown_face_encodings[i]
    results = face_recognition.compare_faces(face_encodings, unknown_encoding)
    for j in range(len(results)):
        if results[j]:
            name = names[j]
            cv2.putText(unknown_image, name, (left-10, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

unknown_image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
cv2.imshow("Output", unknown_image_rgb)
cv2.waitKey(0)


unknown_image=face_recognition.load_image_file("unknown.jpg")
biden_encoding=face_recognition.face_encodings(known_image)[0]

unknown_encoding=face_recognition.face_encodings(unknown_image)[0]

results=face_recognition.compare_faces([biden_encoding],unknown_encoding)