Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	È«“Ÿ –œƒ GNOME
Summary(uk):	∂«“… –¶ƒ GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.8.0
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	28ca74bc8b3305103aaf18b7f3530191
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-desktop.patch
Icon:		gnome-games.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.7.92
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gnome-vfs2-devel >= 2.7.92
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnome-devel >= 2.7.92
BuildRequires:	libgnomeui-devel >= 2.7.92
BuildRequires:	libltdl-devel
BuildRequires:	librsvg >= 1:2.8.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	rpm-build >= 4.1-10
Requires:	gnome-vfs2 >= 2.7.92
Requires:	librsvg >= 1:2.8.1
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
Gnome-games jest kolekcj± prostych, choÊ uzaleøniaj±cych gier projektu
GNOME. S± w∂rÛd nich reprezentanci wielu popularnych gier, wliczaj±c
karciane, uk≥adanki i zrÍczno∂ciowe.

%description -l uk
¡À≈‘ gnome-games ◊ÀÃ¿ﬁ¡§ ¶«“… ƒÃ— ”≈“≈ƒœ◊…›¡ “œ¬œﬁœ«œ ”‘œÃ’ GNOME,
”≈“≈ƒ —À…» GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome ‘¡ sol.

%description -l ru
¡À≈‘ gnome-games ◊ÀÃ¿ﬁ¡≈‘ …«“Ÿ ƒÃ— ”“≈ƒŸ “¡¬œﬁ≈«œ ”‘œÃ¡ GNOME, ”“≈ƒ…
Àœ‘œ“Ÿ» GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome … sol.

%package blackjack
Summary:	GNOME's version of blackjack
Summary(pl):	Blackjack dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description blackjack
Casino card game Blackjack.

%description blackjack -l pl
Kasynowa wersja gry oczko.

%package gataxx
Summary:	GNOME Ataxx
Summary(pl):	Ataxx dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gataxx
Reversi like game.

%description gataxx -l pl
Gra podobna do Reversi.

%package glines
Summary:	Five or more game
Summary(pl):	Gra "PiÍÊ albo wiÍcej"
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description glines
Remove colored balls from the board by forming lines.

%description glines -l pl
Gra polegaj±ca na usuwaniu kolorwych kul poprzez uk≥adanie ich w
linie.

%package gnect
Summary:	Four-in-a-row game
Summary(pl):	Gra "Cztery w rzÍdzie"
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnect
Compete to make lines of the same color.

%description gnect -l pl
Gra, ktÛrej celem jest utowrzenie linii w jednym kolorze.

%package gnibbles
Summary:	GNOME Nibbles
Summary(pl):	Nibbles dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnibbles
Guide a worm around a maze.

%description gnibbles -l pl
Gra polegaj±ca na przeprowadzeniu robaka przez labirynt.

%package gnobots2
Summary:	GNOME Robots
Summary(pl):	Robots dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnobots2
Avoid the robots and make them crash into each other.

%description gnobots2 -l pl
Gra polegaj±ca na zapobieganiu zderzeniom robotÛw.

%package stones
Summary:	GNOME Stones
Summary(pl):	"Kamienie" dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description stones
Boulder Dash like game.

%description stones -l pl
Gra podobna do Boulder Dasha.

%package gnometris
Summary:	GNOME Tetris
Summary(pl):	Tetris dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnometris
Tetris like game.

%description gnometris -l pl
Gra podobna do Tetrisa.

%package gnomine
Summary:	GNOME Mines
Summary(pl):	Miny dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnomine
Clear mines from a minefield.

%description gnomine -l pl
Gra, ktÛrej celem jest rozminowanie pola minowego.

%package gnotravex
Summary:	GNOME Tetravex
Summary(pl):	Tetravex dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotravex
Puzzle game.

%description gnotravex -l pl
Uk≥adanka.

%package gnotski
Summary:	Gnome Klotski
Summary(pl):	Klotski dla GNOME
Group:		X11/Applications/Games
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnotski
Clone of the Klotski game. The objective is to move the patterned
block to the area bordered by green markers.

%description gnotski -l pl
Klon gry Klotski. Celem gry jest przesuniÍcie zaznaczonego klocka
w pole ograniczone zielonymi znacznikami.

