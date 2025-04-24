import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__("obstacle_avoidance")
        self.subscription = self.create_subscription(
            LaserScan, "/scan", self.listener_callback, 10
        )
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.twist = Twist()

    def listener_callback(self, msg):
        # Lidar verilerini alıyoruz
        ranges = msg.ranges
        # Etrafımızda bir engel olup olmadığını kontrol ediyoruz
        if min(ranges) < 1.0:  # Eğer bir engel 1 metreden daha yakınsa
            self.twist.linear.x = 0.0  # Dur
            self.twist.angular.z = 1.0  # Dön
        else:
            self.twist.linear.x = 0.5  # İleri git
            self.twist.angular.z = 0.0  # Dönme
        # Robotu hareket ettiriyoruz
        self.publisher.publish(self.twist)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    rclpy.shutdown()
