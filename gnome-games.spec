Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - Gry
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	1.4.0.3
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-games/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-scrollkeeper.patch
Patch2:		%{name}-ac_fix.patch
Icon:		gnome-games.gif
BuildRequires:	ORBit >= 0.4.3
BuildRequires:	audiofile-devel >= 0.1.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	guile-devel >= 1.3
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
GNOME games.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%package devel
Summary:	GNOME games libraries - header files
Summary(pl):	Pliki nag³ówkowe do tworzenia programów opartych o GNOME games
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	gtk+-devel

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów opartych o GNOME games.

%package static
Summary:	GNOME games static libraries
Summary(pl):	Biblioteki statyczne do GNOME games
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static -l pl
Biblioteki statyczne do GNOME games.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}/sound/events/*

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
%attr(2755,root,games) %{_bindir}/gnotski
%attr(2755,root,games) %{_bindir}/gtali
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
%{_datadir}/sol-games
%{_datadir}/xbill

%{_datadir}/gnome-stonesrc
%lang(ko) %{_datadir}/gnome-stonesrc.ko

%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/sounds/*

%{_applnkdir}/Games/*.desktop

%{_omf_dest_dir}/omf/%{name}
%attr(664,root,games) %ghost %{_localstatedir}/games/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-stones/objects/lib*.a
