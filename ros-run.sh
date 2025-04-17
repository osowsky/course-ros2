#!/usr/bin/bash
#

# Display help?
if [ "${1}" == "" ]; then
	echo "Usage: ${0} <pkg-name> <exec-name> [args]"
	echo ""
	echo "Run a specific executable from a package."
	echo ""
	echo "Options:"
	echo ""
	echo " <pkg-name>	the name of the ROS2 package."
	echo " <exec-name>	the name of the ROS2 executable."
	echo " args       	arbitrary arguments to the ROS2 executable."
	echo ""
	exit -1
fi

# Test exec-name argument.
if [ "${2}" == "" ]; then
	echo "ERROR: exec-name argument must not be blank."
	exit -1
fi

# Build package.
echo "Building package ${1}..."
colcon build --packages-select ${1}
echo "...done!"

# Reload package environment.
echo "Reloading devel environment..."
source install/setup.bash
echo "...done!"

# Run exec file.
echo "Running executable ${2}..."
ros2 run ${@}
echo "${@}"
echo "...done!"
echo ""

exit 0
