Summary:	DEC EDIT/TPU support
Summary(pl):	Obs³uga DEC EDIT/TPU
Name:		xemacs-tpu-pkg
%define 	srcname	tpu
Version:	1.12
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:		http://www.xemacs.org
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs

%description
DEC EDIT/TPU support.

%description -l pl 
Obs³uga DEC EDIT/TPU.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/tpu/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/etc/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/tpu/ChangeLog.gz 
