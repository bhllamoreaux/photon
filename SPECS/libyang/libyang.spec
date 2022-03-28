Name: libyang
Version: 2.0.164
Release: 1%{?dist}
Summary: YANG data modeling language library
Url: https://github.com/CESNET/libyang
License: BSD
Group:  Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/CESNET/libyang/archive/refs/tags/v%{version}.tar.gz
%define sha1 %{name}=2df5e4fa47c53b9d9d0477314664641f57e0025c

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pcre2-devel

%description
Libyang is YANG data modeling language parser and toolkit
written (and providing API) in C.

%package devel
Summary:    Development files for libyang

%description devel
Files needed to develop with libyang.

%package tools
Summary:        YANG validator tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      %{name} < 1.0.225-3

%description tools
YANG validator tools.

%prep
%autosetup -p1
mkdir build

%build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DCMAKE_BUILD_TYPE:String="Release" \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libyang.so.2
%{_libdir}/libyang.so.2.*
%exclude %{_libdir}/debug
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files tools
%{_bindir}/yanglint
%{_bindir}/yangre
%{_datadir}/man/man1/yanglint.1.gz
%{_datadir}/man/man1/yangre.1.gz

%files devel
%defattr(-, root, root)
%{_libdir}/*.so.*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libyang.pc
%{_includedir}/libyang/*.h

%changelog
* Fri Mar 25 2022 Brennan Lamoreaux <blamoreaux@vmware.com> 2.0.164-1
- Initial addition