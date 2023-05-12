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

## Cheatsheet

Eager to start programming? Check the file [here](./LAB_CHEAT_SHEET.md)

# ROS2 and the F1/10

## F1/10 simulator and tools

Download the simulator virtual machine [here](https://drive.google.com/drive/folders/1bKxncDvomwaQjNzUz6HRdBx-EhtF9Ov2?usp=sharing). It is based on [Virtual Box](https://www.virtualbox.org/).

## How to setup the sim machine

### Software-in-the-Loop in the same environment

First, run application (e.g., the remote controller), entering in its Workspace

```
$ cd /home/<YOUR WS>
```

Initialize the **local** environment

```
$ source install/setup.bash
```

Run a specific node from a specific package

```
$ ros2 run <PACKAGE> <NODE>
``` 

Then, to run the simulator (shall be done after), enter its Workspace:

```
$ cd /home/f1tenth_gym_ros
```

Initialize the environment

```
$ source install/setup.bash
```

Run

```
$ ros2 launch f1tenth_gym_ros gym_bridge_launch.py
``` 

[RViz]() will run automatically as UI

### Software-in-the-Loop in a different environment
(e.g., outside of sim)

You justneed to make sure that the two OSses can "speak" to each other, e.g., they are in the same subnet. You can configure the Network settings of your VirtualBox instance to "bridged", and (recommended) you might want to set the IP address of your **guest** machine manually.

### Hardware-in-the-Loop

Same as SiL, but make sure that the **guest** OS is in the same subnet as the external board.

## Useful tools

[Here](https://github.com/f1tenth/f1tenth_gym_ros#keyboard-teleop) you can find a remote controller Node for the F1/10 simulated vehicle.
It comes with ROS2, and you can run it with this
```
$ ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

