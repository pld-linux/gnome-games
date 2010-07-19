Summary:	GNOME games
Summary(es.UTF-8):	Juegos de GNOME
Summary(fr.UTF-8):	Jeux pour GNOME
Summary(pl.UTF-8):	GNOME - gry
Summary(ru.UTF-8):	Игры под GNOME
Summary(uk.UTF-8):	Ігри під GNOME
Summary(wa.UTF-8):	Djeus po GNOME
Name:		gnome-games
Version:	2.30.2
Release:	3
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	1fc03fe2209aa8a70da8f25d6eae1735
Patch0:		%{name}-schemas.patch
URL:		http://live.gnome.org/GnomeGames
BuildRequires:	GConf2-devel >= 2.28.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	check-devel >= 0.9.4
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.10.2
BuildRequires:	dbus-glib-devel >= 0.75
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	guile-devel >= 5:1.6.5
BuildRequires:	intltool >= 0.40.4
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	librsvg-devel >= 1:2.22.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel >= 2:2.14.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-proto-glproto-devel
Requires(post,preun):	GConf2
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.22.0
Obsoletes:	gnect
Obsoletes:	gnome
Obsoletes:	gnome-games-blackjack
Obsoletes:	gnome-games-devel
Obsoletes:	gnome-games-gataxx
Obsoletes:	gnome-games-servers
Obsoletes:	gnome-games-static
Obsoletes:	gnome-games-stones
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var
%define		_gamesdir	%{_localstatedir}/games

%description
Gnome-games is a collection of simple, but addictive, games from the
GNOME desktop project. They represent many of the popular games and
include card games, puzzle games and arcade games.

%description -l pl.UTF-8
Gnome-games jest kolekcją prostych, choć uzależniających gier projektu
GNOME. Są wśród nich reprezentanci wielu popularnych gier, wliczając
karciane, układanki i zręcznościowe.

%description -l uk.UTF-8
Пакет gnome-games включає ігри для середовища робочого столу GNOME,
серед яких GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome та sol.

%description -l ru.UTF-8
Пакет gnome-games включает игры для среды рабочего стола GNOME, среди
которых GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome и sol.

%package glchess
Summary:	GNOME glChess - a 2D/3D chess interface
Summary(pl.UTF-8):	GNOME glChess - dwu i trójwymiarowy interfejs do szachów
Group:		X11/Applications/Games
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-gnome-gconf
Suggests:	crafty
Suggests:	gnuchess
Suggests:	python-PyOpenGL
Suggests:	python-pygtkglext >= 1.1.0-2
Obsoletes:	glchess

%description glchess
glChess is a 2D/3D chess game interfacing via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently
use engines such as GNUChess, Sjeng, Faile, Amy, Crafty and Phalanx.

%description glchess -l pl.UTF-8
glChess to dwu i trójwymiarowa gra w szachy komunikująca się za pomocą
protokołu CECP (Chess Engine Communication Protocol) Tima Manna.
Oznacza to, że aktualnie może używać silników takich jak GNUChess,
Sjeng, Faile, Amy, Crafty i Phalanx.

%package glines
Summary:	Five or more game
Summary(pl.UTF-8):	Gra "Pięć albo więcej"
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description glines
Remove colored balls from the board by forming lines.

%description glines -l pl.UTF-8
Gra polegająca na usuwaniu kolorwych kul poprzez układanie ich w
linie.

%package gnect
Summary:	Four-in-a-row game
Summary(pl.UTF-8):	Gra "Cztery w rzędzie"
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnect
Compete to make lines of the same color.

%description gnect -l pl.UTF-8
Gra, której celem jest utowrzenie linii w jednym kolorze.

%package gnibbles
Summary:	GNOME Nibbles
Summary(pl.UTF-8):	Nibbles dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnibbles
Guide a worm around a maze.

%description gnibbles -l pl.UTF-8
Gra polegająca na przeprowadzeniu robaka przez labirynt.

%package gnobots2
Summary:	GNOME Robots
Summary(pl.UTF-8):	Robots dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnobots2
Avoid the robots and make them crash into each other.

%description gnobots2 -l pl.UTF-8
Gra polegająca na zapobieganiu zderzeniom robotów.

%package gnomine
Summary:	GNOME Mines
Summary(pl.UTF-8):	Miny dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnomine
Clear mines from a minefield.

%description gnomine -l pl.UTF-8
Gra, której celem jest rozminowanie pola minowego.

%package gnotravex
Summary:	GNOME Tetravex
Summary(pl.UTF-8):	Tetravex dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotravex
Puzzle game.

%description gnotravex -l pl.UTF-8
Układanka.

