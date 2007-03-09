#
# TODO:
# - system libggz (http://www.ggzgamingzone.org/)
# - pl summary and description for glchess subpackage
#
Summary:	GNOME games
Summary(es.UTF-8):	Juegos de GNOME
Summary(fr.UTF-8):	Jeux pour GNOME
Summary(pl.UTF-8):	GNOME - gry
Summary(ru.UTF-8):	Игры под GNOME
Summary(uk.UTF-8):	Ігри під GNOME
Summary(wa.UTF-8):	Djeus po GNOME
Name:		gnome-games
Version:	2.17.92
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-games/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	d36e595666b72c4644795eff5cd4420b
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-glib-devel >= 0.6.15
BuildRequires:	check >= 0.9.4
BuildRequires:	esound-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.9.2
BuildRequires:	gnome-vfs2-devel >= 2.17.91
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	guile-devel >= 5:1.6.5
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.17.92
BuildRequires:	libltdl-devel
BuildRequires:	librsvg-devel >= 1:2.16.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.4
BuildRequires:	python-gnome-desktop-devel >= 2.17.93
BuildRequires:	python-pygtk-devel >= 2:2.10.4
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.17.91
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.17.92
Requires:	librsvg >= 1:2.16.1
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
Group:		X11/Applications/Games
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	glchess

%description glchess
glChess is a 2D/3D chess game interfacing via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently
use engines such as GNUChess, Sjeng, Faile, Amy, Crafty and Phalanx.

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
Requires:	python-gnome-desktop-print >= 2.17.93
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
%patch1 -p1
%patch2 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-bonjour \
	--disable-howl \
	--disable-scrollkeeper \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

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

%post
%gconf_schema_install libgnomegames.schemas

%preun
%gconf_schema_uninstall libgnomegames.schemas

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
%scrollkeeper_update_post

%preun glchess
%gconf_schema_uninstall glchess.schemas

%postun glchess
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
%{_sysconfdir}/gconf/schemas/libgnomegames.schemas
%dir %{_datadir}/%{name}
%dir %{_omf_dest_dir}/%{name}
%{_pixmapsdir}/gnome-games-common
%dir %{_pixmapsdir}/iagno
%{_pixmapsdir}/iagno/classic.png
%dir %{_datadir}/ggz
%{_datadir}/ggz/gnome-games

%files blackjack -f blackjack.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blackjack
%{_sysconfdir}/gconf/schemas/blackjack.schemas
%{_datadir}/blackjack
%{_desktopdir}/blackjack.desktop
%{_omf_dest_dir}/%{name}/blackjack-C.omf
%{_pixmapsdir}/blackjack
%{_iconsdir}/hicolor/*/*/gnome-blackjack.png

%files glchess -f glchess.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glchess
%attr(755,root,root) %{_bindir}/gnome-gnuchess
%{_sysconfdir}/gconf/schemas/glchess.schemas
%{_desktopdir}/glchess.desktop
%{_datadir}/glchess
%{py_sitescriptdir}/glchess
%{_pixmapsdir}/glchess.svg
%{_pixmapsdir}/glchess
%dir %{_omf_dest_dir}/glchess
%{_omf_dest_dir}/glchess/glchess-C.omf

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_desktopdir}/glines.desktop
%{_pixmapsdir}/glines
%{_iconsdir}/hicolor/*/*/gnome-five-or-more.png
%dir %{_omf_dest_dir}/glines
%{_omf_dest_dir}/glines/glines-C.omf
%lang(sv) %{_omf_dest_dir}/glines/glines-sv.omf
%attr(664,root,games) %ghost %{_localstatedir}/games/glines.*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_datadir}/gnect
%{_desktopdir}/gnect.desktop
%{_pixmapsdir}/gnect
%{_iconsdir}/hicolor/*/*/gnome-four-in-a-row.png
%dir %{_omf_dest_dir}/gnect
%{_omf_dest_dir}/gnect/gnect-C.omf
%lang(sv) %{_omf_dest_dir}/gnect/gnect-sv.omf

%files gnibbles -f gnibbles.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnibbles
%{_sysconfdir}/gconf/schemas/gnibbles.schemas
%{_sysconfdir}/sound/events/gnibbles.soundlist
%{_datadir}/gnibbles
%{_datadir}/sounds/gnibbles
%{_desktopdir}/gnibbles.desktop
%{_omf_dest_dir}/%{name}/gnibbles-C.omf
%{_pixmapsdir}/gnibbles
%{_iconsdir}/hicolor/*/*/gnome-nibbles.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnibbles.*

