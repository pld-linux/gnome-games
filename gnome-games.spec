#
# TODO:
# - system libggz (http://www.ggzgamingzone.org/)
#
Summary:	GNOME games
Summary(es.UTF-8):	Juegos de GNOME
Summary(fr.UTF-8):	Jeux pour GNOME
Summary(pl.UTF-8):	GNOME - gry
Summary(ru.UTF-8):	Игры под GNOME
Summary(uk.UTF-8):	Ігри під GNOME
Summary(wa.UTF-8):	Djeus po GNOME
Name:		gnome-games
Version:	2.19.92
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	ae47893206f44c97333eb8f6b56716aa
Patch0:		%{name}-schemas.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	check >= 0.9.4
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gnome-vfs2-devel >= 2.19.91
BuildRequires:	gtk+2-devel >= 2:2.10.14
BuildRequires:	guile-devel >= 5:1.6.5
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	librsvg-devel >= 1:2.18.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.29
BuildRequires:	pkgconfig >= 1:0.15
BuildRequires:	python-devel >= 2.4
BuildRequires:	python-gnome-desktop-devel >= 2.19.2
BuildRequires:	python-pygtk-devel >= 2:2.10.4
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.19.91
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.19.1
Requires:	librsvg >= 1:2.18.2
Obsoletes:	gnect
Obsoletes:	gnome
Obsoletes:	gnome-games-devel
Obsoletes:	gnome-games-gataxx
Obsoletes:	gnome-games-static
Obsoletes:	gnome-games-stones
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var
%define		_gnomehelpdir	%{_datadir}/gnome/help
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

%package blackjack
Summary:	GNOME's version of blackjack
Summary(pl.UTF-8):	Blackjack dla GNOME
Group:		X11/Applications/Games
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description blackjack
Casino card game Blackjack.

%description blackjack -l pl.UTF-8
Kasynowa wersja gry oczko.

%package glchess
Summary:	GNOME glChess - a 2D/3D chess interface
Summary(pl.UTF-8):	GNOME glChess - dwu i trójwymiarowy interfejs do szachów
Group:		X11/Applications/Games
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	python-pygtkglext >= 1.1.0-2
Suggests:	python-PyOpenGL
Obsoletes:	glchess

%description glchess
glChess is a 2D/3D chess game interfacing via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently
use engines such as GNUChess, Sjeng, Faile, Amy, Crafty and Phalanx.

%description glchess -l pl.UTF-8
glChess to dwu i trójwymiarowa gra w szachy komunikująca się za
pomocą protokołu CECP (Chess Engine Communication Protocol) Tima
Manna. Oznacza to, że aktualnie może używać silników takich jak
GNUChess, Sjeng, Faile, Amy, Crafty i Phalanx.

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

%package gnometris
Summary:	GNOME Tetris
Summary(pl.UTF-8):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnometris
Tetris like game.

%description gnometris -l pl.UTF-8
Gra podobna do Tetrisa.

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

%package same-gnome
Summary:	Same GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description same-gnome
Remove groups of balls to try and clear the screen.

%description same-gnome -l pl.UTF-8
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-gnome-desktop-print >= 2.19.2
Obsoletes:	gnome-sudoku

%description sudoku
GNOME Sudoku provides a simple interface for playing, saving, printing
and solving Sudoku.

%description sudoku -l pl.UTF-8
GNOME Sudoku dostarcza prosty interfejs do grania, zapisywania,
drukowania i rozwiązywania Sudoku.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-games=all \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-stones/objects/lib*.la

%py_postclean

%find_lang %{name} --all-name
%find_lang gnect --with-gnome
%find_lang gnomine --with-gnome
%find_lang same-gnome --with-gnome
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
%find_lang gnometris --with-gnome
%find_lang blackjack --with-gnome
%find_lang aisleriot --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post blackjack
%scrollkeeper_update_post
%gconf_schema_install blackjack.schemas
%update_icon_cache hicolor

%preun blackjack
%gconf_schema_uninstall blackjack.schemas

%postun blackjack
%scrollkeeper_update_postun
%update_icon_cache hicolor

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

%post gnometris
%scrollkeeper_update_post
%gconf_schema_install gnometris.schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/gnometris.scores ]; then
	touch %{_gamesdir}/gnometris.scores
	chown root:games %{_gamesdir}/gnometris.scores
	chmod 664 %{_gamesdir}/gnometris.scores
fi

