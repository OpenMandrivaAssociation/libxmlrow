%define	major 1
%define libname %mklibname xmlrow %{major}
%define develname %mklibname xmlrow -d

Summary:	The libxmlrow C library
Name:		libxmlrow
Version:	0.2
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRequires:	libxml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{name}-devel = %{version}-%{release}
Provides:	xmlrow-devel = %{version}-%{release}

%description -n	%{develname}
The libxmlrow C library.

This package contains the static libxmlrow library and its header files.

%prep

%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

