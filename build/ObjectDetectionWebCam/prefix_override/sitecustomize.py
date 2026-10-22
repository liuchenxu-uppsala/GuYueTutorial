import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/dobot_ws/shared/ros_ws/ROS_GuYue_ROS2_Tutorial/src/install/ObjectDetectionWebCam'
