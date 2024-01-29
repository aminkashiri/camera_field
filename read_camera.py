import cv2
import apriltag
import matplotlib.pyplot as plt

# cap = cv2.VideoCapture("http://192.168.0.15:4747/video?640x480")
# while True:
#     ret, frame = cap.read()



#     cv2.imshow("frame", frame)
#     cv2.waitKey(1)

def find_apriltags(show_image=True):
    img = cv2.imread("frame_0.jpg", cv2.IMREAD_GRAYSCALE)
    detector = apriltag.Detector()
    result = detector.detect(img)
    for i in range(10):
        print("-------------------")
        corners = result[i].corners
        # print(dir(result[i]))
        # print(result[0].count(True))
        print(result[i].index(0))
        # print(result[i].tag_id)
        # print(result[i].tag_family)
        print(result[i].tostring())

    if show_image:
        plt.imshow(img)
        plt.scatter(corners[:, 0], corners[:, 1])
        # plt.scatter(corners[0, 0], corners[0, 1], c="green")
        # plt.scatter(corners[1, 0], corners[1, 1], c ="red")
        plt.show()
    return corners

find_apriltags(show_image=False)