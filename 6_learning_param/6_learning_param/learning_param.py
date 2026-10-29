import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

class ParamNode(Node):
    def __init__(self):
        super().__init__('SelfParamNode')
        self.declare_parameter('robot_name','mbot')
        self.create_timer(2,None)
    def timer_callback(self):
        new_value = self.get_parameter('robot_name').get_parameter_value().string_value
        self.get_logger().info(f'robot_name:{new_value}')
        para = rclpy.Parameter('robot_name',Parameter.Type.STRING,'mbot')
        all_params = [para]
        self.set_parameters(all_params)

def main():
    rclpy.init()
    param = ParamNode()
    rclpy.spin(param)
    param.destroy_node()
    rclpy.shutdown()