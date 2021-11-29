Summary:        Dos Filesystem tools
Name:           dosfstools
Version:        4.1
Release:        1%{?dist}
License:        GPLv3+
URL:            https://github.com/dosfstools
Group:          Filesystem Tools
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%define sha1    dosfstools=db39f667c3cb51bdf321f07f9cf17c726ca50323

%description
dosfstools contains utilities for making and checking MS-DOS FAT filesystems.

%prep
%autosetup -p1

%build
sh ./configure --prefix=%{_prefix} --enable-compat-symlinks
make %{?_smp_mflags}

%install
[ %{buildroot} != "/" ] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} PREFIX="/usr" install %{?_smp_mflags}

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_libdir}/*
%{_mandir}/man8/*
%{_docdir}/dosfstools/*
%exclude %{_mandir}/de/*
%exclude %{_libdir}/debug/*

%changelog
* Tue Oct 17 2017 Xiaolin Li <xiaolinl@vmware.com> 4.1-1
- Update to version 4.1 for CVE-2016-4804, CVE-2015-8872
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.0.26-2
- GA - Bump release of all rpms
* Tue Jul 1 2014 Sharath George <sharathg@vmware.com> 3.0.26-1
- Initial build.  First version
