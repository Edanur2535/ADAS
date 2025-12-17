from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='adas_perception',
            executable='camera',
            name='camera_node',
            parameters=['config/params.yaml']
        ),

        Node(
            package='adas_perception',
            executable='mock_node',
            name='mock_control_publisher',
            parameters=['config/params.yaml']
        )
    ])
