Summary: NetBSD rc.d system
Name: rcd

Version: 20140525.2
Release: 3%{dist}
License: BSD

Group: System Environment/Base
URL: http://github.com/olear/rcd

Packager: Ole Andre Rodlie, <olear@dracolinux.org>
Vendor: DracoLinux, http://dracolinux.org

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bmake

%description
NetBSD rc.d system

%prep
%setup

%build
cd pkgtools/rcorder
bmake NO_CHECKSUM=yes PKG_DEVELOPER=no

cd ../rc.subr
bmake NO_CHECKSUM=yes PKG_DEVELOPER=no

%install
mkdir -p %{buildroot}/sbin %{buildroot}/etc/init.d %{buildroot}/etc/rc.d %{buildroot}/usr/share/man/man{5,8}
cp pkgtools/rcorder/work/rcorder-20120310/rcorder %{buildroot}/sbin/
cat pkgtools/rcorder/work/rcorder-20120310/rcorder.8 > %{buildroot}/usr/share/man/man8/rcorder.8
cat etc/rc.conf > %{buildroot}/etc/rc.conf
cat pkgtools/rc.subr/work/rc.subr-20090118/rc.subr | sed 's#/usr/bin/su#/bin/su#g' > %{buildroot}/etc/rc.subr
cp pkgtools/rc.subr/work/rc.subr-20090118/rc.d/{DAEMON,LOGIN,NETWORKING} %{buildroot}/etc/rc.d/
cat pkgtools/rc.subr/work/rc.subr-20090118/rc.d/SERVERS | sed 's/# REQUIRE: mountcritremote//' > %{buildroot}/etc/rc.d/SERVERS
cp man/*.5 %{buildroot}/usr/share/man/man5/
cat etc/rc.redhat > %{buildroot}/etc/init.d/rcd
chmod +x %{buildroot}/etc/init.d/rcd
chmod +x %{buildroot}/etc/rc.d/SERVERS

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/init.d/rcd
/etc/rc.conf
/etc/rc.d/DAEMON
/etc/rc.d/LOGIN
/etc/rc.d/NETWORKING
/etc/rc.d/SERVERS
/etc/rc.subr
/sbin/rcorder
/usr/share/man/man8/*
/usr/share/man/man5/*

%changelog
* Thu Apr 29 2014 Ole Andre Rodlie <olear@dracolinux.org> - 0.1-1
- initial version
