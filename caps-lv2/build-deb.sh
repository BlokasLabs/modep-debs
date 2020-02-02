#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pushd $DIR

source ../env.sh

mkdir -p deb/usr/modep/lv2
popd
