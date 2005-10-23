Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	éÇÒÙ ÐÏÄ GNOME
Summary(uk):	¶ÇÒÉ Ð¦Ä GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.12.1
Release:	2
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-games/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	b4870504aa1a5a759c89a2b92f1a2c21
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-desktop.patch
Icon:		gnome-games.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.12.0
BuildRequires:	gob2 >= 2.0.0
BuildRequires:	guile-devel >= 5:1.6.5
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	howl-devel >= 0.9.10
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libltdl-devel
BuildRequires:	librsvg-devel >= 1:2.9.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.8
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.12.0
Requires:	librsvg >= 1:2.9.5
Obsoletes:	gnect
Obsoletes:	gnome
Obsoletes:	gnome-games-devel
Obsoletes:	gnome-games-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var
%define		_gnomehelpdir	%{_datadir}/gnome/help
%define		_gamesdir	%{_localstatedir}/games

%description
Gnome-games is a collection of simple, but addictive, games from the
GNOME desktop project. They represent many of the popular games and
include card games, puzzle games and arcade games.

%description -l pl
Gnome-games jest kolekcj± prostych, choæ uzale¿niaj±cych gier projektu
GNOME. S± w¶ród nich reprezentanci wielu popularnych gier, wliczaj±c
karciane, uk³adanki i zrêczno¶ciowe.

%description -l uk
ðÁËÅÔ gnome-games ×ËÌÀÞÁ¤ ¦ÇÒÉ ÄÌÑ ÓÅÒÅÄÏ×ÉÝÁ ÒÏÂÏÞÏÇÏ ÓÔÏÌÕ GNOME,
ÓÅÒÅÄ ÑËÉÈ GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome ÔÁ sol.

%description -l ru
ðÁËÅÔ gnome-games ×ËÌÀÞÁÅÔ ÉÇÒÙ ÄÌÑ ÓÒÅÄÙ ÒÁÂÏÞÅÇÏ ÓÔÏÌÁ GNOME, ÓÒÅÄÉ
ËÏÔÏÒÙÈ GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome É sol.

%package blackjack
Summary:	GNOME's version of blackjack
Summary(pl):	Blackjack dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description blackjack
Casino card game Blackjack.

%description blackjack -l pl
Kasynowa wersja gry oczko.

%package gataxx
Summary:	GNOME Ataxx
Summary(pl):	Ataxx dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gataxx
Reversi like game.

%description gataxx -l pl
Gra podobna do Reversi.

%package glines
Summary:	Five or more game
Summary(pl):	Gra "Piêæ albo wiêcej"
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description glines
Remove colored balls from the board by forming lines.

%description glines -l pl
Gra polegaj±ca na usuwaniu kolorwych kul poprzez uk³adanie ich w
linie.

%package gnect
Summary:	Four-in-a-row game
Summary(pl):	Gra "Cztery w rzêdzie"
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnect
Compete to make lines of the same color.

%description gnect -l pl
Gra, której celem jest utowrzenie linii w jednym kolorze.

%package gnibbles
Summary:	GNOME Nibbles
Summary(pl):	Nibbles dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnibbles
Guide a worm around a maze.

%description gnibbles -l pl
Gra polegaj±ca na przeprowadzeniu robaka przez labirynt.

%package gnobots2
Summary:	GNOME Robots
Summary(pl):	Robots dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnobots2
Avoid the robots and make them crash into each other.

%description gnobots2 -l pl
Gra polegaj±ca na zapobieganiu zderzeniom robotów.

%package stones
Summary:	GNOME Stones
Summary(pl):	"Kamienie" dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description stones
Boulder Dash like game.

%description stones -l pl
Gra podobna do Boulder Dasha.

%package gnometris
Summary:	GNOME Tetris
Summary(pl):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnometris
Tetris like game.

%description gnometris -l pl
Gra podobna do Tetrisa.

%package gnomine
Summary:	GNOME Mines
Summary(pl):	Miny dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnomine
Clear mines from a minefield.

%description gnomine -l pl
Gra, której celem jest rozminowanie pola minowego.

%package gnotravex
Summary:	GNOME Tetravex
Summary(pl):	Tetravex dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotravex
Puzzle game.

%description gnotravex -l pl
Uk³adanka.

%package gnotski
Summary:	Gnome Klotski
Summary(pl):	Klotski dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotski
Clone of the Klotski game. The objective is to move the patterned
block to the area bordered by green markers.

%description gnotski -l pl
Klon gry Klotski. Celem gry jest przesuniêcie zaznaczonego klocka
w pole ograniczone zielonymi znacznikami.

%package gtali
Summary:	GNOME Tali
Summary(pl):	Tali dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gtali
Poker-style dice game.

%description gtali -l pl
Gra w ko¶ci w pokerowym stylu.

%package iagno
Summary:	GNOME Iagno
Summary(pl):	Iagno dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description iagno
Reversi like game.

%description iagno -l pl
Gra podobna do Reversi.

