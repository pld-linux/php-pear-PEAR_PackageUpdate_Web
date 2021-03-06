%define		_status		stable
%define		_pearname	PEAR_PackageUpdate_Web
Summary:	%{_pearname} - A Web front end for PEAR_PackageUpdate
Summary(pl.UTF-8):	%{_pearname} - frontend WWW do PEAR_PackageUpdate
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP License 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5bf47f866a6497266fedf5e64879cfda
URL:		http://pear.php.net/package/PEAR_PackageUpdate_Web/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.6
Requires:	php-pear-PEAR_PackageUpdate >= 1.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEAR_PackageUpdate (PPU) is designed to allow developers to easily
include auto updating features for other packages and PEAR installable
applications.

PEAR_PackageUpdate_Web is a HTML web front end for PPU.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR_PackageUpdate (PPU) został zaprojektowany aby ułatwić
programistom dołączanie funkcjonalności automatycznej aktualizacji
innych pakietów oraz aplikacji PEAR.

PEAR_PackageUpdate_Web to frontend www do PPU.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/{examples/ppuWebExample1.php,examples/ppuWebExample2.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageUpdate/Web.php
%{php_pear_dir}/data/PEAR_PackageUpdate_Web
