# $Revision: 1.1 $, $Date: 2011/08/26 04:28:07 $
# TODO
# - tarball snapshots here: http://build.chromium.org/f/client/nacl_archive/sdk/
# - build from source
# - toolchain in nacl-toolchain-newlib
# - current stable (from naclsdk list)
#   description: Native Client SDK Tools, revision 1.11
#   description: Chrome 15 bundle, revision 1239
Summary:	Native Client SDK
Name:		nacl-sdk
Version:	0.6.1074
Release:	0.1
License:	BSD
Group:		Development/Tools
#Source0:	http://commondatastorage.googleapis.com/nativeclient-mirror/nacl/nacl_sdk/naclsdk_linux.tgz
Source0:	nacl-sdk-20110826.tar.bz2
# Source0-md5:	5f1356e698602de7d434c3f6e1d75ded
# don't enable until rel 1
NoSource:	0
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
#setup -q -n native_client_sdk_0_6_1074
%setup -q -n nacl-sdk

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

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: nacl-sdk.spec,v $
Revision 1.1  2011/08/26 04:28:07  glen
- base .spec
