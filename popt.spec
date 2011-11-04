# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       popt
Summary:    C library for parsing command line parameters
Version:    1.16
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.rpm5.org/
Source0:    http://www.rpm5.org/files/%{name}/%{name}-%{version}.tar.gz
Source100:  popt.yaml
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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=/%{_lib} \
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

# Move libpopt.{so,a} to %{_libdir}
rm -f $RPM_BUILD_ROOT/%{_lib}/libpopt.{la,so}
pushd $RPM_BUILD_ROOT/%{_lib}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
ln -sf ../../%{_lib}/$(ls libpopt.so.?.?.?) $RPM_BUILD_ROOT%{_libdir}/libpopt.so
popd

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
/%{_lib}/libpopt.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc README
#%doc doxygen/html
%{_libdir}/libpopt.so
%{_libdir}/pkgconfig/popt.pc
%{_includedir}/popt.h
%doc %{_mandir}/man3/popt.3*
# << files devel
