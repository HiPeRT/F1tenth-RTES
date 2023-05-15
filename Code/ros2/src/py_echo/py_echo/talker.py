import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from time import sleep

from rclpy.clock import Clock
from datetime import datetime, timedelta

class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.i = 1
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.sender_callback)
        self.subscription = self.create_subscription(
            String,
            'topic_echo',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def sender_callback(self):
        self.timer.cancel()
        msg = String()
        msg.data = 'a' * 2 * self.i     # send multiple of 2 byte
        self.message = msg.data

        # Get timestamp with rclpy
        self.now = Clock().now()
        #self.get_logger().info(f"[RCLPY] Current time for {msg.data}: {now.nanoseconds}") # Print it

        # Get timestap with UNIX
        self.nowUnix = datetime.now()
        #self.get_logger().info(f"[UNIX] Current time for {msg.data}: {nowUnix.time().microsecond}")  # Print it

        self.publisher_.publish(msg)
        #self.get_logger().info(f"Publishing: {msg.data}")
        self.i += 1

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)

        # Get timestamp with rclpy
        now = Clock().now()
        #self.get_logger().info(f"[RCLPY] Current time for {msg.data}: {now.nanoseconds}") # Print it

        # Get timestap with UNIX
        nowUnix = datetime.now()
        #self.get_logger().info(f"[UNIX] Current time for {msg.data}: {nowUnix.time().microsecond}")  # Print it

        print(f"[RCLPY] {len(self.message)} {now.nanoseconds - self.now.nanoseconds}")
        print(f"[UNIX] {len(self.message)} {(nowUnix - self.nowUnix) // timedelta(microseconds=1)}")

        if self.i <= 400:
            self.sender_callback()
        else:
            msg = String()
            msg.data = 'exit'
            self.publisher_.publish(msg)
            sleep(1)    # Make sure the exit command is sent
            raise SystemExit


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()

    try:
        rclpy.spin(talker)
    except SystemExit:
        pass

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()