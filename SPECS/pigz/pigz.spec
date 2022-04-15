Summary:        Parallel Implementation of GZip
Name:           pigz
Version:        2.7
Release:        1%{?dist}
License:        zlib
Group:          Application/Tools
URL:            https://zlib.net/pigz
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://zlib.net/pigz/pigz-%{version}.tar.gz
%define sha1 %{name}=64acd19929e01f04de4e9c481860492b27fe5ec4

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  zlib >= 1.2.3

%description
Fully functional replacement for gzip that exploits multiple processors and multiple cores 
to the hilt when compressing data.

%package devel
Summary: pigz development files

%description devel
pigz header files

%prep
%autosetup -p1

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_includedir}
mv pigz unpigz %{buildroot}%{_bindir}
mv pigz.1 %{buildroot}%{_mandir}
cp *.h %{buildroot}%{_includedir}


%check
%if %{?with_check}
make test
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/pigz
%{_bindir}/unpigz

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_mandir}/*.1

%changelog
*   Thu Mar 24 2022 Brennan Lamoreaux <blamoreaux@vmware.com> 2.1.7-1
-   Initial addition to Photon. Modified from provided pigz source version.