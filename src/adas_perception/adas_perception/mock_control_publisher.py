import rclpy
from rclpy.node import Node
from adas_msgs.msg import ControlCommand



class MockControlPublisher(Node):
    def __init__(self):
        super().__init__('mock_control_publisher')


        self.declare_parameter('test_mode', 'normal')

        self.test_mode = self.get_parameter(
            'test_mode'
        ).get_parameter_value().string_value

        self.publisher_ = self.create_publisher(
            ControlCommand,
            '/control/command',
            10
        )

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.throttle = 0.0
        self.steering = 0.0

    def timer_callback(self):
        msg = ControlCommand()

        msg.throttle = self.throttle
        msg.brake = 0.0
        msg.steering = self.steering

        if self.test_mode == 'aggressive':
            self.throttle += 0.1
        else:
            self.throttle += 0.05


        self.publisher_.publish(msg)

        self.throttle += 0.05
        if self.throttle > 1.0:
            self.throttle = 0.0

        self.steering += 0.1
        if self.steering > 0.5:
            self.steering = -0.5
def main(args=None):
    rclpy.init(args=args)
    node = MockControlPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()