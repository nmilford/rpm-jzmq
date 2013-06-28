# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install libtool automake autoconf
# wget https://raw.github.com/nmilford/rpm-jzmq/master/jzmq.spec -O ~/rpmbuild/SPECS/jzmq.spec
# wget https://codeload.github.com/nathanmarz/jzmq/zip/master -O ~/rpmbuild/SOURCES/jzmq-2.1.0.zip
# rpmbuild -bb ~/rpmbuild/SPECS/jzmq-2.1.0.spec

Name:          jzmq
Version:       2.1.0
Release:       storm1%{?dist}
Summary:       The Java ZeroMQ bindings
Group:         Applications/Internet
License:       LGPLv3+
URL:           http://www.zeromq.org/
Source:        %{name}-%{version}.zip
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, libstdc++-devel, libtool, zeromq-devel, jdk
Requires:      libstdc++, zeromq

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the Java Bindings for ZeroMQ.

%package devel
Summary:  Development files and static library for the Java Bindings for the ZeroMQ library.
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig, zeromq

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains Java Bindings for ZeroMQ related development libraries and header files.

%prep
%setup -n jzmq-master

%build
export JAVA_HOME=/usr/java/default/
./autogen.sh
%configure

%{__make}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Install the package to build area
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)

# docs in the main package
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README

# libraries
%{_libdir}/libjzmq.so*
/usr/share/java/zmq.jar

%files devel
%defattr(-,root,root,-)
%{_libdir}/libjzmq.la
%{_libdir}/libjzmq.a

%changelog
* Mon Jun 11 2012 Nathan Milford <nathan@milford.io>
- Tweaked to work with Nathan Marz's github fork for use with Storm.
* Thu Dec 09 2010 Alois Belaska <alois.belaska@gmail.com>
- version of package changed to 2.1.0
* Tue Sep 21 2010 Stefan Majer <stefan.majer@gmail.com>
- Initial packaging
