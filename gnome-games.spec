Summary:	GNOME games
Summary(es.UTF-8):	Juegos de GNOME
Summary(fr.UTF-8):	Jeux pour GNOME
Summary(pl.UTF-8):	GNOME - gry
Summary(ru.UTF-8):	Игры под GNOME
Summary(uk.UTF-8):	Ігри під GNOME
Summary(wa.UTF-8):	Djeus po GNOME
Name:		gnome-games
Version:	3.4.1
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	7dc21d85550b58818a8db432f364bf3e
URL:		http://live.gnome.org/GnomeGames
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 1.0.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.40.4
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.15.1
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.32.0
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
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme
Suggests:	crafty
Suggests:	gnuchess
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
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description glines
Remove colored balls from the board by forming lines.

%description glines -l pl.UTF-8
Gra polegająca na usuwaniu kolorowych kul poprzez układanie ich w
linie.

%package gnect
Summary:	Four-in-a-row game
Summary(pl.UTF-8):	Gra "Cztery w rzędzie"
Group:		X11/Applications/Games
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnect
Compete to make lines of the same color.

%description gnect -l pl.UTF-8
Gra, której celem jest utworzenie linii w jednym kolorze.

%package gnibbles
Summary:	GNOME Nibbles
Summary(pl.UTF-8):	Nibbles dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnibbles
Guide a worm around a maze.

%description gnibbles -l pl.UTF-8
Gra polegająca na przeprowadzeniu robaka przez labirynt.

%package gnobots2
Summary:	GNOME Robots
Summary(pl.UTF-8):	Robots dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnobots2
Avoid the robots and make them crash into each other.

%description gnobots2 -l pl.UTF-8
Gra polegająca na zapobieganiu zderzeniom robotów.

%package gnomine
Summary:	GNOME Mines
Summary(pl.UTF-8):	Miny dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnomine
Clear mines from a minefield.

%description gnomine -l pl.UTF-8
Gra, której celem jest rozminowanie pola minowego.

%package gnotravex
Summary:	GNOME Tetravex
Summary(pl.UTF-8):	Tetravex dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gnotravex
Puzzle game.

%description gnotravex -l pl.UTF-8
Układanka.

%package gnotski
Summary:	Gnome Klotski
Summary(pl.UTF-8):	Klotski dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

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
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description gtali
Poker-style dice game.

%description gtali -l pl.UTF-8
Gra w kości w pokerowym stylu.

%package iagno
Summary:	GNOME Iagno
Summary(pl.UTF-8):	Iagno dla GNOME
Group:		X11/Applications/Games
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description iagno
Reversi like game.

%description iagno -l pl.UTF-8
Gra podobna do Reversi.

%package lightsoff
Summary:	Lights Off
Summary(pl.UTF-8):	Gra Lights Off dla GNOME
Group:		X11/Applications/Games
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description lightsoff
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked
tile and its non-diagonal neighbors.

%description lightsoff -l pl.UTF-8
Lights Off to układanka, której celem jest zgaszenie wszystkich pól na
planszy. Każde kliknięcie zmienia stan klikniętego pola oraz jego
najbliższych sąsiadów (nie po przekątnej).

%package mahjongg
Summary:	GNOME Mahjongg
Summary(pl.UTF-8):	Mahjongg dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%description mahjongg -l pl.UTF-8
Gra polegająca na demontażu stosu kafli poprzez usuwanie pasujących
par.

%package quadrapassel
Summary:	GNOME Tetris
Summary(pl.UTF-8):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme
Provides:	gnome-games-gnometris
Obsoletes:	gnome-games-gnometris

%description quadrapassel
Tetris like game.

%description quadrapassel -l pl.UTF-8
Gra podobna do Tetrisa.

%package sudoku
Summary:	Simple interface for playing, saving, printing and solving Sudoku
Summary(pl.UTF-8):	Prosty interfejs do grania, zapisywania, drukowania i rozwiązywania Sudoku
Group:		X11/Applications/Games
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gobject-introspection >= 0.10.0
Requires:	gtk+3
Requires:	hicolor-icon-theme
Requires:	python-pycairo
Requires:	python-pygobject3
Obsoletes:	gnome-sudoku

%description sudoku
GNOME Sudoku provides a simple interface for playing, saving, printing
and solving Sudoku.

%description sudoku -l pl.UTF-8
GNOME Sudoku dostarcza prosty interfejs do grania, zapisywania,
drukowania i rozwiązywania Sudoku.

%package swell-foop
Summary:	Swell Foop
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hicolor-icon-theme
Provides:	gnome-games-same-gnome
Obsoletes:	gnome-games-same-gnome

%description swell-foop
Remove groups of balls to try and clear the screen.

%description swell-foop -l pl.UTF-8
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%prep
%setup -q

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
	--enable-staging \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%py_postclean

