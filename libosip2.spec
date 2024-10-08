Name: libosip2
Version: 5.3.1
Release: 1%{?dist}
Summary: oSIP is an implementation of SIP
License: LGPL-2.0-or-later

URL: https://www.gnu.org/software/osip/

Source0: https://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

%description
oSIP is an implementation of SIP.

SIP stands for the Session Initiation Protocol and is described by the rfc3261
(wich deprecates rfc2543). This library aims to provide multimedia and telecom
software developers an easy and powerful interface to initiate and control SIP
based sessions in their applications. SIP is a open standard replacement from
IETF for H.323.

%package devel
Summary: Development libraries for oSIP
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The GNU oSIP library is written in C and get no dependencies except the
standard C library. oSIP is thread safe and will generally be used in a
multi-threaded application. Nevertheless, this is optional.

oSIP is little in size and code and thus could be use to implement IP
soft-phone as well as embedded SIP software. oSIP is not limited to endpoint
agents, and can also be used to implement "SIP proxy".

oSIP does not intend to provide a high layer API for controlling "SIP Session"
at this step. Instead, it currently provides an API for the SIP message parser,
SDP message parser, and library to handle "SIP transactions" as defined by the
SIP document.

%prep
%autosetup

%build
autoreconf -fi -I scripts
%configure --disable-static
%make_build

%install
%make_install

# Remove .la files.
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

# Rename and move manpage.
mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING ChangeLog FEATURES HISTORY NEWS README TODO
%{_libdir}/libosip2.so.15*
%{_libdir}/libosipparser2.so.15*

%files devel
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/libosip2.so
%{_libdir}/libosipparser2.so
%{_libdir}/pkgconfig/libosip2.pc
%{_mandir}/man1/osip2.1*

%changelog
%autochangelog