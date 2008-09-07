%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Hatena
%define		_status		alpha
%define		_pearname	Services_Hatena

Summary:	%{_pearname} - WebServices for Hatena
Summary(pl.UTF-8):	%{_pearname} - dostęp do usług sieciowych Hatena
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e33146e5f9aa644e185e17445f02389f
URL:		http://pear.php.net/package/Services_Hatena/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.3.0
Requires:	php-pear-PEAR >= 1.3.0
Requires:	php-pear-Services_OpenSearch >= 0.0.1
Requires:	php-pear-XML_RPC >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface to Hatena's XML-API.

It provides objects to operate Hatena's Bookmark or Fotolife service,
and get information from Hatena Web Site.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs do XML-API Hatena.

Umożliwia operacje na usługach Hatena's Bookmark lub Hatena's
Fotolife, oraz pobieranie informacji ze stron Hatena.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%doc install.log docs/%{_pearname}/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Hatena
%{php_pear_dir}/Services/Hatena.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Hatena