%find_lang %{name}
%find_lang gnect --with-gnome
%find_lang gnomine --with-gnome
%find_lang swell-foop --with-gnome
%find_lang mahjongg --with-gnome
%find_lang glchess --with-gnome
%find_lang gtali --with-gnome
%find_lang gnome-sudoku --with-gnome
%find_lang gnotravex --with-gnome
%find_lang gnotski --with-gnome
%find_lang glines --with-gnome
%find_lang iagno --with-gnome
%find_lang gnobots2 --with-gnome
%find_lang gnibbles --with-gnome
%find_lang quadrapassel --with-gnome
%find_lang lightsoff --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%post glchess
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun glchess
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%post glines
%update_icon_cache hicolor
%glib_compile_schemas

if [ ! -f %{_gamesdir}/glines.scores ]; then
	touch %{_gamesdir}/glines.scores
	chown root:games %{_gamesdir}/glines.scores
	chmod 664 %{_gamesdir}/glines.scores
fi

%postun glines
%update_icon_cache hicolor
%glib_compile_schemas

%post gnect
%update_icon_cache hicolor
%glib_compile_schemas

%postun gnect
%update_icon_cache hicolor
%glib_compile_schemas

%post gnibbles
%update_icon_cache hicolor
%glib_compile_schemas

for i in gnibbles.1.0 gnibbles.1.1 gnibbles.2.0 gnibbles.2.1 gnibbles.3.0 \
	gnibbles.3.1 gnibbles.4.0 gnibbles.4.1; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnibbles
%update_icon_cache hicolor
%glib_compile_schemas

%post gnobots2
%glib_compile_schemas
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

%postun	gnobots2
%glib_compile_schemas
%update_icon_cache hicolor

%post gnomine
%glib_compile_schemas
%update_icon_cache hicolor

for i in gnomine.Custom gnomine.Large gnomine.Medium gnomine.Small; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnomine
%update_icon_cache hicolor
%glib_compile_schemas

%post gnotravex
%glib_compile_schemas
%update_icon_cache hicolor

for i in gnotravex.2x2 gnotravex.3x3 gnotravex.4x4 gnotravex.5x5 \
	gnotravex.6x6; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnotravex
%update_icon_cache hicolor
%glib_compile_schemas

%post gnotski
%glib_compile_schemas
%update_icon_cache hicolor

for i in 1 2 3 4 5 6 7 11 12 13 14 15 16 17 21 22 23 24 25 26; do
	if [ ! -f %{_gamesdir}/gnotski.$i.scores ]; then
	touch %{_gamesdir}/gnotski.$i.scores
	chown root:games %{_gamesdir}/gnotski.$i.scores
	chmod 664 %{_gamesdir}/gnotski.$i.scores
	fi
done

%postun gnotski
%glib_compile_schemas
%update_icon_cache hicolor

%post gtali
%glib_compile_schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%postun gtali
%glib_compile_schemas
%update_icon_cache hicolor

%post iagno
%glib_compile_schemas
%update_icon_cache hicolor

%postun iagno
%update_icon_cache hicolor
%glib_compile_schemas

%post lightsoff
%update_icon_cache hicolor
%glib_compile_schemas

%postun lightsoff
%update_icon_cache hicolor
%glib_compile_schemas

%post mahjongg
%glib_compile_schemas
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

%postun mahjongg
%update_icon_cache hicolor
%glib_compile_schemas

%post quadrapassel
%update_icon_cache hicolor
%glib_compile_schemas

if [ ! -f %{_gamesdir}/quadrapassel.scores ]; then
	touch %{_gamesdir}/quadrapassel.scores
	chown root:games %{_gamesdir}/quadrapassel.scores
	chmod 664 %{_gamesdir}/quadrapassel.scores
fi

%postun quadrapassel
%update_icon_cache hicolor
%glib_compile_schemas

%post sudoku
%update_icon_cache hicolor
%glib_compile_schemas

%postun sudoku
%update_icon_cache hicolor
%glib_compile_schemas

%post swell-foop
%update_icon_cache hicolor
%glib_compile_schemas

for i in large normal small; do
	if [ ! -f %{_gamesdir}/swell-foop.$i.scores ]; then
		touch %{_gamesdir}/swell-foop.$i.scores
		chown root:games %{_gamesdir}/swell-foop.$i.scores
		chmod 664 %{_gamesdir}/swell-foop.$i.scores
	fi
done

%postun swell-foop
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libgames-support-gi.so*
%{_libdir}/%{name}/GnomeGamesSupport-1.0.*
%{_datadir}/glib-2.0/schemas/org.gnome.Games.WindowState.gschema.xml
%{_iconsdir}/hicolor/*/*/*.png
%dir %{_datadir}/%{name}

