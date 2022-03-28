<<<<<<< HEAD
%global debug_package %{nil}
=======
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887
Summary:        NETCONF library in C intended for building NETCONF clients and servers.
Name:           libnetconf2
Version:        2.1.7
Release:        1%{?dist}
License:        BSD-3-Clause
Group:          Development/Tools
URL:            https://github.com/CESNET/libnetconf2
Vendor:         VMware, Inc.
Distribution:   Photon

<<<<<<< HEAD
Source0:        https://github.com/CESNET/libnetconf2/archive/refs/tags/%{name}-2.1.7.tar.gz
=======
Source0:        https://github.com/CESNET/libnetconf2/archive/refs/tags/v2.1.7.tar.gz
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887
%define sha1 %{name}=bac66d22bc7928f5fbd77850775f79f73e4b18b8

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
<<<<<<< HEAD
BuildRequires:  libtool
BuildRequires:  libssh-devel
BuildRequires:  openssl-devel
BuildRequires:  libyang-devel
BuildRequires:  pcre2-devel

%package devel
Summary:    Headers of libnetconf2 library
=======
BuildRequires:  libssh2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libyang) >= 2

%package devel
Summary:    Headers of libnetconf2 library
Conflicts:  libnetconf-devel
Requires:   %{name}%{?_isa} = %{version}-%{release}
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887

%description devel
Headers of libnetconf library.

%description
libnetconf2 is a NETCONF library in C intended for building NETCONF clients and
servers. NETCONF is the NETwork CONFiguration protocol introduced by IETF.

<<<<<<< HEAD
%pre
echo 'new install'

=======
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887
%prep
%autosetup -p1
mkdir build

<<<<<<< HEAD
=======
%configure
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887
%build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DCMAKE_BUILD_TYPE:String="Release" \
<<<<<<< HEAD
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    ..
make %{?_smp_mflags}

%install
echo "hello!"
cd build
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
=======
    -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
    -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
    ..
make

%install
cd build
make DESTDIR=%{buildroot} %{?_smp_mflags} install
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887

%files
%license LICENSE
%{_libdir}/libnetconf2.so.*
<<<<<<< HEAD
%exclude %{_libdir}/debug
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
=======
>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887

%files devel
%{_libdir}/libnetconf2.so
%{_libdir}/pkgconfig/libnetconf2.pc
%{_includedir}/*.h
%{_includedir}/libnetconf2/*.h
%dir %{_includedir}/libnetconf2/

<<<<<<< HEAD
=======
%find_lang %{name}

>>>>>>> 49af4eba3aaeb882db4a4e8ab7d78f9673220887
%changelog
*   Thu Mar 24 2022 Brennan Lamoreaux <blamoreaux@vmware.com> 2.1.7-1
-   Initial addition