%define upstream_name    ex-lib
%define upstream_version 0.90

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	The same as C<lib>, but makes relative path absolute
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ex/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-PathTools
BuildRequires:	perl(lib::abs) >= 0.900.0
BuildArch:	noarch
Requires:	perl(lib::abs) >= 0.900.0
Provides:	perl(ex::lib) = %{version}-%{release}

%description
The same as C<lib>, but makes relative path absolute

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.900.0-2mdv2011.0
+ Revision: 658425
- rebuild for updated rpm-setup

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.0
+ Revision: 398912
- update to 0.90

* Wed May 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.07-1mdv2010.0
+ Revision: 378032
- update to new version 0.07

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 369665
- update to new version 0.06

* Fri Mar 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 354490
- update to new version 0.05

* Fri Feb 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 343360
- adding missing prereq & provides
- import perl-ex-lib


* Fri Feb 20 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

