#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-babel
Version  : 2.9.1
Release  : 91
URL      : https://files.pythonhosted.org/packages/17/e6/ec9aa6ac3d00c383a5731cc97ed7c619d3996232c977bb8326bcbb6c687e/Babel-2.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/e6/ec9aa6ac3d00c383a5731cc97ed7c619d3996232c977bb8326bcbb6c687e/Babel-2.9.1.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-babel-bin = %{version}-%{release}
Requires: pypi-babel-license = %{version}-%{release}
Requires: pypi-babel-python = %{version}-%{release}
Requires: pypi-babel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: Babel
Provides: Babel-python
Provides: Babel-python3
BuildRequires : pypi(pytz)
BuildRequires : pytest
BuildRequires : pytz

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the pypi-babel package.
Group: Binaries
Requires: pypi-babel-license = %{version}-%{release}

%description bin
bin components for the pypi-babel package.


%package license
Summary: license components for the pypi-babel package.
Group: Default

%description license
license components for the pypi-babel package.


%package python
Summary: python components for the pypi-babel package.
Group: Default
Requires: pypi-babel-python3 = %{version}-%{release}

%description python
python components for the pypi-babel package.


%package python3
Summary: python3 components for the pypi-babel package.
Group: Default
Requires: python3-core
Provides: pypi(babel)
Requires: pypi(pytz)

%description python3
python3 components for the pypi-babel package.


%prep
%setup -q -n Babel-2.9.1
cd %{_builddir}/Babel-2.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641419997
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-babel
cp %{_builddir}/Babel-2.9.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/2c712b75adbb8352f37d377289596fd88935352d
cp %{_builddir}/Babel-2.9.1/docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/Babel-2.9.1/docs/license.rst %{buildroot}/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e
/usr/share/package-licenses/pypi-babel/2c712b75adbb8352f37d377289596fd88935352d
/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
