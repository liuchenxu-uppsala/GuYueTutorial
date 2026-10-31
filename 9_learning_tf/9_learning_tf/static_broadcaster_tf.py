import rclpy
import tf_transformations
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


class StaticTFBroadcaster(Node):
    def __init__(self):
        super().__init__('StaticTFBroadcaster')
        self.broad_caster = StaticTransformBroadcaster(self)
        static_transform_stamped = TransformStamped()
        static_transform_stamped.header.stamp = self.get_clock().now().to_msg()
        static_transform_stamped.header.frame_id = 'world'
        static_transform_stamped.child_frame_id = 'house'
        static_transform_stamped.transform.translation.x = 10.0
        static_transform_stamped.transform.translation.y = 0.0
        static_transform_stamped.transform.translation.z = 0.0
        quanter = tf_transformations.quaternion_from_euler(0, 0, 0)
        static_transform_stamped.transform.rotation.x = quanter[0]
        static_transform_stamped.transform.rotation.y = quanter[1]
        static_transform_stamped.transform.rotation.z = quanter[2]
        static_transform_stamped.transform.rotation.w = quanter[3]
        self.broad_caster.sendTransform(static_transform_stamped)


def main():
    rclpy.init()
    node = StaticTFBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