%preun gnometris
%gconf_schema_uninstall gnometris.schemas

%postun gnometris
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

%post same-gnome
%scrollkeeper_update_post
%gconf_schema_install same-gnome.schemas
%update_icon_cache hicolor

if [ ! -f %{_gamesdir}/same-gnome.scores ]; then
	touch %{_gamesdir}/same-gnome.scores
	chown root:games %{_gamesdir}/same-gnome.scores
	chmod 664 %{_gamesdir}/same-gnome.scores
fi

%preun same-gnome
%gconf_schema_uninstall same-gnome.schemas

%postun same-gnome
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/gnome-games-render-cards
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/pixmaps
%{_datadir}/gnome-games-common
%dir %{_datadir}/ggz
%{_datadir}/ggz/gnome-games
%dir %{_omf_dest_dir}/%{name}

%files blackjack -f blackjack.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blackjack
%{_sysconfdir}/gconf/schemas/blackjack.schemas
%{_datadir}/%{name}/blackjack
%{_desktopdir}/blackjack.desktop
%dir %{_omf_dest_dir}/blackjack
%{_omf_dest_dir}/blackjack/blackjack-C.omf
%lang(es) %{_omf_dest_dir}/blackjack/blackjack-es.omf
%lang(fr) %{_omf_dest_dir}/blackjack/blackjack-fr.omf
%lang(oc) %{_omf_dest_dir}/blackjack/blackjack-oc.omf
%lang(sv) %{_omf_dest_dir}/blackjack/blackjack-sv.omf
%{_iconsdir}/hicolor/*/*/gnome-blackjack.*

%files glchess -f glchess.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glchess
%attr(755,root,root) %{_bindir}/gnome-gnuchess
%{_sysconfdir}/gconf/schemas/glchess.schemas
%{_desktopdir}/glchess.desktop
%{_datadir}/glchess
%{py_sitescriptdir}/glchess
%{_pixmapsdir}/glchess
%dir %{_omf_dest_dir}/glchess
%{_omf_dest_dir}/glchess/glchess-C.omf
%lang(es) %{_omf_dest_dir}/glchess/glchess-es.omf
%lang(fr) %{_omf_dest_dir}/glchess/glchess-fr.omf
%lang(oc) %{_omf_dest_dir}/glchess/glchess-oc.omf
%lang(sv) %{_omf_dest_dir}/glchess/glchess-sv.omf
%{_iconsdir}/hicolor/*/*/gnome-glchess.*

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_desktopdir}/glines.desktop
%{_pixmapsdir}/glines
%{_iconsdir}/hicolor/*/*/gnome-glines.*
%dir %{_omf_dest_dir}/glines
%{_omf_dest_dir}/glines/glines-C.omf
%lang(en_GB) %{_omf_dest_dir}/glines/glines-en_GB.omf
%lang(es) %{_omf_dest_dir}/glines/glines-es.omf
%lang(fr) %{_omf_dest_dir}/glines/glines-fr.omf
%lang(oc) %{_omf_dest_dir}/glines/glines-oc.omf
%lang(ru) %{_omf_dest_dir}/glines/glines-ru.omf
%lang(sv) %{_omf_dest_dir}/glines/glines-sv.omf
%attr(664,root,games) %ghost %{_localstatedir}/games/glines.*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_datadir}/gnect
%{_desktopdir}/gnect.desktop
%{_pixmapsdir}/gnect
%{_iconsdir}/hicolor/*/*/gnome-gnect.*
%dir %{_omf_dest_dir}/gnect
%{_omf_dest_dir}/gnect/gnect-C.omf
%lang(en_GB) %{_omf_dest_dir}/gnect/gnect-en_GB.omf
%lang(es) %{_omf_dest_dir}/gnect/gnect-es.omf
%lang(fr) %{_omf_dest_dir}/gnect/gnect-fr.omf
%lang(oc) %{_omf_dest_dir}/gnect/gnect-oc.omf
%lang(sv) %{_omf_dest_dir}/gnect/gnect-sv.omf

%files gnibbles -f gnibbles.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnibbles
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%{_datadir}/gnibbles
%{_desktopdir}/gnibbles.desktop
%dir %{_omf_dest_dir}/gnibbles
%{_omf_dest_dir}/gnibbles/gnibbles-C.omf
%lang(es) %{_omf_dest_dir}/gnibbles/gnibbles-es.omf
%lang(oc) %{_omf_dest_dir}/gnibbles/gnibbles-oc.omf
%lang(sv) %{_omf_dest_dir}/gnibbles/gnibbles-sv.omf
%{_pixmapsdir}/gnibbles
%{_iconsdir}/hicolor/*/*/gnome-gnibbles.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnibbles.*

