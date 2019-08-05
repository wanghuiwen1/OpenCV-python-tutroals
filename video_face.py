import time

import cv2
import imutils
import numpy as np
from imutils.video import VideoStream
import face_recognition


image = face_recognition.load_image_file("./resource/wanghuiwen.jpeg")
wanghuiwen = face_recognition.face_encodings(image)[0]

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("resource/deploy.prototxt", "resource/res10_300x300_ssd_iter_140000.caffemodel")

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    time.sleep(0.001)
    #从线程视频流中抓取帧并调整其大小
    #最大宽度为400像素
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # 抓住框架尺寸并将其转换为blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    #
    # # 通过网络传递blob并获取检测和预测
    net.setInput(blob)
    detections = net.forward()
    #
    # # 在detectionsq上循环
    for i in range(0, detections.shape[2]):
        # 提取与之相关的置信度（即概率）
        # 预测
        confidence = detections[0, 0, i, 2]

        # 通过确保“置信度”大于最小置信度来过滤弱检测
        if confidence < 0.5:
            continue
    #     #计算边界框的（x，y）坐标t
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        # 检测到的人脸
        face = frame[startY:endY, startX:endX]

        unknown_face_encodings = face_recognition.face_encodings(face)
        if(len(unknown_face_encodings)>0):
            results = face_recognition.compare_faces([wanghuiwen], unknown_face_encodings[0])
            for j in range(len(results)):
                if results[j]:
                    print("wanghuiwen")
        cv2.imshow("1",face)

        # 绘制面部的边界框以及相关的边框

        # text = "{:.2f}%".format(confidence * 100)
        # y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        # cv2.putText(frame, text, (startX, y),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    #
    # # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
