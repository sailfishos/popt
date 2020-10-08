Name:       popt
Summary:    C library for parsing command line parameters
Version:    1.18
Release:    1
License:    MIT
URL:        https://github.com/rpm-software-management/popt/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gettext
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but
it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.


%package devel
Summary:    Development files for the popt library
Requires:   %{name} = %{version}-%{release}

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-static --disable-nls

%make_build

%install
%make_install

# Multiple popt configurations are possible
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_sysconfdir}/popt.d
%{_libdir}/libpopt.so.*

%files devel
%defattr(-,root,root,-)
%doc README
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*
