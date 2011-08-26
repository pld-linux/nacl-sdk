# TODO
# - tarball snapshots here: http://build.chromium.org/f/client/nacl_archive/sdk/
# - build from source
Summary:	Native Client SDK
Name:		nacl-sdk
Version:	0.6.1074
Release:	0.1
License:	BSD
Group:		Development/Tools
Source0:	http://commondatastorage.googleapis.com/nativeclient-mirror/nacl/nacl_sdk/naclsdk_linux.tgz
# Source0-md5:	-
URL:		https://code.google.com/intl/et/chrome/nativeclient/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Native Client is an open source technology for running native compiled
code in the browser, with the goal of maintaining the OS portability
and safety that people expect from web apps. Native Client expands web
programming beyond JavaScript, enabling developers to enhance their
web applications using their preferred language. This technology can
be implemented in any browser and is not tied to a specific CPU
architecture.

The SDK includes toolchain tools: 32- and 64-bit customized Native
Client-compatible versions of standard compilers, linkers, profilers.

%prep
%setup -q -n native_client_sdk_0_6_1074

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING LICENSE NOTICE README
