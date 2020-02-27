#!/bin/bash

for i in $(find . | grep debian/rules); do
	pushd $(dirname "$i")/..
	debian/rules clean
	popd
done
