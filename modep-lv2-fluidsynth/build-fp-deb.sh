#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source ../env.sh

PACKAGE=modep-lv2-fluidplug
VERSION=1.0.0

PKGFOLDER=${PACKAGE}-${VERSION}

mkdir -p ${PKGFOLDER}
cp -r src_fp/* ${PKGFOLDER}
tar -czf ${PKGFOLDER}.tar.gz --exclude .git ${PKGFOLDER}

cd ${PKGFOLDER}

echo y | debuild -b -us -uc
