Name:		consonance
Version:	0.5.1
Release:	%mkrel 1
License:	unknown
Summary:	A lightweight GTK+ music manager
Summary(ru):	Легкий менеджер музыкальных коллекций
Group:		Multimedia/Accesories
URL:		http://sites.google.com/site/consonancemanager
Source:		https://github.com/downloads/sujith/consonance/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

BuildRequires:	dbus-glib, libflac-devel, libgtk+2.0_0-devel, libao-devel, libmad-devel
BuildRequires:	libnotify-devel, libsndfile-devel, libvorbis-devel, sqlite3-devel
BuildRequires:	libmodplug-devel, libcdio-devel, libcddb-devel, libcurl-devel, libtaglib-devel

%description
A lightweight GTK+ music manager

%description -l ru
Легкий менеджер музыкальных коллекций

%prep
%setup
autoreconf
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root,0755)
%doc README ChangeLog FAQ
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*
%{_datadir}/%{name}/data/*.png
%{_datadir}/%{name}/doc/*
%{_mandir}/man1/%{name}.*

%clean
rm -rf $RPM_BUILD_ROOT

