#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherPy(Node):
    def __init__(self):
        super().__init__('publisher_py_node')
        self.publisher_ = self.create_publisher(String, '/chatter_topic', 10)
        self.timer = self.create_timer(1.5, self.timer_callback)
        self.i = 0
        self.get_logger().info('Publisher Python iniciado.')

    def timer_callback(self):
        msg = String()
        msg.data = f'[PYTHON Publisher] Mensaje #{self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherPy()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    