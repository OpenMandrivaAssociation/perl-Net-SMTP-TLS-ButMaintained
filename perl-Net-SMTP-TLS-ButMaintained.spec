%define upstream_name    Net-SMTP-TLS-ButMaintained
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An SMTP client supporting TLS and AUTH
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::HMAC_MD5)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Net::Cmd)
BuildRequires: perl(Net::SSLeay)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*Net::SMTP::TLS::ButMaintained* is forked from the Net::SMTP::TLS manpage.
blame 'Evan Carroll' for the idea. :)

*Net::SMTP::TLS::ButMaintained* is a TLS and AUTH capable SMTP client which
offers an interface that users will find familiar from the Net::SMTP
manpage. *Net::SMTP::TLS::ButMaintained* implements a subset of the methods
provided by that module, but certainly not (yet) a complete mirror image of
that API.

The methods supported by *Net::SMTP::TLS::ButMaintained* are used in the
above example. Though self explanatory for the most part, please see the
perldoc for the Net::SMTP manpage if you are unclear.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


