#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	HDF4
Summary:	Alien::HDF4 - encapsulate install info for HDF4
Summary(pl.UTF-8):	Alien::HDF4 - opakowanie informacji o instalacji HDF4
Name:		perl-Alien-HDF4
Version:	0.06
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f91416a74e4644639fd2b081c33c2060
URL:		https://metacpan.org/dist/Alien-HDF4
BuildRequires:	hdf-devel >= 1:4.2
BuildRequires:	perl-ExtUtils-Depends >= 0.402
BuildRequires:	perl-IO-All
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Requires:	hdf-devel >= 1:4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binaries, not noarch due to arch-dependent paths
%define		_enable_debug_packages	0

%description
Alien::HDF4 - encapsulate install info for HDF4.

%description -l pl.UTF-8
Alien::HDF4 - opakowanie informacji o instalacji HDF4.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e 's/\.a/.so/' common.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Alien/HDF4.pm
%{perl_vendorarch}/Alien/HDF4
%{_mandir}/man3/Alien::HDF4.3pm*
%{_mandir}/man3/Alien::HDF4::Install::Files.3pm*