%files gnobots2 -f gnobots2.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnobots2
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%{_datadir}/gnobots2
%{_desktopdir}/gnobots2.desktop
%dir %{_omf_dest_dir}/gnobots2
%{_omf_dest_dir}/gnobots2/gnobots2-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gnobots2-da.omf
%lang(es) %{_omf_dest_dir}/gnobots2/gnobots2-es.omf
%lang(fr) %{_omf_dest_dir}/gnobots2/gnobots2-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnobots2-it.omf
%lang(oc) %{_omf_dest_dir}/gnobots2/gnobots2-oc.omf
%lang(sv) %{_omf_dest_dir}/gnobots2/gnobots2-sv.omf
%{_pixmapsdir}/gnobots2
%{_iconsdir}/hicolor/*/*/gnome-robots.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnobots2.*

%files gnometris -f gnometris.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnometris
%{_sysconfdir}/gconf/schemas/gnometris.schemas
%{_desktopdir}/gnometris.desktop
%dir %{_omf_dest_dir}/gnometris
%{_omf_dest_dir}/gnometris/gnometris-C.omf
%lang(el) %{_omf_dest_dir}/gnometris/gnometris-el.omf
%lang(es) %{_omf_dest_dir}/gnometris/gnometris-es.omf
%lang(fr) %{_omf_dest_dir}/gnometris/gnometris-fr.omf
%lang(oc) %{_omf_dest_dir}/gnometris/gnometris-oc.omf
%lang(sv) %{_omf_dest_dir}/gnometris/gnometris-sv.omf
%{_pixmapsdir}/gnometris
%{_iconsdir}/hicolor/*/*/gnome-gnometris.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnometris.*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_desktopdir}/gnomine.desktop
%dir %{_omf_dest_dir}/gnomine
%{_omf_dest_dir}/gnomine/gnomine-C.omf
%lang(es) %{_omf_dest_dir}/gnomine/gnomine-es.omf
%lang(fr) %{_omf_dest_dir}/gnomine/gnomine-fr.omf
%lang(oc) %{_omf_dest_dir}/gnomine/gnomine-oc.omf
%lang(sv) %{_omf_dest_dir}/gnomine/gnomine-sv.omf
%{_pixmapsdir}/gnomine
%{_iconsdir}/hicolor/*/*/gnome-mines.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnomine.*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_desktopdir}/gnotravex.desktop
%dir %{_omf_dest_dir}/gnotravex
%{_omf_dest_dir}/gnotravex/gnotravex-C.omf
%lang(el) %{_omf_dest_dir}/gnotravex/gnotravex-el.omf
%lang(es) %{_omf_dest_dir}/gnotravex/gnotravex-es.omf
%lang(fr) %{_omf_dest_dir}/gnotravex/gnotravex-fr.omf
%lang(oc) %{_omf_dest_dir}/gnotravex/gnotravex-oc.omf
%lang(sv) %{_omf_dest_dir}/gnotravex/gnotravex-sv.omf
%{_pixmapsdir}/gnotravex
%{_iconsdir}/hicolor/*/*/gnome-tetravex.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotravex.*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_desktopdir}/gnotski.desktop
%dir %{_omf_dest_dir}/gnotski
%{_omf_dest_dir}/gnotski/gnotski-C.omf
%lang(es) %{_omf_dest_dir}/gnotski/gnotski-es.omf
%lang(fr) %{_omf_dest_dir}/gnotski/gnotski-fr.omf
%lang(oc) %{_omf_dest_dir}/gnotski/gnotski-oc.omf
%lang(sv) %{_omf_dest_dir}/gnotski/gnotski-sv.omf
%dir %{_datadir}/%{name}/gnotski
%{_datadir}/%{name}/gnotski/gnotski.svg
%{_iconsdir}/hicolor/*/*/gnome-klotski.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotski.*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_desktopdir}/gtali.desktop
%dir %{_omf_dest_dir}/gtali
%{_omf_dest_dir}/gtali/gtali-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gtali-da.omf
%lang(es) %{_omf_dest_dir}/gtali/gtali-es.omf
%lang(fr) %{_omf_dest_dir}/gtali/gtali-fr.omf
%lang(oc) %{_omf_dest_dir}/gtali/gtali-oc.omf
%lang(sv) %{_omf_dest_dir}/gtali/gtali-sv.omf
%{_pixmapsdir}/gtali
%{_iconsdir}/hicolor/*/*/gnome-tali.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gtali.*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_desktopdir}/iagno.desktop
%dir %{_omf_dest_dir}/iagno
%{_omf_dest_dir}/iagno/iagno-C.omf
%lang(es) %{_omf_dest_dir}/iagno/iagno-es.omf
%lang(fr) %{_omf_dest_dir}/iagno/iagno-fr.omf
%lang(oc) %{_omf_dest_dir}/iagno/iagno-oc.omf
%lang(sv) %{_omf_dest_dir}/iagno/iagno-sv.omf
%{_iconsdir}/hicolor/*/*/gnome-iagno.*
%{_pixmapsdir}/iagno

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_desktopdir}/mahjongg.desktop
%dir %{_omf_dest_dir}/mahjongg
%{_omf_dest_dir}/mahjongg/mahjongg-C.omf
%lang(es) %{_omf_dest_dir}/mahjongg/mahjongg-es.omf
%lang(fr) %{_omf_dest_dir}/mahjongg/mahjongg-fr.omf
%lang(oc) %{_omf_dest_dir}/mahjongg/mahjongg-oc.omf
%lang(sv) %{_omf_dest_dir}/mahjongg/mahjongg-sv.omf
%{_pixmapsdir}/mahjongg
%{_iconsdir}/hicolor/*/*/gnome-mahjongg.png
%{_datadir}/%{name}/mahjongg
%attr(664,root,games) %ghost %{_localstatedir}/games/mahjongg.*

