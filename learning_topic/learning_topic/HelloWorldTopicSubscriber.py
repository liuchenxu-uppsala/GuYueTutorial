import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('HelloWorldSubscriber')
        self.create_subscription(String,'HelloWorldTopic',self.subscribtion_callback,10)
    def subscribtion_callback(self,msg):
        message:String = msg
        self.get_logger().info(f'收到消息{message.data}')

def main():
    rclpy.init()
    node  = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()