Summary:           A toolkit for defining and handling authorizations.
Name:              polkit
Version:           0.120
Release:           1%{?dist}
Group:             Applications/System
Vendor:            VMware, Inc.
License:           LGPLv2+
URL:               https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html
Distribution:      Photon

Source0:           https://www.freedesktop.org/software/polkit/releases/%{name}-%{version}.tar.gz
%define sha1       %{name}=75d5885251eef36b28851e095120bc1f60714160

BuildRequires:     autoconf
BuildRequires:     expat-devel
BuildRequires:     glib-devel
BuildRequires:     gobject-introspection
BuildRequires:     intltool >= 0.40.0
# polkit needs mozjs-78.X
BuildRequires:     mozjs-devel >= 78.3.1
BuildRequires:     Linux-PAM-devel
BuildRequires:     systemd-devel

Requires:          mozjs
Requires:          expat
Requires:          glib
Requires:          Linux-PAM
Requires:          systemd
Requires(pre):     /usr/sbin/useradd /usr/sbin/groupadd
Requires(postun):  /usr/sbin/userdel /usr/sbin/groupdel

%description
polkit provides an authorization API intended to be used by privileged programs
(“MECHANISMS”) offering service to unprivileged programs (“SUBJECTS”) often
through some form of inter-process communication mechanism

%package           devel
Summary:           polkit development headers and libraries
Group:             Development/Libraries
Requires:          polkit = %{version}-%{release}

%description       devel
header files and libraries for polkit

%prep
%autosetup -p1

%build
%configure --enable-libsystemd-login=yes \
        --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name '*.la' -delete
install -vdm 755 %{buildroot}/etc/pam.d
cat > %{buildroot}/etc/pam.d/polkit-1 << "EOF"
# Begin /etc/pam.d/polkit-1

auth     include        system-auth
account  include        system-account
password include        system-password
session  include        system-session

# End /etc/pam.d/polkit-1
EOF

%check
# Disable check. It requires dbus - not available in chroot/container.

%pre
getent group polkitd > /dev/null || groupadd -fg 27 polkitd &&
getent passwd polkitd > /dev/null || \
    useradd -c "PolicyKit Daemon Owner" -d /etc/polkit-1 -u 27 \
        -g polkitd -s /bin/false polkitd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    systemctl stop polkit
    if getent passwd polkitd >/dev/null; then
        userdel polkitd
    fi
    if getent group polkitd >/dev/null; then
        groupdel polkitd
    fi
fi

%files
%defattr(-,root,root)
%{_bindir}/pk*
%{_libdir}/lib%{name}-*.so.*
%{_libdir}/polkit-1/polkit-agent-helper-1
%{_libdir}/polkit-1/polkitd
%{_unitdir}/polkit.service
%{_datadir}/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%{_datadir}/locale/*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%{_sysconfdir}/pam.d/polkit-1
%{_sysconfdir}/polkit-1/rules.d/50-default.rules
%{_datadir}/gettext/its

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}-1/
%{_libdir}/lib%{name}-*.a
%{_libdir}/lib%{name}-*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Oct 19 2021 Shreenidhi Shedi <sshedi@vmware.com> 0.120-1
- Bump version as a part of mozjs upgrade
* Wed Apr 28 2021 Gerrit Photon <photon-checkins@vmware.com> 0.118-2
- Bump up release version since mozjs is update to 78.10.0
* Wed Sep 09 2020 Gerrit Photon <photon-checkins@vmware.com> 0.118-1
- Automatic Version Bump
* Tue Aug 25 2020 Ankit Jain <ankitja@vmware.com> 0.117-2
- This version of polkit build requires specific mozjs version
* Thu Aug 13 2020 Ankit Jain <ankitja@vmware.com> 0.117-1
- Upgraded to 0.117
* Sat Oct 26 2019 Ankit Jain <ankitja@vmware.com> 0.116-1
- Upgraded to 0.116
* Thu Jan 10 2019 Dweep Advani <dadvani@vmware.com> 0.113-4
- Fix for CVE-2018-19788
* Thu Dec 07 2017 Alexey Makhalov <amakhalov@vmware.com> 0.113-3
- Added pre and postun requires for shadow tools
* Thu Oct 05 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.113-2
- Enable PAM and systemd.
* Wed Oct 04 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.113-1
- Upgrade to 0.113-1
* Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.112-1
- initial version
