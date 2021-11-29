Summary:        An URL retrieval utility and library
Name:           curl
Version:        7.78.0
Release:        2%{?dist}
License:        MIT
URL:            http://curl.haxx.se
Group:          System Environment/NetworkingLibraries
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://curl.haxx.se/download/%{name}-%{version}.tar.gz
%define sha1    curl=c51b85373ae7b3186ad364e909f29b93043a9c16

Patch0:         curl-CVE-2021-22945.patch
Patch1:         curl-CVE-2021-22946.patch
Patch2:         curl-CVE-2021-22947.patch

Requires:       ca-certificates
Requires:       openssl
Requires:       libssh2

BuildRequires:  ca-certificates
BuildRequires:  openssl-devel
BuildRequires:  libssh2-devel

%description
The cURL package contains an utility and a library used for
transferring files with URL syntax to any of the following
protocols: FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET,
DICT, LDAP, LDAPS and FILE. Its ability to both download and
upload files can be incorporated into other programs to support
functions like streaming media.

%prep
%autosetup -p1
sed -i '/--static-libs)/{N;s#echo .*#echo #;}' curl-config.in

%build
%configure \
    CFLAGS="%{optflags}" \
    CXXFLAGS="%{optflags}" \
    --disable-static \
    --enable-threaded-resolver \
    --with-ssl \
    --with-libssh2 \
    --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt
make %{?_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -v -d -m755 %{buildroot}/%{_docdir}/%{name}-%{version}
find %{buildroot}/%{_libdir} -name '*.la' -delete
%{_fixperms} %{buildroot}/*

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%{_datarootdir}/aclocal/libcurl.m4
%{_docdir}/%{name}-%{version}

%changelog
* Tue Sep 14 2021 Dweep Advani <dadvani@vmware.com> 7.78.0-2
- Fixed CVE-2021-22945, CVE-2021-22946, CVE-2021-22947
* Thu Aug 12 2021 Harinadh D <hdommaraju@vmware.com> 7.78.0-1
- Version update
* Thu Jul 22 2021 Harinadh D <hdommaraju@vmware.com> 7.75.0-4
- Fix CVE-2021-22924,CVE-2021-22925
* Fri Jul 2 2021 Nitesh Kumar <kunitesh@vmware.com> 7.75.0-3
- Fix CVE-2021-22897
* Fri May 21 2021 Harinadh D <hdommaraju@vmware.com> 7.75.0-2
- Fix CVE-2021-22898,CVE-2021-22901
* Mon Mar 29 2021 Harinadh D <hdommaraju@vmware.com> 7.75.0-1
- Fix CVE-2021-22876,CVE-2021-22890
* Mon Dec 07 2020 Dweep Advani <dadvani@vmware.com> 7.59.0-12
- Patched for  CVE-2020-8284, CVE-2020-8285 and CVE-2020-8286
* Wed Aug 19 2020 Harinadh D <hdommaraju@vmware.com> 7.59.0-11
- Fix for CVE-2020-8231
* Wed Jun 17 2020 Ankit Jain <ankitja@vmware.com> 7.59.0-10
- Fix for CVE-2020-8177
* Thu Oct 03 2019 Dweep Advani <dadvani@vmware.com> 7.59.0-9
- Patch for CVE-2019-5481 and CVE-2019-5482
* Wed May 29 2019 Siju Maliakkal <smaliakkal@vmware.com> 7.59.0-8
- Patch for CVE-2019-5436
* Thu Mar 14 2019 Anish Swaminathan <anishs@vmware.com> 7.59.0-7
- Patch for CVE-2018-16890
* Thu Feb 14 2019 Dweep Advani <dadvani@vmware.com> 7.59.0-6
- Fixed CVE-2019-3822 and CVE-2019-3823
* Wed Jan 30 2019 Dweep Advani <dadvani@vmware.com> 7.59.0-5
- Fixed CVE-2018-14618 and CVE-2018-16839
* Thu Jan 03 2019 Siju Maliakkal <smaliakkal@vmware.com> 7.59.0-4
- Apply patches for CVE-2018-16840, CVE-2018-16842
* Tue Sep 18 2018 Keerthana K <keerthanak@vmware.com> 7.59.0-3
- Fix for CVE-2018-0500
* Thu Jul 05 2018 Keerthana K <keerthanak@vmware.com> 7.59.0-2
- Fix for CVE-2018-1000300, CVE-2018-1000301.
* Wed Apr 04 2018 Dheeraj Shetty <dheerajs@vmware.com> 7.59.0-1
- Update to version 7.59.0
* Mon Feb 12 2018 Xiaolin Li <xiaolinl@vmware.com> 7.58.0-1
- Update to version 7.58.0
* Thu Dec 21 2017 Xiaolin Li <xiaolinl@vmware.com> 7.56.1-2
- Fix CVE-2017-8818.
* Wed Dec 13 2017 Xiaolin Li <xiaolinl@vmware.com> 7.56.1-1
- Update to version 7.56.1
* Mon Nov 27 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.0-5
- Fix CVE-2017-1000257
* Mon Nov 06 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.0-4
- Fix CVE-2017-1000254
* Thu Nov 02 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.0-3
- Fix CVE-2017-1000100
* Wed Oct 25 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.0-2
- Fix CVE-2017-1000101
* Wed May 24 2017 Divya Thaluru <dthaluru@vmware.com> 7.54.0-1
- Update to 7.54.0
* Wed Nov 30 2016 Xiaolin Li <xiaolinl@vmware.com> 7.51.0-2
- Enable sftp support.
* Wed Nov 02 2016 Anish Swaminathan <anishs@vmware.com> 7.51.0-1
- Upgrade curl to 7.51.0
* Thu Oct 27 2016 Anish Swaminathan <anishs@vmware.com> 7.47.1-4
- Patch for CVE-2016-5421
* Mon Sep 19 2016 Xiaolin Li <xiaolinl@vmware.com> 7.47.1-3
- Applied CVE-2016-7167.patch.
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 7.47.1-2
- GA - Bump release of all rpms
* Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 7.47.1-1
- Updated to version 7.47.1
* Thu Jan 14 2016 Xiaolin Li <xiaolinl@vmware.com> 7.46.0-1
- Updated to version 7.46.0
* Thu Aug 13 2015 Divya Thaluru <dthaluru@vmware.com> 7.43.0-1
- Update to version 7.43.0.
* Mon Apr 6 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 7.41.0-1
- Update to version 7.41.0.
