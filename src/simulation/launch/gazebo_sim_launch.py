"""Simulate a Tello drone"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    world_path = os.path.join(get_package_share_directory('simulation'), 'worlds', 'simple.world')
    robot_sdf_path = os.path.join(get_package_share_directory('simulation'), 'models','mobrob', 'model.sdf')
    urdf_path = os.path.join(get_package_share_directory('simulation'), 'urdf', 'mobrob.urdf')

    return LaunchDescription([
        # Launch Gazebo, loading tello.world
        ExecuteProcess(cmd=[
            'gazebo',
            '--verbose',
            '-s', 'libgazebo_ros_init.so',  # Publish /clock
            '-s', 'libgazebo_ros_factory.so',  # Provide gazebo_ros::Node
            world_path
        ], output='screen'),

        
        # Spawn robot
        Node(package='simulation', executable='insert_mobrob.py', output='screen',
             arguments=[robot_sdf_path, '0', '0', '0', '1.5707']),

        # Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen',
        #     arguments=[urdf_path]),
        

    ])
