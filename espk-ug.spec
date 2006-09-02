Summary:	LDP Emacs Speak User Guide
Summary(pl):	Podrêcznik LDP dla u¿ytkowników Emacs Speak
Name:		espk-ug
Version:	1.3
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/espk-ug/%{name}.html.tar.gz
# Source0-md5:	7fe2a70206d48d830e4ba641dec2be7a
URL:		http://www.tldp.org/LDP/abs/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document helps Emacspeak users become familiar with Emacs as an
audio desktop and provides tutorials on many common tasks and the
Emacs applications available to perform those tasks.

%description -l pl
Ten dokument pomaga u¿ytkownikom Emacspeak zaznajomiæ siê z Emacsem
jako desktopem g³osowym i dostarcza przyk³adów najczê¶ciej
wykonywanych zadañ. Opisuje te¿ aplikacje Emacsa, które s± przy tym
stosowane.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/espk-ug
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/espk-ug

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/espk-ug
