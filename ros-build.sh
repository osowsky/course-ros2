#!/usr/bin/bash
#

# Display help?
if [ "${1}" == "" ]; then
	echo "Usage: ${0} <pkg-name>|all"
	echo ""
	echo "Build a specific package or all packages."
	echo ""
	echo "Options:"
	echo ""
	echo " <pkg-name>	the name of the ROS2 package."
	echo " all      	all packages will be built."
	echo ""
	exit -1
fi

# Build all packages?
BARGS="--packages-select ${1}"
if [ "${1}" == "all" ]; then
	echo "Building all packages..."
	BARGS=""
else
	echo "Building ${1} package..."
fi

# Build either a specific package or all them.
colcon build --executor sequential ${BARGS}
echo "...done!"
exit 0