%package gtali
Summary:	GNOME Tali
Summary(pl):	Tali dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gtali
Poker-style dice game.

%description gtali -l pl
Gra w ko∂ci w pokerowym stylu.

%package iagno
Summary:	GNOME Iagno
Summary(pl):	Iagno dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description iagno
Reversi like game.

%description iagno -l pl
Gra podobna do Reversi.

%package mahjongg
Summary:	GNOME Mahjongg
Summary(pl):	Mahjongg dla GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description mahjongg
Disassemble a pile of tiles by removing matching pairs.

%description mahjongg -l pl
Gra polegjaca na demontaøu stosu kafli poprzez usuwanie pasuj±cych
par.

%package same-gnome
Summary:	Same GNOME
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description same-gnome
Remove groups of balls to try and clear the screen.

%description same-gnome -l pl
Gra, ktÛrej celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%package sol
Summary:	AisleRiot Solitaire
Summary(pl):	Pasjans AisleRiot
Group:		X11/Applications/Games
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sol
Many different solitaire games.

%description sol -l pl
RÛøne gry karciane.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post blackjack
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun blackjack -p /usr/bin/scrollkeeper-update

%post gataxx
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun gataxx -p /usr/bin/scrollkeeper-update

%post glines
/usr/bin/scrollkeeper-update
%gconf_schema_install

if [ ! -f %{_gamesdir}/glines.scores ]; then
	touch %{_gamesdir}/glines.scores
	chown root:games %{_gamesdir}/glines.scores
	chmod 664 %{_gamesdir}/glines.scores
fi

%postun glines -p /usr/bin/scrollkeeper-update

%post gnect
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun gnect -p /usr/bin/scrollkeeper-update

%post gnibbles
/usr/bin/scrollkeeper-update
%gconf_schema_install

for i in gnibbles.1.0 gnibbles.1.1 gnibbles.2.0 gnibbles.2.1 gnibbles.3.0 \
	gnibbles.3.1 gnibbles.4.0 gnibbles.4.1; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnibbles -p /usr/bin/scrollkeeper-update

%post gnobots2
/usr/bin/scrollkeeper-update
%gconf_schema_install

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

%postun	gnobots2 -p /usr/bin/scrollkeeper-update

%post stones
/usr/bin/scrollkeeper-update
%gconf_schema_install

if [ ! -f %{_gamesdir}/gnome-stones.scores ]; then
	touch %{_gamesdir}/gnome-stones.scores
	chown root:games %{_gamesdir}/gnome-stones.scores
	chmod 664 %{_gamesdir}/gnome-stones.scores
fi

%postun stones -p /usr/bin/scrollkeeper-update

%post gnometris
/usr/bin/scrollkeeper-update
%gconf_schema_install

if [ ! -f %{_gamesdir}/gnometris.scores ]; then
	touch %{_gamesdir}/gnometris.scores
	chown root:games %{_gamesdir}/gnometris.scores
	chmod 664 %{_gamesdir}/gnometris.scores
fi

%postun gnometris -p /usr/bin/scrollkeeper-update

%post gnomine
/usr/bin/scrollkeeper-update
%gconf_schema_install

for i in gnomine.Custom gnomine.Large gnomine.Medium gnomine.Small; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnomine -p /usr/bin/scrollkeeper-update

%post gnotravex
/usr/bin/scrollkeeper-update
%gconf_schema_install

for i in gnotravex.2x2 gnotravex.3x3 gnotravex.4x4 gnotravex.5x5 \
	gnotravex.6x6; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun gnotravex -p /usr/bin/scrollkeeper-update

%post gnotski
/usr/bin/scrollkeeper-update

for i in 1 2 3 4 5 6 7 11 12 13 14 15 16 17 21 22 23 24 25 26; do
	if [ ! -f %{_gamesdir}/gnotski.$i.scores ]; then
	touch %{_gamesdir}/gnotski.$i.scores
	chown root:games %{_gamesdir}/gnotski.$i.scores
	chmod 664 %{_gamesdir}/gnotski.$i.scores
	fi
done

%postun gnotski -p /usr/bin/scrollkeeper-update

%post gtali
/usr/bin/scrollkeeper-update
%gconf_schema_install

