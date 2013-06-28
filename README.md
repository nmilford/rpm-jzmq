rpm-jzmq
========

An RPM spec file for ØMQ's Java bindings. This RPM is built to be compatible with Storm.

To Build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`sudo yum -y install libtool automake autoconf zeromq-devel`

`wget https://raw.github.com/nmilford/rpm-jzmq/master/jzmq.spec -O ~/rpmbuild/SPECS/jzmq.spec`

`wget https://codeload.github.com/nathanmarz/jzmq/zip/master -O ~/rpmbuild/SOURCES/jzmq-2.1.0.zip`

`rpmbuild -bb ~/rpmbuild/SPECS/jzmq.spec`