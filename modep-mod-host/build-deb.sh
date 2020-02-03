#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source ../env.sh

pushd src
make -j4
make DESTDIR=$DEB_ROOT PREFIX=/usr install
popd

fakeroot dpkg --build debroot modep-mod-host.deb