if [ ! -f %{_gamesdir}/gtali.scores ]; then
	touch %{_gamesdir}/gtali.scores
	chown root:games %{_gamesdir}/gtali.scores
	chmod 664 %{_gamesdir}/gtali.scores
fi

%postun gtali -p /usr/bin/scrollkeeper-update

%post iagno
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun iagno -p /usr/bin/scrollkeeper-update

%post mahjongg
/usr/bin/scrollkeeper-update
%gconf_schema_install

for i in mahjongg.bridges mahjongg.cloud mahjongg.confounding \
	mahjongg.difficult mahjongg.dragon mahjongg.easy \
	mahjongg.pyramid mahjongg.tictactoe mahjongg.ziggurat; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

%postun mahjongg -p /usr/bin/scrollkeeper-update

%post same-gnome
/usr/bin/scrollkeeper-update
%gconf_schema_install

if [ ! -f %{_gamesdir}/same-gnome.scores ]; then
	touch %{_gamesdir}/same-gnome.scores
	chown root:games %{_gamesdir}/same-gnome.scores
	chmod 664 %{_gamesdir}/same-gnome.scores
fi

%postun same-gnome -p /usr/bin/scrollkeeper-update

%post sol
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun sol -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_pixmapsdir}/gnome-games-common

%files blackjack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blackjack
%{_sysconfdir}/gconf/schemas/blackjack.schemas
%{_datadir}/blackjack
%{_desktopdir}/blackjack.desktop
%{_omf_dest_dir}/%{name}/blackjack-C.omf
%{_pixmapsdir}/blackjack
%{_pixmapsdir}/gnome-blackjack.png
%dir %{_gnomehelpdir}/blackjack
%{_gnomehelpdir}/blackjack/C

%files gataxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gataxx
%{_sysconfdir}/gconf/schemas/gataxx.schemas
%{_desktopdir}/gataxx.desktop
%{_omf_dest_dir}/%{name}/gataxx-C.omf
%{_pixmapsdir}/gataxx.png
%dir %{_gnomehelpdir}/gataxx
%{_gnomehelpdir}/gataxx/C

%files glines
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/glines
%{_sysconfdir}/gconf/schemas/glines.schemas
%{_desktopdir}/glines.desktop
%{_omf_dest_dir}/%{name}/glines-C.omf
%{_pixmapsdir}/glines
%{_pixmapsdir}/glines.png
%attr(664,root,games) %ghost %{_localstatedir}/games/glines.*
%dir %{_gnomehelpdir}/glines
%{_gnomehelpdir}/glines/C

%files gnect
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/gnect
%{_sysconfdir}/gconf/schemas/gnect.schemas
%{_sysconfdir}/sound/events/gnect.soundlist
%{_datadir}/gnect
%{_desktopdir}/gnect.desktop
%{_omf_dest_dir}/%{name}/gnect-C.omf
%{_pixmapsdir}/gnect
%{_pixmapsdir}/gnect-icon.png
%dir %{_gnomehelpdir}/gnect
%{_gnomehelpdir}/gnect/C

%files gnibbles
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
%dir %{_gnomehelpdir}/gnibbles
%{_gnomehelpdir}/gnibbles/C

%files gnobots2
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
%dir %{_gnomehelpdir}/gnobots2
%{_gnomehelpdir}/gnobots2/C
%lang(da) %{_gnomehelpdir}/gnobots2/da
%lang(es) %{_gnomehelpdir}/gnobots2/es
%lang(it) %{_gnomehelpdir}/gnobots2/it

%files stones
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
%{_libdir}/gnome-stones/objects/lib*.la
%{_desktopdir}/gnome-stones.desktop
%{_omf_dest_dir}/%{name}/gnome-stones-C.omf
%{_pixmapsdir}/gnome-stones
%{_pixmapsdir}/gnome-stones*.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnome-stones.*
%dir %{_gnomehelpdir}/gnome-stones
%{_gnomehelpdir}/gnome-stones/C

%files gnometris
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnometris
%{_sysconfdir}/gconf/schemas/gnometris.schemas
%{_desktopdir}/gnometris.desktop
%{_omf_dest_dir}/%{name}/gnometris-C.omf
%{_pixmapsdir}/gnometris
%{_pixmapsdir}/gnome-gtetris.png
%{_datadir}/sounds/gnometris
%attr(664,root,games) %ghost %{_localstatedir}/games/gnometris.*
%dir %{_gnomehelpdir}/gnometris
%{_gnomehelpdir}/gnometris/C

