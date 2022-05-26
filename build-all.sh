#!/bin/bash

set -e

for i in $(ls); do
	if [ -d $i ]; then
		pushd $i
		if [ ! -e SKIP ]; then
			echo Building $i...
			./build-deb.sh
			touch SKIP
		else
			echo Skipping building $i due to SKIP file.
		fi
		popd
	fi
done