%files gnobots2 -f gnobots2.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnobots2
%{_sysconfdir}/gconf/schemas/gnobots2.schemas
%{_sysconfdir}/sound/events/gnobots2.soundlist
%{_datadir}/gnobots2
%{_datadir}/sounds/gnobots2
%{_desktopdir}/gnobots2.desktop
%{_omf_dest_dir}/%{name}/gnobots2-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gnobots2-da.omf
%lang(es) %{_omf_dest_dir}/%{name}/gnobots2-es.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnobots2-it.omf
%{_pixmapsdir}/gnobots2
%{_iconsdir}/hicolor/*/*/gnome-robots.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnobots2.*

%files gnometris -f gnometris.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnometris
%{_sysconfdir}/gconf/schemas/gnometris.schemas
%{_desktopdir}/gnometris.desktop
%{_omf_dest_dir}/%{name}/gnometris-C.omf
%{_pixmapsdir}/gnometris
%{_iconsdir}/hicolor/*/*/gnome-gnometris.png
%{_datadir}/sounds/gnometris
%attr(664,root,games) %ghost %{_localstatedir}/games/gnometris.*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_desktopdir}/gnomine.desktop
%{_omf_dest_dir}/%{name}/gnomine-C.omf
%{_pixmapsdir}/gnomine
%{_iconsdir}/hicolor/*/*/gnome-gnomine.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gnomine.*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_desktopdir}/gnotravex.desktop
%{_omf_dest_dir}/%{name}/gnotravex-C.omf
%{_pixmapsdir}/gnotravex
%{_iconsdir}/hicolor/*/*/gnome-tetravex.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotravex.*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_desktopdir}/gnotski.desktop
%{_omf_dest_dir}/%{name}/gnotski-C.omf
%{_pixmapsdir}/gnotski.svg
%{_iconsdir}/hicolor/*/*/gnome-klotski.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotski.*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_desktopdir}/gtali.desktop
%{_omf_dest_dir}/%{name}/gtali-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gtali-da.omf
%{_pixmapsdir}/gtali
%{_iconsdir}/hicolor/*/*/gnome-tali.*
%attr(664,root,games) %ghost %{_localstatedir}/games/gtali.*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_sysconfdir}/sound/events/iagno.soundlist
%{_datadir}/sounds/iagno
%{_desktopdir}/iagno.desktop
%{_omf_dest_dir}/%{name}/iagno-C.omf
%{_iconsdir}/hicolor/*/*/gnome-iagno.*
%{_pixmapsdir}/iagno/woodtrim.png

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_desktopdir}/mahjongg.desktop
%{_omf_dest_dir}/%{name}/mahjongg-C.omf
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
%{_iconsdir}/hicolor/*/*/gnome-same-gnome.png
%dir %{_omf_dest_dir}/same-gnome
%{_omf_dest_dir}/same-gnome/same-gnome-C.omf
%lang(sv) %{_omf_dest_dir}/same-gnome/same-gnome-sv.omf
%attr(664,root,games) %ghost %{_localstatedir}/games/same-gnome.*

%files sol -f aisleriot.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/sol
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/sol-games
%{_desktopdir}/freecell.desktop
%{_desktopdir}/sol.desktop
%{_omf_dest_dir}/%{name}/aisleriot-C.omf
%lang(fr) %{_omf_dest_dir}/%{name}/aisleriot-fr.omf
%{_pixmapsdir}/cards
%{_iconsdir}/hicolor/*/*/gnome-aisleriot.png
%{_iconsdir}/hicolor/*/*/gnome-freecell.png

%files sudoku -f gnome-sudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-sudoku
%{_desktopdir}/gnome-sudoku.desktop
%dir %{py_sitescriptdir}/gnome_sudoku
%{py_sitescriptdir}/gnome_sudoku/*.py[co]
%dir %{py_sitescriptdir}/gnome_sudoku/gtk_goodies
%{py_sitescriptdir}/gnome_sudoku/gtk_goodies/*.py[co]
%{_datadir}/gnome-sudoku
%{_pixmapsdir}/gnome-sudoku
%{_pixmapsdir}/sudoku.png
