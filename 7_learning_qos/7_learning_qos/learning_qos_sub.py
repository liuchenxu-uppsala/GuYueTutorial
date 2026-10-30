import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from std_msgs.msg import String

class QosSub(Node):
    def __init__(self):
        super().__init__('QosSub')
        qos_profile = QoSProfile(
            history = HistoryPolicy.KEEP_LAST,
            depth = 10,
            reliability = ReliabilityPolicy.BEST_EFFORT,
            durability = DurabilityPolicy.VOLATILE
        )
        self.sub = self.create_subscription(String,'qos_message',self.sub_callback,qos_profile)
    def sub_callback(self,msg:String):
        self.get_logger().info(f'收到消息{msg.data}')

def main():
    rclpy.init()
    node = QosSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()