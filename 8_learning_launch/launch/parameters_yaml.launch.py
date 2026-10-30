import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import rclpy

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('8_learning_launch'),
        'config',
        'turtlesim.yaml'
    )
    return LaunchDescription(
        [
            Node(
                package='turtlesim',
                executable='turtlesim_node',
                name='sim',
                namespace='turtlesim2',
                parameters=[config],
            )
        ]
    )