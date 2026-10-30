from struct import pack

from launch_ros.actions import Node 

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package='turtlesim',executable='turtlesim_node',namespace='turtlesim1',name='turtlesim1'),
            Node(package='turtlesim',executable='turtlesim_node',namespace='turtlesim2',name='turtlesim2'),
            Node(package='turtlesim',executable='mimic',remappings = [
                ('/input/pose','/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel','/turtlesim2/turtle1/cmd_vel')
            ],name='mimic')
        ]
    )