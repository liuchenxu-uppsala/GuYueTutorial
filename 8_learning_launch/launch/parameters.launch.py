import rclpy
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.logging import LaunchConfig
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    back_ground_r = DeclareLaunchArgument('r', default_value='130')
    back_ground_g = DeclareLaunchArgument('g', default_value='110')
    back_ground_b = DeclareLaunchArgument('b', default_value='198')
    back_ground_test = DeclareLaunchArgument('ghost', default_value='100')
    return LaunchDescription(
        [
            back_ground_r,
            back_ground_g,
            back_ground_b,
            Node(
                package='turtlesim',
                executable='turtlesim_node',
                name='sim',
                parameters=[
                    {
                        'background_r': LaunchConfiguration('r'),
                        'background_g': LaunchConfiguration('g'),
                        'background_b': LaunchConfiguration('b'),
                    }
                ],
            ),
        ]
    )
