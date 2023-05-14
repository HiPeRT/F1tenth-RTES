import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from rclpy.clock import Clock
from datetime import datetime

class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        self.publisher_ = self.create_publisher(String, 'topic_echo', 10)
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        if (msg.data == 'exit'):
            raise SystemExit

        self.get_logger().info(f"I heard: {len(msg.data)} Bytes")
        self.sender(msg)

    def sender(self, msg):
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing to topic_echo: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    listener = Listener()

    try:
        rclpy.spin(listener)
    except SystemExit:
        pass

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
