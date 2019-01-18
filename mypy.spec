#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mypy
Version  : 0.660
Release  : 24
URL      : https://github.com/python/mypy/archive/v0.660.tar.gz
Source0  : https://github.com/python/mypy/archive/v0.660.tar.gz
Summary  : Optional static typing for Python 2 and 3 (PEP484)
Group    : Development/Tools
License  : Python-2.0
Requires: mypy-bin = %{version}-%{release}
Requires: mypy-license = %{version}-%{release}
Requires: mypy-python = %{version}-%{release}
Requires: mypy-python3 = %{version}-%{release}
Requires: mypy_extensions
Requires: typed-ast
BuildRequires : buildreq-distutils3
BuildRequires : mypy_extensions
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : typed-ast
BuildRequires : virtualenv

%description
<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

%package bin
Summary: bin components for the mypy package.
Group: Binaries
Requires: mypy-license = %{version}-%{release}

%description bin
bin components for the mypy package.


%package license
Summary: license components for the mypy package.
Group: Default

%description license
license components for the mypy package.


%package python
Summary: python components for the mypy package.
Group: Default
Requires: mypy-python3 = %{version}-%{release}

%description python
python components for the mypy package.


%package python3
Summary: python3 components for the mypy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mypy package.


%prep
%setup -q -n mypy-0.660

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547741169
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mypy
cp LICENSE %{buildroot}/usr/share/package-licenses/mypy/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dmypy
/usr/bin/mypy
/usr/bin/stubgen

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mypy/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
