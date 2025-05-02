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
	echo "    --remap|-r __node:=<new-node-name>"
	echo "    --remap|-r <topic-name>:=<new-topic-name>"
	echo "    --remap|-r <service-name>:=<new-service-name>"
	echo ""
	exit -1
fi

# Test exec-name argument.
if [ "${2}" == "" ]; then
	echo "ERROR: exec-name argument must not be blank."
	exit -1
fi

# Run exec file (with arguments).
if [ "${#}" -eq 2 ]; then
	echo "Running executable ${2}..."
	ros2 run ${@}
else
	pname=${1}
	ename=${2}
	shift 2
	echo "Running executable ${ename} with args ${@}..."
	ros2 run ${pname} ${ename} --ros-args ${@}
fi
echo "...done!"
echo ""

exit 0
