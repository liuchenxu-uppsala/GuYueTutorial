import rclpy
import time
from rclpy.node import Node
class HelloNodeClass(Node):
    def __init__(self):
        super().__init__('HelloNodeClass')
        while(rclpy.ok()):
            time.sleep(0.5)
            self.get_logger().info('HelloNodeClass')

def main():
    rclpy.init()
    node_hello = HelloNodeClass()
    rclpy.spin(node_hello)
    node_hello.destroy_node()
    rclpy.shutdown()