%files glchess -f glchess.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glchess
%{_desktopdir}/glchess.desktop
%{_datadir}/glchess
%{_datadir}/glib-2.0/schemas/org.gnome.glchess.gschema.xml
%{_iconsdir}/hicolor/*/*/glchess.*
%{_mandir}/man6/glchess.6*

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_datadir}/glines
%{_datadir}/glib-2.0/schemas/org.gnome.glines.gschema.xml
%{_desktopdir}/glines.desktop
%{_iconsdir}/hicolor/*/*/glines.*
%attr(664,root,games) %ghost %{_gamesdir}/glines.*
%{_mandir}/man6/glines.6*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_datadir}/gnect
%{_datadir}/glib-2.0/schemas/org.gnome.gnect.gschema.xml
%{_desktopdir}/gnect.desktop
%{_iconsdir}/hicolor/*/*/gnect.*
%{_mandir}/man6/gnect.6*

%files gnibbles -f gnibbles.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnibbles
%{_datadir}/gnibbles
%{_datadir}/glib-2.0/schemas/org.gnome.gnibbles.gschema.xml
%{_desktopdir}/gnibbles.desktop
%{_iconsdir}/hicolor/*/*/gnibbles.*
%attr(664,root,games) %ghost %{_gamesdir}/gnibbles.*
%{_mandir}/man6/gnibbles.6*

%files gnobots2 -f gnobots2.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnobots2
%{_datadir}/gnobots2
%{_datadir}/glib-2.0/schemas/org.gnome.gnobots2.gschema.xml
%{_desktopdir}/gnobots2.desktop
%{_iconsdir}/hicolor/*/*/gnobots2.*
%attr(664,root,games) %ghost %{_gamesdir}/gnobots2.*
%{_mandir}/man6/gnobots2.6*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_datadir}/gnomine
%{_datadir}/glib-2.0/schemas/org.gnome.gnomine.gschema.xml
%{_desktopdir}/gnomine.desktop
%{_iconsdir}/hicolor/*/*/gnomine.*
%attr(664,root,games) %ghost %{_gamesdir}/gnomine.*
%{_mandir}/man6/gnomine.6*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_datadir}/glib-2.0/schemas/org.gnome.gnotravex.gschema.xml
%{_desktopdir}/gnotravex.desktop
%{_datadir}/gnotravex
%{_iconsdir}/hicolor/*/*/gnotravex.*
%attr(664,root,games) %ghost %{_gamesdir}/gnotravex.*
%{_mandir}/man6/gnotravex.6*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_desktopdir}/gnotski.desktop
%{_datadir}/gnotski
%{_datadir}/glib-2.0/schemas/org.gnome.gnotski.gschema.xml
%{_iconsdir}/hicolor/*/*/gnotski.*
%attr(664,root,games) %ghost %{_gamesdir}/gnotski.*
%{_mandir}/man6/gnotski.6*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_datadir}/gtali
%{_datadir}/glib-2.0/schemas/org.gnome.gtali.gschema.xml
%{_desktopdir}/gtali.desktop
%{_iconsdir}/hicolor/*/*/gtali.*
%attr(664,root,games) %ghost %{_gamesdir}/gtali.*
%{_mandir}/man6/gtali.6*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_datadir}/iagno
%{_datadir}/glib-2.0/schemas/org.gnome.iagno.gschema.xml
%{_desktopdir}/iagno.desktop
%{_iconsdir}/hicolor/*/*/iagno.*
%{_mandir}/man6/iagno.6*

%files lightsoff -f lightsoff.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lightsoff
%{_datadir}/lightsoff
%{_datadir}/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
%{_desktopdir}/lightsoff.desktop
%{_iconsdir}/hicolor/*/*/lightsoff.*

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_datadir}/glib-2.0/schemas/org.gnome.mahjongg.gschema.xml
%{_desktopdir}/mahjongg.desktop
%{_iconsdir}/hicolor/*/*/mahjongg.*
%{_datadir}/mahjongg
%attr(664,root,games) %ghost %{_gamesdir}/mahjongg.*
%{_mandir}/man6/mahjongg.6*

%files quadrapassel -f quadrapassel.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/quadrapassel
%{_datadir}/quadrapassel
%{_datadir}/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%{_desktopdir}/quadrapassel.desktop
%{_iconsdir}/hicolor/*/*/quadrapassel.*
%attr(664,root,games) %ghost %{_gamesdir}/quadrapassel.*
%{_mandir}/man6/quadrapassel.6*

%files sudoku -f gnome-sudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_datadir}/gnome-sudoku
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml
%{_iconsdir}/hicolor/*/*/gnome-sudoku.*
%{_mandir}/man6/gnome-sudoku.6*

%files swell-foop -f swell-foop.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/swell-foop
%{_desktopdir}/swell-foop.desktop
%{_datadir}/gnome-games/swell-foop
%{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%{_iconsdir}/hicolor/*/*/swell-foop.*
%attr(664,root,games) %ghost %{_gamesdir}/swell-foop.*
