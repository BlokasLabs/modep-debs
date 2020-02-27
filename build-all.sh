#!/bin/bash

for i in $(ls); do
	if [ -d $i ]; then
		echo Building $i...
		pushd $i
		./build-deb.sh
		popd
	fi
done
