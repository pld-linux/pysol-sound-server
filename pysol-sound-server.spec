Summary:	Sound server for PySol
Summary(pl.UTF-8):	Serwer dźwięku dla PySola
Name:		pysol-sound-server
Version:	3.01
Release:	4
License:	GPL v2+
Group:		X11/Applications/Games
#Source0Download: http://www.pysol.org/
Source0:	http://www.pysol.org/download/pysol/%{name}-%{version}.tar.bz2
# Source0-md5:	5ef963dbf5d5c2f032a7e5a90afb536f
URL:		http://www.pysol.org/
BuildRequires:	SDL-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	smpeg-devel
Requires:	pysol >= 4.81
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound server for PySol.

%description -l pl.UTF-8
Serwer dźwięku dla PySola.

%prep
%setup -q

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/pysol

install src/build/lib*/pysolsoundserver.so $RPM_BUILD_ROOT%{py_sitedir}/pysol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{py_sitedir}/pysol/pysolsoundserver.so
