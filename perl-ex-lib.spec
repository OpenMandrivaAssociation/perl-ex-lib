%define upstream_name    ex-lib
%define upstream_version 0.90

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    The same as C<lib>, but makes relative path absolute
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ex/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl-PathTools
BuildRequires: perl(lib::abs) >= 0.900.0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch
Requires: perl(lib::abs) >= 0.900.0
Provides: perl(ex::lib)


%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

