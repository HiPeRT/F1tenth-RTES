# Cheat sheet for the lab exercises in ROS2


First, open a terminal, and source the ROS2 environment/default underlay.
```
$ source /opt/ros/foxy/setup.bash
```

This will create the necessary environmental vars and stuff for using ROS2 toolchain **only in this terminal**.

Enter the root folder of your workspace (in my examples, ```<REPO-ROOT>/Code/ros2```), and check , just to be sure, that the folìder ```src``` is there.
```
$ ls
README.md <other files> src/
```

Then you can install deps for this workspace (fetch by ```package.xml``` manifest files).
```
$ rosdep install -i --from-path src --rosdistro foxy -y
```

Now, it's time to build all the packages in your workspace.
```
$ colcon build [--symlink-install]
# This latter flag for Python packages
```
For Python packages, it is **very important** to run also the ```--symlink-install``` flag, to resolve/fix symbolic links.

If build succeeds, you should see three more folders: ```install```, ```log```, and ```build```, aside with ```src```.
```
$ ls
README.md <other files> build/ install/ log/ src/
```

Now, your local overlay is ready! Among other files, you have now to very important scripts, inside your.```install``` folder:

1. a local setup script, which configures your overlay against the default underlay (i.e., ROS2 environment);
```
$ source install/setup.bash
```

2. a **global** setup script, similar to the one in ```/opt/ros/foxy/setup.bash```, but including also local overlay's configuration;
```
$ source install/local_setup.bash
```
It is recommended that you run the latter one, to set up the ROS environment, when you open a new Terminal.

...now you can run your node, opening a new terminal for each of them. Again, **don't forget to source your ```install/setup.bash``` every time!**
```
$ ros2 run <package name> <node name>
```
(note that, if the workspace and overlay are set up correctly, you shall be able to use ```TAB``` co autocomplete your ```<package name>``` and ```<node name>```)