# ME439MobileRobotSimulation
# The repository is a simulation of an LQR controller for a differential mobile robot on Gazebo and ROS2 #

### Prerequisites ####
The trajectory based LQR controller is available in the following repository: https://github.com/mohsafwat23/ME439MobileRobotEKF

#### Install Ros2 foxy ####
For Ubuntu 20.04: https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

#### Build ####
`colcon build`

### Install Gazebo ###
`sudo apt install gazebo11 libgazebo11 libgazebo11-dev`

`sudo apt install ros-foxy-gazebo-ros-pkgs ros-foxy-cv-bridge`

#### Source Enviroment and Gazebo ####
`source install/setup.bash`

`export GAZEBO_MODEL_PATH=${PWD}/install/simulation/share/simulation/models`

`source /usr/share/gazebo/setup.sh`

#### Velocity publisher example command line ####
`ros2 topic pub /mobrob/cmd_vel geometry_msgs/Twist "{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"`

#### ROS1 Bridge ####
Tutorial: https://www.theconstructsim.com/ros2-qa-217-how-to-mix-ros1-and-ros2-packages/

`ros2 run ros1_bridge dynamic_bridge --bridge-all-topics`

#### Running the simulation ####
Option 1 (1 waypoint):

`ros2 launch simulation gazebo_sim_launch.py`

and run `ros2 run simulation lqr.py`

Option 2 (trajectory): 

`ros2 launch simulation gazebo_sim_launch.py`

and from the other Repo run `roslaunch mobrob gazebo_sim.launch`


#### Kill gazebo server if it crashes ####
`killall -9 gzserver`