%files gnomine
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnomine
%{_sysconfdir}/gconf/schemas/gnomine.schemas
%{_desktopdir}/gnomine.desktop
%{_omf_dest_dir}/%{name}/gnomine-C.omf
%{_pixmapsdir}/gnomine
%{_pixmapsdir}/gnome-gnomine.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnomine.*
%dir %{_gnomehelpdir}/gnomine
%{_gnomehelpdir}/gnomine/C

%files gnotravex
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotravex
%{_sysconfdir}/gconf/schemas/gnotravex.schemas
%{_desktopdir}/gnotravex.desktop
%{_omf_dest_dir}/%{name}/gnotravex-C.omf
%{_pixmapsdir}/gnome-gnotravex.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotravex.*
%dir %{_gnomehelpdir}/gnotravex
%{_gnomehelpdir}/gnotravex/C

%files gnotski
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gnotski
%{_desktopdir}/gnotski.desktop
%{_omf_dest_dir}/%{name}/gnotski-C.omf
%{_pixmapsdir}/gnotski*.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gnotski.*
%dir %{_gnomehelpdir}/gnotski
%{_gnomehelpdir}/gnotski/C

%files gtali
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/gtali
%{_sysconfdir}/gconf/schemas/gtali.schemas
%{_desktopdir}/gtali.desktop
%{_omf_dest_dir}/%{name}/gtali-C.omf
%lang(da) %{_omf_dest_dir}/%{name}/gtali-da.omf
%{_pixmapsdir}/gtali
%{_pixmapsdir}/gnome-gtali.png
%attr(664,root,games) %ghost %{_localstatedir}/games/gtali.*
%dir %{_gnomehelpdir}/gtali
%{_gnomehelpdir}/gtali/C
%lang(da) %{_gnomehelpdir}/gtali/da

%files iagno
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iagno
%{_sysconfdir}/gconf/schemas/iagno.schemas
%{_sysconfdir}/sound/events/iagno.soundlist
%{_datadir}/sounds/iagno
%{_desktopdir}/iagno.desktop
%{_omf_dest_dir}/%{name}/iagno-C.omf
%{_pixmapsdir}/iagno
%{_pixmapsdir}/iagno.png
%dir %{_gnomehelpdir}/iagno
%{_gnomehelpdir}/iagno/C

%files mahjongg
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/mahjongg
%{_sysconfdir}/gconf/schemas/mahjongg.schemas
%{_desktopdir}/mahjongg.desktop
%{_omf_dest_dir}/%{name}/mahjongg-C.omf
%{_pixmapsdir}/mahjongg
%{_pixmapsdir}/gnome-mahjongg.png
%attr(664,root,games) %ghost %{_localstatedir}/games/mahjongg.*
%dir %{_gnomehelpdir}/mahjongg
%{_gnomehelpdir}/mahjongg/C

%files same-gnome
%defattr(644,root,root,755)
%attr(2755,root,games) %{_bindir}/same-gnome
%{_sysconfdir}/gconf/schemas/same-gnome.schemas
%{_desktopdir}/same-gnome.desktop
%{_omf_dest_dir}/%{name}/same-gnome-C.omf
%{_pixmapsdir}/same-gnome
%{_pixmapsdir}/gnome-gsame.png
%attr(664,root,games) %ghost %{_localstatedir}/games/same-gnome.*
%dir %{_gnomehelpdir}/same-gnome
%{_gnomehelpdir}/same-gnome/C

%files sol
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/sol
%{_sysconfdir}/gconf/schemas/aisleriot.schemas
%{_datadir}/sol-games
%{_desktopdir}/freecell.desktop
%{_desktopdir}/sol.desktop
%{_omf_dest_dir}/%{name}/aisleriot-C.omf
%{_pixmapsdir}/cards
%{_pixmapsdir}/gnome-cardgame.png
%{_pixmapsdir}/gnome-aisleriot.png
%dir %{_gnomehelpdir}/aisleriot
%{_gnomehelpdir}/aisleriot/C
