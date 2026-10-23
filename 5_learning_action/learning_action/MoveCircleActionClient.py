from rclpy.task import Future
from rclpy.action.client import ClientGoalHandle
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer,ActionClient
from rclpy.action.server import ServerGoalHandle
import time
from learning_interface.action import MoveCircle

class MoveCricleActionClient(Node):
    def __init__(self):
        super().__init__('MoveCricleActionClient')
        self.actionClient = ActionClient(self,MoveCircle,'MoveCircle')
    def sendGoal(self):
        while not self.actionClient.wait_for_server(1):
            self.get_logger().info('Server is not online')
        goal = MoveCircle.Goal()
        goal.enable = True
        goalFuture = self.actionClient.send_goal_async(goal,self.feedbackCallback)
        goalFuture.add_done_callback(self.goalFutureDoneCallback)

    def feedbackCallback(self,feedback_msg:MoveCircle.Impl.FeedbackMessage):
        self.get_logger().info(f'现在的feedback:{feedback_msg.feedback}')
        
    def goalFutureDoneCallback(self,future_:Future):
        goal_handle:ClientGoalHandle = future_.result()
        if not goal_handle.accepted:
            self.get_logger().info('服务端拒绝')
            return
        f:Future = goal_handle.get_result_async()
        f.add_done_callback(self.resultCallback)
    def resultCallback(self,future_:Future):
        result_:MoveCircle.Impl.GetResultService.Response = future_.result()
        self.get_logger().info('最终的Result: {%d}' % result_.result.finish)
def main():
    rclpy.init()
    client = MoveCricleActionClient()
    client.sendGoal()
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()