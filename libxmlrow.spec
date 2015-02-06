%define	major 1
%define libname %mklibname xmlrow %{major}
%define develname %mklibname xmlrow -d

Summary:	The libxmlrow C library
Name:		libxmlrow
Version:	0.2
Release:	5
Group:		System/Libraries
License:	BSD
URL:		http://tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRequires:	libxml2-devel

%description
The libxmlrow C library.

%package -n	%{libname}
Summary:	A memcached C library
Group:          System/Libraries

%description -n	%{libname}
The libxmlrow C shared library.

%package -n	%{develname}
Summary:	Static library and header files for the libxmlrow library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Provides:	xmlrow-devel = %{EVRD}

%description -n	%{develname}
The libxmlrow C library.

This package contains the static libxmlrow library and its header files.

%prep

%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdv2011.0
+ Revision: 620240
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2010.0
+ Revision: 439495
- rebuild

* Thu Nov 27 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2009.1
+ Revision: 307277
- fix deps
- import libxmlrow


* Thu Nov 27 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2009.0
- initial Mandriva package
