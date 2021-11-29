%global security_hardening none
%global commit          553f4857346faa8c5f6ddf9eced4180924890bfc.tar.bz2
%define debug_package %{nil}

Summary:        iPXE open source boot firmware
Name:           ipxe
Version:        553f485
Release:        1%{?dist}
License:        GPLv2
URL:            http://ipxe.org
Group:          System Environment/Daemons
Vendor:         VMware, Inc.
Distribution:   Photon

#Download URL:  https://git.ipxe.org/ipxe.git/snapshot/%{commit}.tar.bz2
Source0:        %{name}-%{version}.tar.bz2
%define sha1 %{name}=723e1e46b00a7de870065b74f053941f46748062

BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  cdrkit
BuildRequires:  gcc
BuildRequires:  libgcc
BuildRequires:  libgcc-devel
BuildRequires:  make
BuildRequires:  linux
BuildRequires:  linux-dev
BuildRequires:  perl
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib
BuildRequires:  zlib-devel

%description
iPXE is the leading open source network boot firmware. It provides a full
PXE implementation enhanced with additional features.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
cd src
make %{_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
mkdir -p %{buildroot}%{_datadir}/%{name}
install -vDm 644 src/bin/%{name}.{dsk,iso,lkrn,usb} %{buildroot}%{_datadir}/%{name}/
install -vDm 644 src/bin/*.{rom,mrom} %{buildroot}%{_datadir}/%{name}/

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root)
%{_datadir}/%{name}/%{name}.dsk
%{_datadir}/%{name}/%{name}.iso
%{_datadir}/%{name}/%{name}.lkrn
%{_datadir}/%{name}/%{name}.usb
%{_datadir}/%{name}/10222000.rom
%{_datadir}/%{name}/10500940.rom
%{_datadir}/%{name}/10ec8139.rom
%{_datadir}/%{name}/15ad07b0.rom
%{_datadir}/%{name}/1af41000.rom
%{_datadir}/%{name}/8086100e.mrom
%{_datadir}/%{name}/8086100f.mrom
%{_datadir}/%{name}/808610d3.mrom
%{_datadir}/%{name}/80861209.rom
%{_datadir}/%{name}/rtl8139.rom

%changelog
*   Wed Jun 06 2018 Xiaolin Li <xiaolinl@vmware.com> 553f485-1
-   Update to 553f485 after upgraded perl to 5.24.1
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> ed0d7c4-2
-   GA - Bump release of all rpms
*   Thu Nov 12 2015 Vinay Kulkarni <kulkarniv@vmware.com> ed0d7c4-1
-   Initial build. First version
