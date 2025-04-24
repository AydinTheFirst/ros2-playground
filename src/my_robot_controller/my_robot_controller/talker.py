import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TalkerNode(Node):
    def __init__(self):
        super().__init__("talker_node")

        # Create a publisher for the "chatter" topic
        self.publisher = self.create_publisher(String, "chatter", 10)

        # Create a timer to publish messages periodically
        self.timer = self.create_timer(1.0, self.timer_callback)

        # Initialize the message counter
        self.count = 10

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello, world! {self.count}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.count += 10


def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()
