from rclpy.impl.implementation_singleton import package
from launch_ros.actions import Node  

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([
        Node(package = '7_learning_qos',executable='publisher'),
        Node(package = '7_learning_qos',executable='sub')]
    )