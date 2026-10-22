import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class PublisherCam(Node):
    def __init__(self):
        super().__init__('PublisherCam')
        self.pub = self.create_publisher(Image,'image_raw',10)
        self.cap = cv2.VideoCapture(0)
        self.CvBridge = CvBridge()
        self.create_timer(0.01,self.webCamCallback)
    def webCamCallback(self):
        ret,frame = self.cap.read()
        if ret == True:
            self.pub.publish(self.CvBridge.cv2_to_imgmsg(frame,'bgr8'))
        self.get_logger().info('Publishing video frame')

def main():
    rclpy.init()
    publisher = PublisherCam()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()
