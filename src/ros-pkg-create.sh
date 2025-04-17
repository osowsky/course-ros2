#!/usr/bin/bash
#

# Display help?
if [ "${1}" == "" ]; then
	echo "Usage: ${0} <pkg-name> <build-type>"
	echo ""
	echo "Create the package environment for a new ROS2 package."
	echo ""
	echo "Options:"
	echo ""
	echo " <pkg-name>	the name of the new ROS2 package."
	echo " <build-type>	which programming language will be used in this package?"
	echo "             	you could choose either 'cpp' or 'python'"
	echo ""
	exit -1
fi

# Test build-type argument.
if [ "${2}" == "" ]; then
	echo "ERROR: build-type argument must be either 'cpp' or 'python', not blank."
	exit -1
fi

# Create package environmeent.
echo "Creating ${1} package in ${2}..."
if [ "${2}" == "python" ]; then
	ros2 pkg create ${1} --build-type ament_python --dependencies rclpy
	echo "...done!"
elif [ "${2}" == "cpp" ]; then
	ros2 pkg create ${1} --build-type ament_cmake --dependencies rclcpp
	echo "...done!"
else
	echo "...ERROR: invalid build-type ${2}."
fi
echo ""

exit 0

