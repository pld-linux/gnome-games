Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	éÇÒÙ ÐÏÄ GNOME
Summary(uk):	¶ÇÒÉ Ð¦Ä GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.7.3
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	ca563f78f21921687763fd9fa9f3b8fc
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-cxx_warnings.patch
Icon:		gnome-games.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gnome-vfs2-devel >= 2.7.1
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnome-devel >= 2.7.1
BuildRequires:	libgnomeui-devel >= 2.7.1
BuildRequires:	libltdl-devel
BuildRequires:	librsvg >= 1:2.6.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.7.1
Requires:	librsvg >= 1:2.6.4
Obsoletes:	gnect
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var

%description
Gnome-games is a collection of simple, but addictive, games from the              
GNOME desktop project. They represent many of the popular games and               
include card games, puzzle games and arcade games.

%description -l pl
Gnome-games jest kolekcj± prostych, choæ uzale¿niaj±cych gier projektu
GNOME. S± w¶ród nich reprezentanci wielu popularnych gier, wliczaj±c
karciane, uk³adanki i zrêczno¶ciowe.

%package blackjack
Summary:	GNOME's version of blackjack
Summary(pl):	Blackjack dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description blackjack
Casino card game Blackjack.

%description blackjack -l pl
Kasynowa wersja gry oczko.

%package freecell
Summary:	FreeCell Solitaire
Summary(pl):	Pasjans FreeCell
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description freecell
FreeCell card game.

%description freecell -l pl
Kolejna gra karciana FreeCell.

%package glines
Summary:	Five or more game
Summary(pl):	Gra "Piêæ albo wiêcej"
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description glines
Remove colored balls from the board by forming lines.

%description glines -l pl
Gra polegaj±ca na usuwaniu kolorwych kul poprzez uk³adanie ich w
linie.

%package gnect
Summary:	Four-in-a-row game
Summary(pl):	Gra "Cztery w rzêdzie"
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnect
Compete to make lines of the same color.

%description gnect -l pl
Gra, której celem jest utowrzenie linii w jednym kolorze.


%package gnibbles
Summary:	GNOME Nibbles
Summary(pl):	Nibbles dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnibbles
Guide a worm around a maze.

%description gnibbles -l pl
Gra polegaj±ca na przeprowadzeniu robaka przez labirynt.

%package gnobots2
Summary:	GNOME Robots
Summary(pl):	Robots dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnobots2
Avoid the robots and make them crash into each other.

%description gnobots2 -l pl
Gra polegaj±ca na zapobieganiu zderzeniom robotów.

%package stones
Summary:	GNOME Stones
Summary(pl):	"Kamienie" dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description stones
Boulder Dash like game.

%description stones -l pl
Gra podobna do Boulder Dasha.

%package gnometris
Summary:	GNOME Tetris
Summary(pl):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnometris
Tetris like game.

%description gnometris -l pl
Gra podobna do Tetrisa.

%package gnomine
Summary:	GNOME Mines
Summary(pl):	Miny dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnomine
Clear mines from a minefield.

%description gnomine -l pl
Gra, której celem jest rozminowanie pola minowego.

%package gnotravex
Summary:	GNOME Tetravex
Summary(pl):	Tetravex dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gnotravex
Puzzle game.

%description gnotravex -l pl
Uk³adanka.

%package gtali
Summary:	GNOME Tali
Summary(pl):	Tali dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description gtali
Poker-style dice game.

%description gtali -l pl
Gra w ko¶ci w pokerowym stylu.

%package iagno
Summary:	GNOME Iagno
Summary(pl):	Iagno dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description iagno
Reversi like game.

%description iagno -l pl
Gra podobna do Reversi.

%package mahjongg
Summary:	GNOME Mahjongg
Summary(pl):	Mahjongg dla GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%description mahjongg -l pl
Gra polegjaca na demonta¿u stosu kafli poprzez usuwanie pasuj±cych
par.

%package same-gnome
Summary:	Same GNOME
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description same-gnome
Remove groups of balls to try and clear the screen.

%description same-gnome -l pl
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%package sol
Summary:	AisleRiot Solitaire
Summary(pl):	Pasjans AisleRiot
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description sol
Many different solitaire games.

%description sol -l pl
Ró¿ne gry karciane.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
cp -f /usr/share/automake/config.sub .
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
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
