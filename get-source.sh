#!/bin/sh
p=nacl-sdk
svn=http://nativeclient-sdk.googlecode.com/svn/trunk/src

test -s depot_tools.tar.gz || wget -c http://src.chromium.org/svn/trunk/tools/depot_tools.tar.gz
test -d depot_tools || tar xzf depot_tools.tar.gz

install -d $p
cd $p

test -f .gclient || ../depot_tools/gclient config $svn
../depot_tools/gclient sync
cd ..

tar -cjf $p-$(date +%Y%m%d).tar.bz2 --exclude-vcs $p
