from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node as ROS2Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        # Include the Gazebo empty world launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                get_package_share_directory('gazebo_ros'), '/launch', '/empty_world.launch.py'
            ])
        ),
        
        # Static transform publisher node
        ROS2Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_footprint_base',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint', '40']
        ),
        
        # Spawn model node
        ROS2Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_model',
            output='screen',
            arguments=['-file', 
                       get_package_share_directory('Ros2_RobotBipede') + '/urdf/Ros2_RobotBipede.urdf', 
                       '-urdf', 
                       '-entity', 
                       'Ros2_RobotBipede']
        ),
        
        # Fake joint calibration node
        ROS2Node(
            package='ros2_topic',
            executable='topic',
            name='fake_joint_calibration',
            arguments=['pub', '/calibrated', 'std_msgs/Bool', 'true']
        ),
    ])

