Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	Игры под GNOME
Summary(uk):	╤гри п╕д GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.5.0
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	5f2ab0452635ee88280dd758efd290d8
Patch0:		%{name}-schemas.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.5.1
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	gtk+2-devel >= 1:2.3.0
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.5.0
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	scrollkeeper
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.4.0
Obsoletes:	gnect
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var

%description
GNOME games.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%description -l uk
Пакет gnome-games включа╓ ╕гри для середовища робочого столу GNOME,
серед яких GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome та sol.

%description -l ru
Пакет gnome-games включает игры для среды рабочего стола GNOME, среди
которых GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome и sol.

%package devel
Summary:	GNOME games libraries - header files
Summary(pl):	Pliki nagЁСwkowe do tworzenia programСw opartych o GNOME games
Summary(ru):	Файлы разработки игр под GNOME
Summary(uk):	Файли розробки ╕гр п╕д GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	gtk+2-devel >= 2.2.4

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description devel -l pl
Pliki nagЁСwkowe do tworzenia programСw opartych o GNOME games.

%description devel -l uk
Пакет gnome-games-devel встановлю╓ файли, необх╕дн╕ для розробки ╕гор
п╕д GNOME.

%description devel -l ru
Пакет gnome-games-devel устанавливает файлы, необходимые для
разработки игр под GNOME.

%package static
Summary:	GNOME games static libraries
Summary(pl):	Biblioteki statyczne do GNOME games
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GNOME games static libraries.

%description static -l pl
Biblioteki statyczne do GNOME games.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config %{_sysconfdir}/sound/events/*
%{_sysconfdir}/gconf/schemas/*

%attr(755,root,root) %{_bindir}/gataxx
%attr(755,root,root) %{_bindir}/sol
%attr(755,root,root) %{_bindir}/gnect
%attr(755,root,root) %{_bindir}/gnibbles
%attr(755,root,root) %{_bindir}/gnobots2
%attr(755,root,root) %{_bindir}/blackjack
%attr(2755,root,games) %{_bindir}/glines
%attr(2755,root,games) %{_bindir}/gnome-stones
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
%{_libdir}/gnome-stones/objects/lib*.la

%{_datadir}/gnome-stones
%{_datadir}/sol-games
%{_datadir}/blackjack

%{_datadir}/gnome-stonesrc
%lang(ko) %{_datadir}/gnome-stonesrc.ko

%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/sounds/*
%{_desktopdir}/*
%{_datadir}/gnect
%{_datadir}/gnibbles
%{_datadir}/gnobots2

%{_omf_dest_dir}/%{name}
%attr(664,root,games) %ghost %{_localstatedir}/games/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-stones/objects/lib*.a
