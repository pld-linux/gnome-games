Summary:	GNOME games
Summary(pl):	GNOME - Gry
Name:		gnome-games
Version:	1.0.42
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Patch:		gnome-games-applnk.patch
Icon:		gnome-games.gif
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	ORBit >= 0.4.3
BuildRequires:	audiofile-devel >= 0.1.5
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	guile-devel >= 1.3
BuildRequires:	esound-devel >= 0.2.7
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_applnkdir	%{_datadir}/applnk

%description
GNOME games.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%package devel
Summary:	GNOME games libraries - header files
Summary(pl):	Pliki nag³ówkowedo tworzenia programów opartych o GNOME games
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description -l pl devel
Pliki nag³ówkowedo tworzenia programów opartych o GNOME games.

%package static
Summary:	GNOME games static libraries
Summary(pl):	Biblioteki statyczne do GNOME games
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static
Biblioteki statyczne do GNOME games

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz
%config /etc/X11/GNOME/sound/events/*

%attr(755,root,root) %{_bindir}/GnomeScott
%attr(755,root,root) %{_bindir}/ctali
%attr(755,root,root) %{_bindir}/freecell
%attr(755,root,root) %{_bindir}/gataxx
%attr(755,root,root) %{_bindir}/sol
%attr(2755,root,games) %{_bindir}/glines
%attr(2755,root,games) %{_bindir}/gnibbles
%attr(2755,root,games) %{_bindir}/gnobots2
%attr(2755,root,games) %{_bindir}/gnome-stones
%attr(2755,root,games) %{_bindir}/gnome-xbill
%attr(2755,root,games) %{_bindir}/gnometris
%attr(2755,root,games) %{_bindir}/gnomine
%attr(2755,root,games) %{_bindir}/gnotravex
%attr(2755,root,games) %{_bindir}/gtali
%attr(2755,root,games) %{_bindir}/gturing
%attr(2755,root,games) %{_bindir}/iagno
%attr(2755,root,games) %{_bindir}/mahjongg
%attr(2755,root,games) %{_bindir}/same-gnome

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gnome-stones
%dir %{_libdir}/gnome-stones/objects
%attr(755,root,root) %{_libdir}/gnome-stones/objects/lib*.so*
%attr(755,root,root) %{_libdir}/gnome-stones/objects/lib*.la

%{_datadir}/gnibbles
%{_datadir}/gnobots2
%{_datadir}/gnome-stones
%{_datadir}/gturing
%{_datadir}/sol-games
%{_datadir}/xbill

%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/sounds/*

%{_datadir}/gnome-stonesrc
%lang(ko) %{_datadir}/gnome-stonesrc.ko

%{_applnkdir}/Games/*.desktop

%dir %{_datadir}/gnome/help/aisleriot
%{_datadir}/gnome/help/aisleriot/C

%dir %{_datadir}/gnome/help/gnobots2
%{_datadir}/gnome/help/gnobots2/C
%lang(es) %{_datadir}/gnome/help/gnobots2/es
%lang(it) %{_datadir}/gnome/help/gnobots2/it

%dir %{_datadir}/gnome/help/gtali
%{_datadir}/gnome/help/gtali/C

%dir %{_datadir}/gnome/help/gturing
%{_datadir}/gnome/help/gturing/C

%dir %{_datadir}/gnome/help/samegnome
%{_datadir}/gnome/help/samegnome/C

%attr(664,root,games) %{_localstatedir}/games/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/gnome-stones/objects/lib*.so
%{_includedir}/*

%files static
%defattr(664,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-stones/objects/lib*.a