%package gnotski
Summary:	Gnome Klotski
Summary(pl.UTF-8):	Klotski dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotski
Clone of the Klotski game. The objective is to move the patterned
block to the area bordered by green markers.

%description gnotski -l pl.UTF-8
Klon gry Klotski. Celem gry jest przesunięcie zaznaczonego klocka w
pole ograniczone zielonymi znacznikami.

%package gtali
Summary:	GNOME Tali
Summary(pl.UTF-8):	Tali dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gtali
Poker-style dice game.

%description gtali -l pl.UTF-8
Gra w kości w pokerowym stylu.

%package iagno
Summary:	GNOME Iagno
Summary(pl.UTF-8):	Iagno dla GNOME
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description iagno
Reversi like game.

%description iagno -l pl.UTF-8
Gra podobna do Reversi.

%package lightsoff
Summary:	Lights Off
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gir-repository
Requires:	seed

%description lightsoff
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked
tile and its non-diagonal neighbors.

%package mahjongg
Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%description mahjongg -l pl.UTF-8
Gra polegjaca na demontażu stosu kafli poprzez usuwanie pasujących
par.

%package quadrapassel
Summary:	GNOME Tetris
Summary(pl.UTF-8):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	gnome-games-gnometris
Obsoletes:	gnome-games-gnometris

%description quadrapassel
Tetris like game.

%description quadrapassel -l pl.UTF-8
Gra podobna do Tetrisa.

%package sol
Summary:	AisleRiot Solitaire
Summary(pl.UTF-8):	Pasjans AisleRiot
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	guile >= 5:1.6.5

%description sol
Many different solitaire games.

%description sol -l pl.UTF-8
Różne gry karciane.

%package sudoku
Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-gnome-desktop-print >= 2.22.0
Requires:	python-gnome-gconf
Obsoletes:	gnome-sudoku

%description sudoku
GNOME Sudoku provides a simple interface for playing, saving, printing
and solving Sudoku.

%description sudoku -l pl.UTF-8
GNOME Sudoku dostarcza prosty interfejs do grania, zapisywania,
drukowania i rozwiązywania Sudoku.

%package swell-foop
Summary:	Swell Foop
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gir-repository
Requires:	seed
Provides:	gnome-games-same-gnome
Obsoletes:	gnome-games-same-gnome

%description swell-foop
Remove groups of balls to try and clear the screen.

%description swell-foop -l pl.UTF-8
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's/^en@shaw//' po/LINGUAS
%{__rm} -f po/en@shaw.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-games=all \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --all-name
%find_lang gnect --with-gnome --with-omf
%find_lang gnomine --with-gnome --with-omf
%find_lang swell-foop --with-gnome --with-omf
%find_lang mahjongg --with-gnome --with-omf
%find_lang glchess --with-gnome --with-omf
%find_lang gtali --with-gnome --with-omf
%find_lang gnome-sudoku --with-gnome --with-omf
%find_lang gnotravex --with-gnome --with-omf
%find_lang gnotski --with-gnome --with-omf
%find_lang glines --with-gnome --with-omf
%find_lang iagno --with-gnome --with-omf
%find_lang gnobots2 --with-gnome --with-omf
%find_lang gnibbles --with-gnome --with-omf
%find_lang quadrapassel --with-gnome --with-omf
%find_lang aisleriot --with-gnome --with-omf
%find_lang lightsoff --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post glchess
%gconf_schema_install glchess.schemas
%update_desktop_database_post
%scrollkeeper_update_post

%preun glchess
%gconf_schema_uninstall glchess.schemas

%postun glchess
%update_desktop_database_postun
%scrollkeeper_update_postun

%post glines
%scrollkeeper_update_post
%gconf_schema_install glines.schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/glines.scores ]; then
	touch %{_gamesdir}/glines.scores
	chown root:games %{_gamesdir}/glines.scores
	chmod 664 %{_gamesdir}/glines.scores
fi

%preun glines
%gconf_schema_uninstall glines.schemas

%postun glines
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnect
%scrollkeeper_update_post
%gconf_schema_install gnect.schemas
%update_icon_cache hicolor

%preun gnect
%gconf_schema_uninstall gnect.schemas

%postun gnect
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnibbles
%scrollkeeper_update_post
%gconf_schema_install gnibbles.schemas
%update_icon_cache hicolor

for i in gnibbles.1.0 gnibbles.1.1 gnibbles.2.0 gnibbles.2.1 gnibbles.3.0 \
	gnibbles.3.1 gnibbles.4.0 gnibbles.4.1; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%preun gnibbles
%gconf_schema_uninstall gnibbles.schemas

