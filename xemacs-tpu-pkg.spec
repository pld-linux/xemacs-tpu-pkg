Summary:	DEC EDIT/TPU support
Summary(pl.UTF-8):   Obsługa DEC EDIT/TPU
Name:		xemacs-tpu-pkg
%define 	srcname	tpu
Version:	1.14
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
URL:		http://www.xemacs.org/
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	f3f5ef913e958e5532a2a682288eac05
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs

%description
DEC EDIT/TPU support.

%description -l pl.UTF-8
Obsługa DEC EDIT/TPU.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%doc lisp/tpu/ChangeLog
