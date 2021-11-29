Summary:        Libxslt is a  XSLT C library
Name:           libxslt
Version:        1.1.34
Release:        1%{?dist}
License:        MIT
URL:            http:/http://xmlsoft.org/libxslt/
Group:          System Environment/General Libraries
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://xmlsoft.org/sources/%{name}-%{version}.tar.gz
%define sha1    libxslt=5b42a1166a1688207028e4a5e72090828dd2a61e

Requires:       libxml2-devel
Requires:       libgcrypt

BuildRequires:  libxml2-devel
BuildRequires:  libgcrypt-devel

%description
The libxslt package contains XSLT libraries used for extending libxml2 libraries to support XSLT files.

%package devel
Summary: Development Libraries for libxslt
Group: Development/Libraries
Requires: libxslt = %{version}-%{release}

%description devel
Header files for doing development with libxslt.

%prep
%autosetup -p1
sed -i 's/int xsltMaxDepth = 3000/int xsltMaxDepth = 5000/g' libxslt/transform.c

%build
%configure \
    $(test %{_host} != %{_build} && echo "--with-sysroot=/target-%{_arch}") \
    --disable-static \
    --without-python
make %{?_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name '*.la' -delete
%{_fixperms} %{buildroot}/*

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/*.sh
%{_libdir}/libxslt-plugins
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*
%{_docdir}/*
%{_datadir}/aclocal/*

%changelog
* Mon May 31 2021 Sujay G <gsujay@vmware.com> 1.1.34-1
- Bump version to 1.1.34 to fix build issue with libxml2 upgrade.
- Removed not applicable patches from the version upgrade.
* Tue Dec 17 2019 Shreyas B. <shreyasb@vmware.com> 1.1.29-8
- Apply patch for CVE-2019-5815: READ heap-buffer-overflow in libxslt.
* Wed Oct 30 2019 Siju Maliakkal <smaliakkal@vmware.com> 1.1.29-7
- Patch for CVE-2019-18197
* Sun Jul 21 2019 Shreyas B. <shreyasb@vmware.com> 1.1.29-6
- Apply patch for CVE-2019-13117 and CVE-2019-13118
* Fri Apr 12 2019 Siju Maliakkal <smaliakkal@vmware.com> 1.1.29-5
- Applied patch for CVE-2019-11068
* Tue Jul 11 2017 Divya Thaluru <dthaluru@vmware.com> 1.1.29-4
- Applied patch for CVE-2015-9019
* Fri Jun 02 2017 Xiaolin Li <xiaolinl@vmware.com> 1.1.29-3
- Build does not requires python.
* Thu May 25 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.1.29-2
- Fix CVE-2017-5029.
* Fri Oct 21 2016 Vinay Kulkarni <kulkarniv@vmware.com> 1.1.29-1
- Fix CVEs 2016-1683, 2016-1684, 2015-7995 with version 1.1.29
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.1.28-3
- GA - Bump release of all rpms
* Tue Jan 19 2016 Xiaolin Li <xiaolinl@vmware.com> 1.1.28-2
- Add a dev subpackage.
* Mon Oct 13 2014 Divya Thaluru <dthaluru@vmware.com> 1.1.28-1
- Initial build.  First version
