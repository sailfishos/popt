Name:       popt


Summary:    C library for parsing command line parameters
Version:    1.16
Release:    2
Group:      System/Libraries
License:    MIT
URL:        http://www.rpm5.org/
Source0:    http://www.rpm5.org/files/%{name}/%{name}-%{version}.tar.gz
Patch0:     001-popt-fix-build-automake-1.12.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  gettext

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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.



%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build

autoreconf -fiv
%configure --disable-static \
    --disable-nls

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

# Multiple popt configurations are possible
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/popt.d
%{_libdir}/libpopt.so.*

%files devel
%defattr(-,root,root,-)
%doc README
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/popt.pc
%{_includedir}/popt.h
%doc %{_mandir}/man3/popt.3*
