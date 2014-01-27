# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       popt

# >> macros
# << macros

Summary:    C library for parsing command line parameters
Version:    1.16
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.rpm5.org/
Source0:    http://www.rpm5.org/files/%{name}/%{name}-%{version}.tar.gz
Source100:  popt.yaml
Patch0:     popt-aarch64.patch
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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --disable-nls

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# Multiple popt configurations are possible
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/popt.d
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_sysconfdir}/popt.d
%{_libdir}/libpopt.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%doc README
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/popt.pc
%{_includedir}/popt.h
%doc %{_mandir}/man3/popt.3*
# << files devel
