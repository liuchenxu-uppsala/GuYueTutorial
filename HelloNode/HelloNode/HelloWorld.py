import rclpy
import time
from rclpy.node import Node

def main():
    rclpy.init()
    node_hello = Node('HelloWorld')
    while rclpy.ok():
        node_hello.get_logger().info('HelloWorld')
        time.sleep(1)
    node_hello.destroy_client()
    rclpy.shutdown()