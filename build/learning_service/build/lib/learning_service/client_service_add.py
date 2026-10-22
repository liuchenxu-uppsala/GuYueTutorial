import sys
import rclpy
from rclpy.node import Node
from learning_interface.srv import AddTwoInts

class AddClient(Node):
    def __init__(self):
        super().__init__('AddClient')
        self.client = self.create_client(AddTwoInts,'add_service')
        while not self.client.wait_for_service(1):
            self.get_logger().info('Service is online now!')
        
    def send_request(self):
        request = AddTwoInts.Request()
        request.a = int(sys.argv[1])
        request.b = int(sys.argv[2])
        self.future = self.client.call_async(request)

def main(argv = None):
    rclpy.init(argv)
    client = AddClient()
    client.send_request()
    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response:AddTwoInts.Response = client.future.result()
            except Exception as e:
                client.get_logger().info(f'error:{e}')
            else:
                client.get_logger().info(f'来自于Service的结果是:{response.sum}')
        break
    client.destroy_node()
    rclpy.shutdown()