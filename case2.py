import numpy as np
import cv2

# 相机读取视屏
# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# # 文件读取视屏
#
# cap = cv2.VideoCapture('D:\\PycharmProjects\\untitled\\output.avi')
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# 保存视频
#
# cap = cv2.VideoCapture('C:\\Users\\Administrator\\Videos\\trailer.mp4')
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (854,480))
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
#
#         # write the flipped frame
#         out.write(frame)
#
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()