Summary:	Libical — an implementation of iCalendar protocols and data formats
Name:		libical
Version:	3.0.7
Release: 	1%{?dist}
License:	MPL-2.0
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/libical/libical/releases/download/v%{version}/%{name}-%{version}.tar.gz
%define sha1 libical=6cffa9c188ee4bde003f2279d37ba2e68163fd7a
BuildRequires:  cmake
BuildRequires:  glib-devel
BuildRequires:  libxml2-devel

%description
Libical is an Open Source implementation of the iCalendar protocols and
protocol data units. The iCalendar specification describes how calendar
clients can communicate with calendar servers so users can store their
calendar data and arrange meetings with other users.

%package	devel
Summary:	Development files for Libical
Group:		Development/System
Requires:	%{name} = %{version}-%{release}

%description	devel
The libical-devel package contains libraries and header files for developing
applications that use libical.

%prep
%setup -q

%build
mkdir build
cd build
cmake -DENABLE_GTK_DOC=OFF ..
make

%install
cd build
make DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} -k check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/local/lib64/*.so.*
/usr/local/lib64/cmake/LibIcal/*.cmake
%doc COPYING TODO

%files devel
/usr/local/include/*
/usr/local/lib64/*.so
/usr/local/lib64/*.a
/usr/local/lib64/pkgconfig/*.pc

%changelog
* Mon Jan 6 2020 Ajay Kaher <akaher@vmware.com> 3.0.7-1
- Initial version


