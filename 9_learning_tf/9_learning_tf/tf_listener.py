from gettext import translation

import rclpy
import tf_transformations
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener


class TFListener(Node):
    def __init__(self):
        super().__init__('TFListener')
        self.declare_parameter('source', 'world')
        self.declare_parameter('target', 'house')
        self.world = self.get_parameter('source')
        self.target = self.get_parameter('target')
        self.buffer = Buffer()
        TransformListener(self.buffer, self)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        now = Time()
        trans = self.buffer.lookup_transform('world', 'house', now)
        pos = trans.transform.translation
        roat = trans.transform.rotation
        euler = tf_transformations.euler_from_quaternion([roat.x, roat.y, roat.z, roat.w])
        self.get_logger().info(
            f'Get {self.world} -> {self.target} transform:{pos.x},{pos.y},{pos.z},{euler[0]},{euler[1]},{euler[2]}'
        )


def main():
    rclpy.init()
    node = TFListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
