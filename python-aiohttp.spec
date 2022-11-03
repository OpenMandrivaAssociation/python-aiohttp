%global srcname aiohttp

Name:		python-%{srcname}
Version:	3.8.3
Release:	1
Summary:	Python HTTP client/server for asyncio
License:	ASL 2.0
URL:		https://github.com/aio-libs/aiohttp
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
Patch0:		aiohttp-3.8.3-allow-charset-normalizer-3.x.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python-setuptools
BuildRequires:	python-cython

%description
Python HTTP client/server for asyncio which supports both the client and the
server side of the HTTP protocol, client and server websocket, and webservers
with middlewares and pluggable routing.

%prep
%autosetup -p 1 -n %{srcname}-%{version}

%build
cython -3 aiohttp/*.pyx -I aiohttp
%py_build

%install
%py_install

%files
%doc CHANGES.rst docs/contributing.rst CONTRIBUTORS.txt README.rst
%license LICENSE.txt
%{python_sitearch}/%{srcname}-*.*-info/
%{python_sitearch}/%{srcname}/
