%include	/usr/lib/rpm/macros.python
Summary:	Sound server for pysol
Summary(pl):	Serwer d¼wiêku dla pysol-a
Name:		pysol-sound-server
Version:	2.62
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.oberhumer.com/opensource/pysol/download/%{name}-%{version}.tar.bz2
URL:		http://www.oberhumer.com/pysol
BuildRequires:	SDL-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	smpeg-devel
Requires:	pysol
%requires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound server for pysol.

%description -l pl
Serwer d¼wiêku dla pysol-a.

%prep
%setup -q

%build
cd src
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_libdir}

install src/build/lib*/pysolsoundserver.so $RPM_BUILD_ROOT%{py_libdir}

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{py_libdir}/*
