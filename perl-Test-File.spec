#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-File
Version  : 1.448
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Test-File-1.448.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Test-File-1.448.tar.gz
Summary  : 'test file attributes'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Test-File-license = %{version}-%{release}
Requires: perl-Test-File-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::utf8)

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Test-File package.
Group: Development
Provides: perl-Test-File-devel = %{version}-%{release}
Requires: perl-Test-File = %{version}-%{release}

%description dev
dev components for the perl-Test-File package.


%package license
Summary: license components for the perl-Test-File package.
Group: Default

%description license
license components for the perl-Test-File package.


%package perl
Summary: perl components for the perl-Test-File package.
Group: Default
Requires: perl-Test-File = %{version}-%{release}

%description perl
perl components for the perl-Test-File package.


%prep
%setup -q -n Test-File-1.448
cd %{_builddir}/Test-File-1.448

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-File
cp %{_builddir}/Test-File-1.448/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-File/d996772fbcb7a7036df0282cb4cc201eefed0d59
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-File/d996772fbcb7a7036df0282cb4cc201eefed0d59

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/File.pm
