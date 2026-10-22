import rclpy
from rclpy.node import Node
from learning_interface.srv import AddTwoInts
class AddServer(Node):
    def __init__(self):
        super().__init__('AddServer')
        self.create_service(AddTwoInts,'add_service',self.add_callback)
    def add_callback(self,request:AddTwoInts.Request,resposne:AddTwoInts.Response):
        self.get_logger().info(f'收到消息:{request.a} + {request.b}')
        resposne.sum = request.a + request.b
        return resposne

def main():
    rclpy.init()
    service = AddServer()
    rclpy.spin(service)
    service.destroy_node()
    rclpy.shutdown()