%package mahjongg
Summary:	GNOME Mahjongg
Summary(pl):	Mahjongg dla GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%description mahjongg -l pl
Gra polegjaca na demonta¿u stosu kafli poprzez usuwanie pasuj±cych
par.

%package same-gnome
Summary:	Same GNOME
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post):	coreutils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description same-gnome
Remove groups of balls to try and clear the screen.

%description same-gnome -l pl
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%package sol
Summary:	AisleRiot Solitaire
Summary(pl):	Pasjans AisleRiot
Group:		X11/Applications/Games
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	guile >= 5:1.6.5

%description sol
Many different solitaire games.

%description sol -l pl
Ró¿ne gry karciane.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-stones/objects/lib*.la

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name
%find_lang gnect --with-gnome
%find_lang gnomine --with-gnome
%find_lang same-gnome --with-gnome
%find_lang mahjongg --with-gnome
%find_lang gtali --with-gnome
%find_lang gnome-stones --with-gnome
%find_lang gataxx --with-gnome
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

%preun blackjack
%gconf_schema_uninstall blackjack.schemas

%postun blackjack
%scrollkeeper_update_postun

%post gataxx
%scrollkeeper_update_post
%gconf_schema_install gataxx.schemas

%preun gataxx
%gconf_schema_uninstall gataxx.schemas

%postun gataxx
%scrollkeeper_update_postun

%post glines
%scrollkeeper_update_post
%gconf_schema_install glines.schemas

if [ ! -f %{_gamesdir}/glines.scores ]; then
	touch %{_gamesdir}/glines.scores
	chown root:games %{_gamesdir}/glines.scores
	chmod 664 %{_gamesdir}/glines.scores
fi

%preun glines
%gconf_schema_uninstall glines.schemas

%postun glines
%scrollkeeper_update_postun

%post gnect
%scrollkeeper_update_post
%gconf_schema_install gnect.schemas

%preun gnect
%gconf_schema_uninstall gnect.schemas

%postun gnect
%scrollkeeper_update_postun

%post gnibbles
%scrollkeeper_update_post
%gconf_schema_install gnibbles.schemas

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

%post gnobots2
%scrollkeeper_update_post
%gconf_schema_install gnobots2.schemas

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

%post stones
%scrollkeeper_update_post
%gconf_schema_install gnome-stones.schemas
%update_desktop_database_post

if [ ! -f %{_gamesdir}/gnome-stones.scores ]; then
	touch %{_gamesdir}/gnome-stones.scores
	chown root:games %{_gamesdir}/gnome-stones.scores
	chmod 664 %{_gamesdir}/gnome-stones.scores
fi

%preun stones
%gconf_schema_uninstall gnome-stones.schemas

%postun stones
%scrollkeeper_update_postun
%update_desktop_database_postun

%post gnometris
%scrollkeeper_update_post
%gconf_schema_install gnometris.schemas

if [ ! -f %{_gamesdir}/gnometris.scores ]; then
	touch %{_gamesdir}/gnometris.scores
	chown root:games %{_gamesdir}/gnometris.scores
	chmod 664 %{_gamesdir}/gnometris.scores
fi

%preun gnometris
%gconf_schema_uninstall gnometris.schemas

%postun gnometris
%scrollkeeper_update_postun

%post gnomine
%scrollkeeper_update_post
%gconf_schema_install gnomine.schemas

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

%post gnotravex
%scrollkeeper_update_post
%gconf_schema_install gnotravex.schemas

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

%post gnotski
%scrollkeeper_update_post
%gconf_schema_install gnotski.schemas

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

%post gtali
%scrollkeeper_update_post
%gconf_schema_install gtali.schemas

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%preun gtali
%gconf_schema_uninstall gtali.schemas

%postun gtali
%scrollkeeper_update_postun

%post iagno
%scrollkeeper_update_post
%gconf_schema_install iagno.schemas

%preun iagno
%gconf_schema_uninstall iagno.schemas

%postun iagno
%scrollkeeper_update_postun

%post mahjongg
%scrollkeeper_update_post
%gconf_schema_install mahjongg.schemas

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

%post same-gnome
%scrollkeeper_update_post
%gconf_schema_install same-gnome.schemas

if [ ! -f %{_gamesdir}/same-gnome.scores ]; then
	touch %{_gamesdir}/same-gnome.scores
	chown root:games %{_gamesdir}/same-gnome.scores
	chmod 664 %{_gamesdir}/same-gnome.scores
fi

%preun same-gnome
%gconf_schema_uninstall same-gnome.schemas

%postun same-gnome
%scrollkeeper_update_postun

%post sol
%scrollkeeper_update_post
%gconf_schema_install aisleriot.schemas

%preun sol
%gconf_schema_uninstall aisleriot.schemas

%postun sol
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/games-server.py
%{_sysconfdir}/gconf/schemas/libgnomegames.schemas
%dir %{_datadir}/%{name}
%dir %{_omf_dest_dir}/%{name}
%{_pixmapsdir}/gnome-games-common
%dir %{_pixmapsdir}/iagno
%{_pixmapsdir}/iagno/classic.png