%postun gnibbles
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnobots2
%scrollkeeper_update_post
%gconf_schema_install gnobots2.schemas
%update_icon_cache hicolor

for i in gnobots2.classic_robots-safe gnobots2.classic_robots \
	gnobots2.classic_robots-super-safe gnobots2.nightmare-safe \
	gnobots2.nightmare gnobots2.nightmare-super-safe \
	gnobots2.robots2_easy-safe gnobots2.robots2_easy \
	gnobots2.robots2_easy-super-safe gnobots2.robots2-safe \
	gnobots2.robots2 gnobots2.robots2-super-safe \
	gnobots2.robots_with_safe_teleport-safe \
	gnobots2.robots_with_safe_teleport \
	gnobots2.robots_with_safe_teleport-super-safe; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%preun gnobots2
%gconf_schema_uninstall gnobots2.schemas

%postun	gnobots2
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnomine
%scrollkeeper_update_post
%gconf_schema_install gnomine.schemas
%update_icon_cache hicolor

for i in gnomine.Custom gnomine.Large gnomine.Medium gnomine.Small; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%preun gnomine
%gconf_schema_uninstall gnomine.schemas

%postun gnomine
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnotravex
%scrollkeeper_update_post
%gconf_schema_install gnotravex.schemas
%update_icon_cache hicolor

for i in gnotravex.2x2 gnotravex.3x3 gnotravex.4x4 gnotravex.5x5 \
	gnotravex.6x6; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%preun gnotravex
%gconf_schema_uninstall gnotravex.schemas

%postun gnotravex
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gnotski
%scrollkeeper_update_post
%gconf_schema_install gnotski.schemas
%update_icon_cache hicolor

for i in 1 2 3 4 5 6 7 11 12 13 14 15 16 17 21 22 23 24 25 26; do
	if [ ! -f %{_gamesdir}/gnotski.$i.scores ]; then
	touch %{_gamesdir}/gnotski.$i.scores
	chown root:games %{_gamesdir}/gnotski.$i.scores
	chmod 664 %{_gamesdir}/gnotski.$i.scores
	fi
done

%preun gnotski
%gconf_schema_uninstall gnotski.schemas

%postun gnotski
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gtali
%scrollkeeper_update_post
%gconf_schema_install gtali.schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%preun gtali
%gconf_schema_uninstall gtali.schemas

%postun gtali
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post iagno
%scrollkeeper_update_post
%gconf_schema_install iagno.schemas
%update_icon_cache hicolor

%preun iagno
%gconf_schema_uninstall iagno.schemas

%postun iagno
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post lightsoff
%scrollkeeper_update_post
%gconf_schema_install lightsoff.schemas
%update_icon_cache hicolor

%preun lightsoff
%gconf_schema_uninstall lightsoff.schemas

%postun lightsoff
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post mahjongg
%scrollkeeper_update_post
%gconf_schema_install mahjongg.schemas
%update_icon_cache hicolor

for i in mahjongg.bridges mahjongg.cloud mahjongg.confounding \
	mahjongg.difficult mahjongg.dragon mahjongg.easy \
	mahjongg.pyramid mahjongg.tictactoe mahjongg.ziggurat; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%preun mahjongg
%gconf_schema_uninstall mahjongg.schemas

%postun mahjongg
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post quadrapassel
%scrollkeeper_update_post
%gconf_schema_install quadrapassel.schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/quadrapassel.scores ]; then
	touch %{_gamesdir}/quadrapassel.scores
	chown root:games %{_gamesdir}/quadrapassel.scores
	chmod 664 %{_gamesdir}/quadrapassel.scores
fi

%preun quadrapassel
%gconf_schema_uninstall quadrapassel.schemas

%postun quadrapassel
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post sol
%scrollkeeper_update_post
%gconf_schema_install aisleriot.schemas
%update_icon_cache hicolor

%preun sol
%gconf_schema_uninstall aisleriot.schemas

%postun sol
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post sudoku
%update_icon_cache hicolor
%gconf_schema_install gnome-sudoku.schemas

%preun sudoku
%gconf_schema_uninstall gnome-sudoku.schemas

%postun sudoku
%update_icon_cache hicolor

%post swell-foop
%scrollkeeper_update_post
%gconf_schema_install swell-foop.schemas
%update_icon_cache hicolor

%preun swell-foop
%gconf_schema_uninstall swell-foop.schemas

%postun swell-foop
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/ar-cards-renderer
%attr(755,root,root) %{_libdir}/%{name}/libgames-support-gi.so*
%{_libdir}/girepository-1.0/GnomeGamesSupport-1.0.typelib
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/pixmaps
%{_datadir}/gnome-games-common

