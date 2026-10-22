import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
from learning_interface.srv import GetObjectPosition

lower_red = np.array([0, 90, 128])
upper_red = np.array([180, 255, 255])

class Subscribe(Node):
    def __init__(self):
        super().__init__('SubscribeCam')
        self.x = 0
        self.y = 0
        self.create_subscription(Image,'image_raw',self.camCallback,10)
        self.CVBridge = CvBridge()
        self.servcie = self.create_service(GetObjectPosition,'GetObjectPosition',self.serviceCallback)

    def camCallback(self,msg):
        self.get_logger().info('Receiving video frame')
        img = self.CVBridge.imgmsg_to_cv2(msg,'bgr8')
        self.detect_apple(img)

    def serviceCallback(self,request:GetObjectPosition.Request,response:GetObjectPosition.Response):
        if request.get == True:
            response.x = self.x
            response.y = self.y
            self.get_logger().info(f'请求物体的坐标:{response.x},{response.y}')
        else:
            response.x = 0
            response.y = 0
        return response


    def detect_apple(self,img):
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask_red = cv2.inRange(hsv_img,lower_red,upper_red)
        contours,_ = cv2.findContours(mask_red,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            if cnt.shape[0] < 150:
                continue
            (x,y,w,h) = cv2.boundingRect(cnt)
            self.x = int(x+w/2)
            self.y = int(y+h/2)
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
            cv2.circle(img, (int(x+w/2), int(y+h/2)), 5, (0, 255, 0), -1)
        cv2.imshow("object", img)                                                    # 使用OpenCV显示处理后的图像效果
        cv2.waitKey(10)
        # cv2.destroyAllWindows()

def main():
    rclpy.init()
    node = Subscribe()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
