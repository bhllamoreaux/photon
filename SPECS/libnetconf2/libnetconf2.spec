%global debug_package %{nil}
Summary:        NETCONF library in C intended for building NETCONF clients and servers.
Name:           libnetconf2
Version:        2.1.7
Release:        1%{?dist}
License:        BSD-3-Clause
Group:          Development/Tools
URL:            https://github.com/CESNET/libnetconf2
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://github.com/CESNET/libnetconf2/archive/refs/tags/%{name}-%{version}.tar.gz
%define sha1 %{name}=bac66d22bc7928f5fbd77850775f79f73e4b18b8

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libssh-devel
BuildRequires:  openssl-devel
BuildRequires:  libyang-devel
BuildRequires:  pcre2-devel

%package devel
Summary: Development libraries for libnetconf2

%description devel
Headers of libnetconf library.

%description
libnetconf2 is a NETCONF library in C intended for building NETCONF clients and
servers. NETCONF is the NETwork CONFiguration protocol introduced by IETF.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libnetconf2.so.*
%exclude %{_libdir}/debug
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files devel
%{_libdir}/libnetconf2.so
%{_libdir}/pkgconfig/libnetconf2.pc
%{_includedir}/*.h
%{_includedir}/libnetconf2/*.h
%dir %{_includedir}/libnetconf2/

%changelog
*   Thu Mar 24 2022 Brennan Lamoreaux <blamoreaux@vmware.com> 2.1.7-1
-   Initial addition