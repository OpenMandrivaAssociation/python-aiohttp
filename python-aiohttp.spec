%global module aiohttp

Name:		python-aiohttp
Version:	3.11.16
Release:	1
Summary:	Python HTTP client/server for asyncio
License:	ASL 2.0
URL:		https://github.com/aio-libs/aiohttp
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python HTTP client/server for asyncio which supports both the client and the
server side of the HTTP protocol, client and server websocket, and webservers
with middlewares and pluggable routing.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
cython -3 aiohttp/*.pyx -I aiohttp
%py_build

%install
%py_install

%files
%doc CHANGES.rst docs/contributing.rst CONTRIBUTORS.txt README.rst
%license LICENSE.txt
%{python_sitearch}/%{module}-%{version}.dist-info/
%{python_sitearch}/%{module}/