%files blackjack -f blackjack.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blackjack
%{_sysconfdir}/gconf/schemas/blackjack.schemas
%{_datadir}/blackjack
%{_desktopdir}/blackjack.desktop
%{_omf_dest_dir}/%{name}/blackjack-C.omf
%{_pixmapsdir}/blackjack
%{_pixmapsdir}/gnome-blackjack.png

%files gataxx -f gataxx.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gataxx
%{_sysconfdir}/gconf/schemas/gataxx.schemas
%{_desktopdir}/gataxx.desktop
%{_omf_dest_dir}/%{name}/gataxx-C.omf
%{_pixmapsdir}/gataxx.png

%files glines -f glines.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_desktopdir}/glines.desktop
%{_omf_dest_dir}/%{name}/glines-C.omf
%{_pixmapsdir}/glines
%{_pixmapsdir}/glines.png
%attr(664,root,games) %ghost %{_localstatedir}/games/glines.*

%files gnect -f gnect.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_datadir}/gnect
%{_desktopdir}/gnect.desktop
%{_omf_dest_dir}/%{name}/gnect-C.omf
%{_pixmapsdir}/gnect
%{_pixmapsdir}/gnect-icon.png

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
%{_pixmapsdir}/gnome-nibbles.png
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
%{_pixmapsdir}/gnome-gnobots2.png
%{_pixmapsdir}/rteleport.png
%{_pixmapsdir}/teleport.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnobots2.*

%files stones -f gnome-stones.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnome-stones
%{_sysconfdir}/gconf/schemas/gnome-stones.schemas
%{_datadir}/gnome-stones
%{_datadir}/mime-info/gnome-stones.*
%{_datadir}/gnome-stonesrc
%lang(ko) %{_datadir}/gnome-stonesrc.ko
%dir %{_libdir}/gnome-stones
%dir %{_libdir}/gnome-stones/objects
%attr(755,root,root) %{_libdir}/gnome-stones/objects/lib*.so
%{_desktopdir}/gnome-stones.desktop
%{_omf_dest_dir}/%{name}/gnome-stones-C.omf
%{_pixmapsdir}/gnome-stones
%{_pixmapsdir}/gnome-stones*.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnome-stones.*

%files gnometris -f gnometris.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnometris
%{_sysconfdir}/gconf/schemas/gnometris.schemas
%{_desktopdir}/gnometris.desktop
%{_omf_dest_dir}/%{name}/gnometris-C.omf
%{_pixmapsdir}/gnometris
%{_pixmapsdir}/gnome-gtetris.png
%{_datadir}/sounds/gnometris
%attr(664,root,games) %ghost %{_localstatedir}/games/gnometris.*

%files gnomine -f gnomine.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_desktopdir}/gnomine.desktop
%{_omf_dest_dir}/%{name}/gnomine-C.omf
%{_pixmapsdir}/gnomine
%{_pixmapsdir}/gnome-gnomine.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnomine.*

%files gnotravex -f gnotravex.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_desktopdir}/gnotravex.desktop
%{_omf_dest_dir}/%{name}/gnotravex-C.omf
%{_pixmapsdir}/gnome-gnotravex.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotravex.*

%files gnotski -f gnotski.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_sysconfdir}/gconf/schemas/gnotski.schemas
%{_desktopdir}/gnotski.desktop
%{_omf_dest_dir}/%{name}/gnotski-C.omf
%{_pixmapsdir}/gnotski*.png
%{_pixmapsdir}/gnotski.svg
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotski.*

%files gtali -f gtali.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_desktopdir}/gtali.desktop
%{_omf_dest_dir}/%{name}/gtali-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gtali-da.omf
%{_pixmapsdir}/gtali
%{_pixmapsdir}/gnome-gtali.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gtali.*

%files iagno -f iagno.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_sysconfdir}/sound/events/iagno.soundlist
%{_datadir}/sounds/iagno
%{_desktopdir}/iagno.desktop
%{_omf_dest_dir}/%{name}/iagno-C.omf
%{_pixmapsdir}/iagno.png
%{_pixmapsdir}/iagno/*
%exclude %{_pixmapsdir}/iagno/classic.png

%files mahjongg -f mahjongg.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_desktopdir}/mahjongg.desktop
%{_omf_dest_dir}/%{name}/mahjongg-C.omf
%{_pixmapsdir}/mahjongg
%{_pixmapsdir}/gnome-mahjongg.png
%{_datadir}/%{name}/mahjongg
%attr(664,root,games) %ghost %{_localstatedir}/games/mahjongg.*

%files same-gnome -f same-gnome.lang
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/same-gnome
%{_sysconfdir}/gconf/schemas/same-gnome.schemas
%{_desktopdir}/same-gnome.desktop
%{_omf_dest_dir}/%{name}/same-gnome-C.omf
%{_datadir}/%{name}/same-gnome
%{_pixmapsdir}/gnome-gsame.png
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
%{_pixmapsdir}/gnome-cardgame.png
%{_pixmapsdir}/gnome-aisleriot.png