%files same-gnome -f same-gnome.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/same-gnome
%{_sysconfdir}/gconf/schemas/same-gnome.schemas
%{_desktopdir}/same-gnome.desktop
%{_datadir}/%{name}/same-gnome
%{_iconsdir}/hicolor/*/*/gnome-samegnome.*
%dir %{_omf_dest_dir}/same-gnome
%{_omf_dest_dir}/same-gnome/same-gnome-C.omf
%lang(en_GB) %{_omf_dest_dir}/same-gnome/same-gnome-en_GB.omf
%lang(es) %{_omf_dest_dir}/same-gnome/same-gnome-es.omf
%lang(fr) %{_omf_dest_dir}/same-gnome/same-gnome-fr.omf
%lang(oc) %{_omf_dest_dir}/same-gnome/same-gnome-oc.omf
%lang(ru) %{_omf_dest_dir}/same-gnome/same-gnome-ru.omf
%lang(sv) %{_omf_dest_dir}/same-gnome/same-gnome-sv.omf
%attr(664,root,games) %ghost %{_localstatedir}/games/same-gnome.*

%files sol -f aisleriot.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/sol
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/%{name}/aisleriot
%{_desktopdir}/freecell.desktop
%{_desktopdir}/sol.desktop
%dir %{_omf_dest_dir}/aisleriot
%{_omf_dest_dir}/aisleriot/aisleriot-C.omf
%lang(es) %{_omf_dest_dir}/aisleriot/aisleriot-es.omf
%lang(fr) %{_omf_dest_dir}/aisleriot/aisleriot-fr.omf
%lang(oc) %{_omf_dest_dir}/aisleriot/aisleriot-oc.omf
%lang(sv) %{_omf_dest_dir}/aisleriot/aisleriot-sv.omf
%{_iconsdir}/hicolor/*/*/gnome-aisleriot.*
%{_iconsdir}/hicolor/*/*/gnome-freecell.*

%files sudoku -f gnome-sudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_datadir}/gnome-sudoku
%dir %{_omf_dest_dir}/gnome-sudoku
%{_omf_dest_dir}/gnome-sudoku/gnome-sudoku-C.omf
%lang(es) %{_omf_dest_dir}/gnome-sudoku/gnome-sudoku-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-sudoku/gnome-sudoku-fr.omf
%lang(oc) %{_omf_dest_dir}/gnome-sudoku/gnome-sudoku-oc.omf
%lang(sv) %{_omf_dest_dir}/gnome-sudoku/gnome-sudoku-sv.omf
%{_pixmapsdir}/gnome-sudoku
%{_iconsdir}/hicolor/*/*/gnome-sudoku.*
