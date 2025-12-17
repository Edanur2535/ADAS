import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os


class ImageGrayPublisher(Node):
    def __init__(self):
        super().__init__('camera_node')

        self.declare_parameter('publish_rate', 5.0)

        publish_rate = self.get_parameter(
            'publish_rate'
        ).get_parameter_value().double_value


    
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.bridge = CvBridge()

        image_path = '/ros2_ws/src/adas_perception/adas_perception/images/iuc.png'

        if not os.path.exists(image_path):
            self.get_logger().error(f'Image not found: {image_path}')
            return

       
        color_image = cv2.imread(image_path)

    
        self.gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    
        self.timer = self.create_timer(
            1.0 / publish_rate,
            self.timer_callback
        )
    def timer_callback(self):
        msg = self.bridge.cv2_to_imgmsg(self.gray_image, encoding='mono8')
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera'

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ImageGrayPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

