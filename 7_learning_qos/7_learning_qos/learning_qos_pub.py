from mpi4py import rc

import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from std_msgs.msg import String
class QosPub(Node):
    def __init__(self):
        super().__init__('QosPub')
        qos_config = QoSProfile(
            history = HistoryPolicy.KEEP_LAST,
            depth = 10,
            reliability = ReliabilityPolicy.BEST_EFFORT,
            durability = DurabilityPolicy.VOLATILE
        )
        self.i = 0
        self.pub = self.create_publisher(String,'qos_message',qos_config)
        self.timer = self.create_timer(1,self.timer_callback)
    def timer_callback(self):
        data = String()
        data.data = f'发送消息:{self.i}'
        self.pub.publish(data)
        self.get_logger().info(f'发送消息:{self.i}')
        self.i = self.i + 1

def main():
    rclpy.init()
    node = QosPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()