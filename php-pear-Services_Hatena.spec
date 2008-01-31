%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Hatena
%define		_status		alpha
%define		_pearname	Services_Hatena

Summary:	%{_pearname} - WebServices for Hatena
Summary(pl.UTF-8):	%{_pearname} - dostęp do usług sieciowych Hatena
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f0bbc5b9ef70dc5deab538f9b2f7c5e5
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
%doc install.log docs/%{_pearname}/{docs/IDEAS,docs/MAINTAINERS,docs/STATUS,docs/TESTERS,examples/Hatena_Services_Example_01.php}
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Services/Hatena
%{php_pear_dir}/Services/Hatena/Asin.php
%{php_pear_dir}/Services/Hatena/Autolink.php
%{php_pear_dir}/Services/Hatena/Bookmark.php
%{php_pear_dir}/Services/Hatena/Bookmarknum.php
%{php_pear_dir}/Services/Hatena/Exist.php
%{php_pear_dir}/Services/Hatena/Foto.php
%{php_pear_dir}/Services/Hatena/Search.php
%{php_pear_dir}/Services/Hatena/Similar.php
%{php_pear_dir}/Services/Hatena.php

%files tests
%defattr(644,root,root,755)
%dir %{php_pear_dir}/tests/Services_Hatena
%dir %{php_pear_dir}/tests/Services_Hatena/tests
%{php_pear_dir}/tests/Services_Hatena/tests/Asin.phpt
%{php_pear_dir}/tests/Services_Hatena/tests/Autolink.phpt
%{php_pear_dir}/tests/Services_Hatena/tests/Bookmarknum.phpt
%{php_pear_dir}/tests/Services_Hatena/tests/Exist.phpt
%{php_pear_dir}/tests/Services_Hatena/tests/Search.phpt
%{php_pear_dir}/tests/Services_Hatena/tests/Similar.phpt
