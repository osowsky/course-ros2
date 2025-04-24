#!/usr/bin/bash
#

# Display help?
if [ "${1}" == "" ]; then
	echo "Usage: ${0} all"
	echo ""
	echo "Remove built directories (build/, install/, and log/)."
	echo ""
	echo "Options:"
	echo ""
	echo " all	remove build/, install/, and log/ folders."
	echo ""
	exit -1
fi

# Build all packages?
RARGS="build/ install/ log/"
if [ "${1}" == "all" ]; then
	echo "Removing folders ${RARGS}..."
	BARGS=""
else
	echo "ERROR: all argument must be typed."
	exit -1
fi

# Remove built directories.
rm -Rf ${RARGS}
echo "...done!"
exit 0

