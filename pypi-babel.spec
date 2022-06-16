#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-babel
Version  : 2.10.3
Release  : 97
URL      : https://files.pythonhosted.org/packages/51/27/81e9cf804a34a550a47cc2f0f57fe4935281d479ae3a0ac093d69476f221/Babel-2.10.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/51/27/81e9cf804a34a550a47cc2f0f57fe4935281d479ae3a0ac093d69476f221/Babel-2.10.3.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-babel-bin = %{version}-%{release}
Requires: pypi-babel-license = %{version}-%{release}
Requires: pypi-babel-python = %{version}-%{release}
Requires: pypi-babel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pytz)
BuildRequires : pypi-pytest

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
%setup -q -n Babel-2.10.3
cd %{_builddir}/Babel-2.10.3
pushd ..
cp -a Babel-2.10.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655393317
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-babel
cp %{_builddir}/Babel-2.10.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/461006fda89ca3bf051ce8ff474915073c065b69
cp %{_builddir}/Babel-2.10.3/docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/Babel-2.10.3/docs/license.rst %{buildroot}/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e
/usr/share/package-licenses/pypi-babel/461006fda89ca3bf051ce8ff474915073c065b69
/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
