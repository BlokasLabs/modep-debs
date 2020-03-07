#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source ../env.sh

PACKAGE=modep-ctl-scripts
VERSION=1.8.0

pushd src
./build-deb.sh
mv ${PACKAGE}.deb ../${PACKAGE}_${VERSION}.deb
popd
