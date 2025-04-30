#!/usr/bin/bash
#

# Display help?
if [ "${1}" == "" ]; then
	echo "Usage: ${0} <pkg-name>|all [args]"
	echo ""
	echo "Build a specific package or all packages."
	echo ""
	echo "Options:"
	echo ""
	echo " <pkg-name>	the name of the ROS2 package."
	echo " all      	all packages will be built."
	echo " args       	arbitrary arguments to the ROS2 executable."
	echo "    --symlink-install"

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
if [ "${#}" -ge 2 ]; then
	shift 1
	BARGS+=" ${@}"
fi
colcon build --executor sequential ${BARGS}
echo "...done!"

# Reload package environment.
echo "Reloading devel environment..."
source ./install/setup.bash
echo "...done!"
exit 0
