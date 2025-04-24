# ROS2 

- See graph
`ros2 run rqt_graph rqt_graph`

- Build project
`colcon build --symlink-install`

- Source the workspace
`source install/setup.bash`

- Run the node
`ros2 run <package_name> <node_name>`

- Create a new package
`ros2 pkg create <package_name> --build-type ament_python --dependencies rclpy std_msgs`


- TurtleSim 
`ros2 run turtlesim turtlesim_node`
`ros2 run turtlesim turtle_teleop_key`