%files glchess -f glchess.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glchess
%attr(755,root,root) %{_bindir}/gnome-gnuchess
%{_sysconfdir}/gconf/schemas/glchess.schemas
%{_desktopdir}/glchess.desktop
%{_datadir}/glchess
%{py_sitescriptdir}/glchess
%{_iconsdir}/hicolor/*/*/gnome-glchess.*
%{_mandir}/man6/glchess.6*

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_datadir}/%{name}/glines
%{_desktopdir}/glines.desktop
%{_iconsdir}/hicolor/*/*/gnome-glines.*
%attr(664,root,games) %ghost %{_localstatedir}/games/glines.*
%{_mandir}/man6/glines.6*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_datadir}/%{name}/gnect
%{_desktopdir}/gnect.desktop
%{_iconsdir}/hicolor/*/*/gnome-gnect.*
%{_mandir}/man6/gnect.6*

%files gnibbles -f gnibbles.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnibbles
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%{_datadir}/%{name}/gnibbles
%{_desktopdir}/gnibbles.desktop
%{_iconsdir}/hicolor/*/*/gnome-gnibbles.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnibbles.*
%{_mandir}/man6/gnibbles.6*

%files gnobots2 -f gnobots2.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnobots2
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%{_datadir}/%{name}/gnobots2
%{_desktopdir}/gnobots2.desktop
%{_iconsdir}/hicolor/*/*/gnome-robots.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnobots2.*
%{_mandir}/man6/gnobots2.6*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_datadir}/%{name}/gnomine
%{_desktopdir}/gnomine.desktop
%{_iconsdir}/hicolor/*/*/gnome-mines.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnomine.*
%{_mandir}/man6/gnomine.6*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_desktopdir}/gnotravex.desktop
%{_iconsdir}/hicolor/*/*/gnome-tetravex.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotravex.*
%{_mandir}/man6/gnotravex.6*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_desktopdir}/gnotski.desktop
%{_datadir}/%{name}/gnotski
%{_iconsdir}/hicolor/*/*/gnome-klotski.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotski.*
%{_mandir}/man6/gnotski.6*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_datadir}/%{name}/gtali
%{_desktopdir}/gtali.desktop
%{_iconsdir}/hicolor/*/*/gnome-tali.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gtali.*
%{_mandir}/man6/gtali.6*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_datadir}/%{name}/iagno
%{_desktopdir}/iagno.desktop
%{_iconsdir}/hicolor/*/*/gnome-iagno.*
%{_mandir}/man6/iagno.6*

%files lightsoff -f lightsoff.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lightsoff
%{_datadir}/%{name}/lightsoff
%{_desktopdir}/lightsoff.desktop
%{_sysconfdir}/gconf/schemas/lightsoff.schemas
%{_iconsdir}/hicolor/*/*/gnome-lightsoff.*

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_desktopdir}/mahjongg.desktop
%{_iconsdir}/hicolor/*/*/gnome-mahjongg.png
%{_iconsdir}/hicolor/*/*/gnome-mahjongg.svg
%{_datadir}/%{name}/mahjongg
%attr(664,root,games) %ghost %{_localstatedir}/games/mahjongg.*
%{_mandir}/man6/mahjongg.6*

%files quadrapassel -f quadrapassel.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/quadrapassel
%{_sysconfdir}/gconf/schemas/quadrapassel.schemas
%{_datadir}/%{name}/quadrapassel
%{_desktopdir}/quadrapassel.desktop
%{_iconsdir}/hicolor/*/*/gnome-quadrapassel.*
%attr(664,root,games) %ghost %{_localstatedir}/games/quadrapassel.*
%{_mandir}/man6/quadrapassel.6*

%files sol -f aisleriot.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/sol
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/%{name}/aisleriot
%{_desktopdir}/freecell.desktop
%{_desktopdir}/sol.desktop
%{_iconsdir}/hicolor/*/*/gnome-aisleriot.*
%{_iconsdir}/hicolor/*/*/gnome-freecell.*
%{_mandir}/man6/sol.6*

%files sudoku -f gnome-sudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_datadir}/gnome-sudoku
%{_iconsdir}/hicolor/*/*/gnome-sudoku.*
%{_sysconfdir}/gconf/schemas/gnome-sudoku.schemas
%{_mandir}/man6/gnome-sudoku.6*

%files swell-foop -f swell-foop.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/swell-foop
%{_sysconfdir}/gconf/schemas/swell-foop.schemas
%{_desktopdir}/swell-foop.desktop
%{_datadir}/%{name}/swell-foop
%{_iconsdir}/hicolor/*/*/gnome-swell-foop.*
