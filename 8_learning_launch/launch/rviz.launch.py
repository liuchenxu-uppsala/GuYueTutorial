import os
from launch_ros.actions import Node  
from ament_index_python import get_package_share_directory
from launch import LaunchDescription


def generate_launch_description():
    rviz_config = os.path.join(get_package_share_directory('8_learning_launch'),'rviz','turtle_rviz.rviz')
    return LaunchDescription(
        [Node(package = 'rviz2',executable='rviz2',name='rviz2',arguments=['-d',rviz_config])]
    )