#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source ../env.sh

PACKAGE=modep-btn-scripts
VERSION=1.2.0-2

pushd src
./make_deb.sh
mv modep-btn-scripts.deb ../${PACKAGE}_${VERSION}.deb
popd
