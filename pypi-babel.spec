#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-babel
Version  : 2.12.1
Release  : 110
URL      : https://files.pythonhosted.org/packages/ba/42/54426ba5d7aeebde9f4aaba9884596eb2fe02b413ad77d62ef0b0422e205/Babel-2.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ba/42/54426ba5d7aeebde9f4aaba9884596eb2fe02b413ad77d62ef0b0422e205/Babel-2.12.1.tar.gz
Summary  : Internationalization utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-babel-bin = %{version}-%{release}
Requires: pypi-babel-license = %{version}-%{release}
Requires: pypi-babel-python = %{version}-%{release}
Requires: pypi-babel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(freezegun)
BuildRequires : pypi(tzdata)
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description python3
python3 components for the pypi-babel package.


%prep
%setup -q -n Babel-2.12.1
cd %{_builddir}/Babel-2.12.1
pushd ..
cp -a Babel-2.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695148683
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test tests || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-babel
cp %{_builddir}/Babel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/b7c68c0cb76754450f52ca54b4b11d387c854b2a || :
cp %{_builddir}/Babel-%{version}/docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5 || :
cp %{_builddir}/Babel-%{version}/docs/license.rst %{buildroot}/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybabel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-babel/11b5e2224ed952488aa2abbd6c9f41c64a7eca3e
/usr/share/package-licenses/pypi-babel/b7c68c0cb76754450f52ca54b4b11d387c854b2a
/usr/share/package-licenses/pypi-babel/d0eff60551064b040266867c393e035d747b0ae5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
