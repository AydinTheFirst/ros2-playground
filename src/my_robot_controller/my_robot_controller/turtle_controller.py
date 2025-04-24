import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller_node")

        self.publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

        self.timer = self.create_timer(1.0, self.timer_callback)

        self.count = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg.linear.x}, {msg.angular.z}")
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
