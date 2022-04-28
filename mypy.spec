#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mypy
Version  : 0.950
Release  : 78
URL      : https://github.com/python/mypy/archive/v0.950/mypy-0.950.tar.gz
Source0  : https://github.com/python/mypy/archive/v0.950/mypy-0.950.tar.gz
Summary  : Optional static typing for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mypy-bin = %{version}-%{release}
Requires: mypy-license = %{version}-%{release}
Requires: mypy-python = %{version}-%{release}
Requires: mypy-python3 = %{version}-%{release}
Requires: pypi(typed_ast)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

%package bin
Summary: bin components for the mypy package.
Group: Binaries
Requires: mypy-license = %{version}-%{release}

%description bin
bin components for the mypy package.


%package dev
Summary: dev components for the mypy package.
Group: Development
Requires: mypy-bin = %{version}-%{release}
Provides: mypy-devel = %{version}-%{release}
Requires: mypy = %{version}-%{release}

%description dev
dev components for the mypy package.


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
Provides: pypi(mypy)
Requires: pypi(mypy_extensions)
Requires: pypi(tomli)
Requires: pypi(typing_extensions)

%description python3
python3 components for the mypy package.


%prep
%setup -q -n mypy-0.950
cd %{_builddir}/mypy-0.950

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651148924
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mypy
cp %{_builddir}/mypy-0.950/mypy/typeshed/LICENSE %{buildroot}/usr/share/package-licenses/mypy/5a77f6d363db008935cc2907446e3965958f3f10
cp %{_builddir}/mypy-0.950/mypyc/external/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mypy/5a2314153eadadc69258a9429104cd11804ea304
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
/usr/bin/mypyc
/usr/bin/stubgen
/usr/bin/stubtest

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-death-test.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-message.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-param-test.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-printers.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-spi.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-test-part.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest-typed-test.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest_pred_impl.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/gtest_prod.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/custom/gtest-port.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/custom/gtest-printers.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/custom/gtest.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-death-test-internal.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-filepath.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-internal.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-linked_ptr.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-param-util-generated.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-param-util.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-port-arch.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-port.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-string.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-tuple.h
/usr/lib/python3.10/site-packages/mypyc/external/googletest/include/gtest/internal/gtest-type-util.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mypy/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mypy/5a77f6d363db008935cc2907446e3965958f3f10

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
