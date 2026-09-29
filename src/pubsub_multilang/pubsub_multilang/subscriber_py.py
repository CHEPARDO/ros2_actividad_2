#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberPy(Node):
    def __init__(self):
        super().__init__('subscriber_py_node')
        self.subscription = self.create_subscription(
            String, '/chatter_topic', self.listener_callback, 10)
        self.get_logger().info('Subscriber Python escuchando...')

    def listener_callback(self, msg):
        self.get_logger().info(f'[PYTHON Subscriber] Recibido: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberPy()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()