Summary:	Sound server for pysol
Summary(pl):	Serwer d�wi�ku dla pysol-a
Name:		pysol-sound-server
Version:	2.62
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.oberhumer.com/opensource/pysol/download/%{name}-%{version}.tar.bz2
URL:		http://www.oberhumer.com/pysol
Requires:	pysol
BuildRequires:	python-devel
BuildRequires:	SDL-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _pythonplugindir  /usr/lib/python2.1/site-packages

%description
Sound server for pysol.

%description -l pl
Serwer d�wi�ku dla pysol-a.

%prep
%setup -q

%build
cd src
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pythonplugindir}
install src/build/lib*/pysolsoundserver.so $RPM_BUILD_ROOT%{_pythonplugindir}

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_pythonplugindir}/*
%doc *.gz
