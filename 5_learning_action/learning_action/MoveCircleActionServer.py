import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
import time
from learning_interface.action import MoveCircle

class MoveCricleAction(Node):
    def __init__(self):
        super().__init__('MoveCricleAction')
        self.actionServer = ActionServer(self,MoveCircle,'MoveCircle',self.exeCallback)
    def exeCallback(self,goal_handle:ServerGoalHandle):
        feedbackMsg = MoveCircle.Feedback()
        for i in range(0,360,10):
            feedbackMsg.state = i
            goal_handle.publish_feedback(feedbackMsg)
            self.get_logger().info(f'feedback现在的值是:{feedbackMsg.state}')
            time.sleep(1)
        goal_handle.succeed()
        result = MoveCircle.Result()
        result.finish = True
        return result
def main():
    rclpy.init()
    actionServer = MoveCricleAction()
    rclpy.spin(actionServer)
    actionServer.destroy_node()
    rclpy.shutdown()