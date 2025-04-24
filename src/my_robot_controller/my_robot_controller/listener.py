import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ListenerNode(Node):
    def __init__(self):
        super().__init__("listener_node")

        # Create a subscription to the "chatter" topic
        self.subscription = self.create_subscription(
            String,
            "chatter",
            self.listener_callback,
            10,
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Received message: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = ListenerNode()

    rclpy.spin(node)
    rclpy.shutdown()
