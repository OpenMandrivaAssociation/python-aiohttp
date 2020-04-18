%global srcname aiohttp
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        3.6.2
Release:        2%{?dist}
Summary:        Python HTTP client/server for asyncio

License:        ASL 2.0
URL:            https://github.com/aio-libs/aiohttp
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Unbundle http-parser
Patch0:         unbundle-http-parser.patch

BuildRequires:  http-parser-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-cython

%description
Python HTTP client/server for asyncio which supports both the client and the
server side of the HTTP protocol, client and server websocket, and webservers
with middlewares and pluggable routing.

%prep
%autosetup -p 1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc CHANGES.rst CONTRIBUTING.rst CONTRIBUTORS.txt HISTORY.rst README.rst
%license LICENSE.txt
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/
