import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MsgTalkerNode(Node):

    def __init__(self):
        super().__init__("msg_talker_node")

        self.publisher = self.create_publisher(String, "chatter", 10)

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = input("Enter a message: ")
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = MsgTalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()
