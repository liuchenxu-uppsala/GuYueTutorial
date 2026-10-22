import rclpy
from rclpy.node import Node
from learning_interface.srv import GetObjectPosition
import time

class WebCamClient(Node):
    def __init__(self):
        super().__init__('WebCamClient')
        self.client = self.create_client(GetObjectPosition,'GetObjectPosition')
        while not self.client.wait_for_service(1):
            self.get_logger().info('Server is not online now')
    def send_request(self):
        request = GetObjectPosition.Request()
        request.get = True
        self.future = self.client.call_async(request)


def main():
    rclpy.init()
    node  = WebCamClient()
    while rclpy.ok():
        node.send_request()
        rclpy.spin_until_future_complete(node,node.future)
        if node.future.done():
            try:
                response:GetObjectPosition.Response = node.future.result()
            except Exception as e:
                node.get_logger().info(f'error:{e}')
            else:
                node.get_logger().info(f'物体的左上角的坐标是{response.x},{response.y}')
        time.sleep(1.0) 
            
     