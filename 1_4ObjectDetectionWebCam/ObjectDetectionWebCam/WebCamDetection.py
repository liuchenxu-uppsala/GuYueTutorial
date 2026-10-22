import rclpy
from rclpy.node import Node
import numpy as np
import cv2

lower_red = np.array([0, 90, 128])
upper_red = np.array([180, 255, 255])
def detect_apple(img):
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask_red = cv2.inRange(hsv_img,lower_red,upper_red)
    contours,_ = cv2.findContours(mask_red,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        if cnt.shape[0] < 150:
            continue
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
        cv2.circle(img, (int(x+w/2), int(y+h/2)), 5, (0, 255, 0), -1)
    cv2.imshow("object", img)                                                    # 使用OpenCV显示处理后的图像效果
    cv2.waitKey(50)
    cv2.destroyAllWindows()

def main():
    rclpy.init()
    node = Node('DetectApple')
    node.get_logger().info('Start Detect')
    cp = cv2.VideoCapture(0)
    while rclpy.ok():
        ret,img = cp.read()
        if ret:
            detect_apple(img)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()