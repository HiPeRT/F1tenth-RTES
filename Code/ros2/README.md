# Installation and basic examples
To correctly configure your ROS2 environment, you can follow the tutorial [here](https://docs.ros.org/en/foxy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)

## Examples

Course examples
- Pub/sub in C++ [here](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)
- Pub/sub in Python [here](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
- Also in the `Code/ros2/src` folder

Fetch more official examples
```
$ git clone https://github.com/ros2/examples src/examples -b foxy
```

# ROS2 and the F1/10

## F1/10 simulator and tools

Download the simulator vrtual machine [here](https://drive.google.com/drive/folders/1bKxncDvomwaQjNzUz6HRdBx-EhtF9Ov2?usp=sharing). It is based on Virtual Box.

## How to setup the sim machine
- <i>Coming soon...</i>

## useful tools

[Here](https://github.com/f1tenth/f1tenth_gym_ros#keyboard-teleop) you can find a remote controller Node for the F1/10 simulated vehicle.
It comes with ROS2, and you can run it with this
```
$ ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

