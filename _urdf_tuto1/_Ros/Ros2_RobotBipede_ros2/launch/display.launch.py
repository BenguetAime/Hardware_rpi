from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Define the path to the URDF and RVIZ files
    urdf_file = get_package_share_directory('Ros2_RobotBipede') + '/urdf/Ros2_RobotBipede.urdf'
    rviz_file = get_package_share_directory('Ros2_RobotBipede') + '/urdf.rviz'
    
    return LaunchDescription([
        # Declare the 'model' argument
        DeclareLaunchArgument(
            'model',
            default_value=urdf_file,
            description='Absolute path to robot urdf file'
        ),
        
        # Set the robot_description parameter
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': ParameterValue(LaunchConfiguration('model'), value_type=str)}]
        ),
        
        # Launch the joint_state_publisher_gui node
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        
        # Launch the RVIZ node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_file]
        )
    ])

