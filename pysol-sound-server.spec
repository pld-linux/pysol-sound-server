Summary:	Sound server for pysol
Summary(pl):	Serwer d¼wiêku dla pysola
Name:		pysol-sound-server
Version:	3.00
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://pysol2.sourceforge.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	fdbfd5c5455b8b51ad469f881870d9f5
URL:		http://www.oberhumer.com/pysol/
BuildRequires:	SDL-devel
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	smpeg-devel
Requires:	pysol >= 4.81
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound server for pysol.

%description -l pl
Serwer d¼wiêku dla pysola.

%prep
%setup -q

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_libdir}

install src/build/lib*/pysolsoundserver.so $RPM_BUILD_ROOT%{py_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{py_libdir}/*
