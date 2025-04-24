# Course: ROS2 for Beginners (ROS Jazzy - 2025)

After installing ROS2 on Linux, add the following lines to the end of the `~/.bashrc` profile file.

> `source /opt/ros/jazzy/setup.bash`
>
> `source ~/Documents/ros2_ws/install/setup.bash`

Scripts in `~/Documents/ros2_ws/`

> ./ros-build.sh
>
> Usage: ./ros-build.sh \<pkg-name>|all
>
> Build a specific package or all packages.

> ./ros-clean.sh
>
> Usage: ./ros-clean.sh all
>
> Remove aux. directories (build/, install/, and log/).

> ./ros-run.sh
>
> Usage: ./ros-run.sh \<pkg-name> \<exec-name> [args]
>
> Run a specific executable from a package.

Scripts in `~/Documents/ros2_ws/src/`

> ./ros-pkg-create.sh
>
> Usage: ./ros-pkg-create.sh <pkg-name> <build-type>
> 
> Create the package environment for a new ROS2 package.
