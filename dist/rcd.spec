Summary: NetBSD rc.d system
Name: rcd

Version: 20140525
Release: 1%{dist}
License: BSD

Group: System Environment/Base
URL: http://www.dracolinux.org

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
mkdir -p %{buildroot}/sbin %{buildroot}/etc/rc.d %{buildroot}/usr/man/man8
cp pkgtools/rcorder/work/rcorder-20120310/rcorder %{buildroot}/sbin/
cat pkgtools/rcorder/work/rcorder-20120310/rcorder.8 > %{buildroot}/usr/man/man8/rcoder.8
cat pkgtools/rc.subr/work/rc.subr-20090118/rc.conf.example > %{buildroot}/etc/rc.conf
cat pkgtools/rc.subr/work/rc.subr-20090118/rc.subr | sed 's#/usr/bin/su#/bin/su#g' > %{buildroot}/etc/rc.subr
cp pkgtools/rc.subr/work/rc.subr-20090118/rc.d/{DAEMON,LOGIN,NETWORKING,SERVERS} %{buildroot}/etc/rc.d/
chmod +x %{buildroot}/etc/rc.subr

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/rc.conf
/etc/rc.d/DAEMON
/etc/rc.d/LOGIN
/etc/rc.d/NETWORKING
/etc/rc.d/SERVERS
/etc/rc.subr
/sbin/rcorder
/usr/man/man8/*

%changelog
* Thu Apr 29 2014 Ole Andre Rodlie <olear@dracolinux.org> - 0.1-1
- initial version
