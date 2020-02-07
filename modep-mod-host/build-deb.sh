#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source ../env.sh

PACKAGE=modep-mod-host
VERSION=2020.02.05

PKGFOLDER=${PACKAGE}-${VERSION}

mkdir -p ${PKGFOLDER}
cp -r src/* ${PKGFOLDER}
tar -czf ${PKGFOLDER}.tar.gz --exclude .git ${PKGFOLDER}

cd ${PKGFOLDER}

echo y | debuild -b -us -uc
