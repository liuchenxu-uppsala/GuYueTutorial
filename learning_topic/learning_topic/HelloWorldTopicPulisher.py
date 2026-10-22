import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('HelloWorldPublisher')
        self.pb = self.create_publisher(String,'HelloWorldTopic',10)
        self.create_timer(0.5,self.publisher_callback)
    def publisher_callback(self):
        msg = String()
        msg.data = 'HelloWorldTopic'
        self.pb.publish(msg)
        self.get_logger().info(f'发布了消息{msg.data}')
def main():
    rclpy.init()
    node  = Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()