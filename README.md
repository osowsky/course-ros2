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

## Nice ROS2 commands (introspect topics with CLI)

> ros2 topic list
>
> ros2 topic info \<topic-name>
>
> ros2 topic echo \<topic-name>
>
> ros2 interface show \<topic-type>
>
> ros2 topic hz \<topic-name> *hz means hertz*
>
> ros2 topic bw \<topic-name> *bw means bandwidth*
>
> ros2 topic pub -r \<hz-value> \<topic-name> \<topic-type> "{name: value}" *pub means publish*
>
> ros2 node list
>
> ros2 node info \<node-name>
>
> ros2 run \<pkg-name> \<exec-name> --ros-args -r __node:=\<new-node-name> -r \<topic-name>:=\<new-topic-name> *-r means --remap*

## Playing with Turtlesim example

> ros2 run turtlesim turtlesim_node *start turtlesim node*
>
> ros2 run turtlesim turtle_teleop_key *start turtlesim keyboard interface*

## Replay topics with bags files

> ros2 bag record [-o \<dir-name>] [-a | \<topic-name-01> \<topic-name-02> \<topic-name-nn>]
>
> ros2 bag info \<dir-name>
>
> ros2 bag play \<dir-name>

## Nice ROS2 commands (introspect services with CLI)

>
> ros2 service list
>
> ros2 service call \<service-name> \<service-type> "{name: value}"
>
> ros2 service type \<service-name>
>
> ros2 interface show \<service-type>
