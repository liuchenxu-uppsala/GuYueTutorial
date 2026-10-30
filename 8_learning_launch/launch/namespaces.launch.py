import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    parameter_yaml = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('8_learning_launch'),'launch','parameters_yaml.launch.py'))
    )
    return LaunchDescription(
        [parameter_yaml]
    )