Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	���� ��� GNOME
Summary(uk):	���� Ц� GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.6.2
Release:	3
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	3b43e035912ec7e941568b571f1237ae
Patch0:		%{name}-schemas.patch
Patch1:		%{name}-locale-names.patch
Icon:		gnome-games.gif
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gnome-vfs2-devel >= 2.6.1.1
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnome-devel >= 2.6.1.1
BuildRequires:	libgnomeui-devel >= 2.6.1.1
BuildRequires:	libltdl-devel
BuildRequires:	librsvg >= 1:2.6.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	scrollkeeper >= 0.3.8
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires(post):	coreutils
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.6.1.1
Requires:	librsvg >= 1:2.6.5
Obsoletes:	gnect
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var
%define		_gamesdir	%{_localstatedir}/games

%description
GNOME games.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%description -l uk
����� gnome-games ������� ���� ��� ���������� �������� ����� GNOME,
����� ���� GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome �� sol.

%description -l ru
����� gnome-games �������� ���� ��� ����� �������� ����� GNOME, �����
������� GnomeScott, freecell, gnibbles, gnobots, gnobots2,
gnome-stones, gnomine, gnotravex, gtali, gturing, iagno, mahjongg,
same-gnome � sol.

%package devel
Summary:	GNOME games libraries - header files
Summary(pl):	Pliki nag��wkowe do tworzenia program�w opartych o GNOME games
Summary(ru):	����� ���������� ��� ��� GNOME
Summary(uk):	����� �������� ��� Ц� GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.3

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description devel -l pl
Pliki nag��wkowe do tworzenia program�w opartych o GNOME games.

%description devel -l uk
����� gnome-games-devel ���������� �����, ����Ȧ�Φ ��� �������� ����
Ц� GNOME.

%description devel -l ru
����� gnome-games-devel ������������� �����, ����������� ���
���������� ��� ��� GNOME.

%package static
Summary:	GNOME games static libraries
Summary(pl):	Biblioteki statyczne do GNOME games
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNOME games static libraries.

%description static -l pl
Biblioteki statyczne do GNOME games.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

for i in glines.scores gnibbles.1.0.scores gnibbles.1.1.scores \
	gnibbles.2.0.scores gnibbles.2.1.scores gnibbles.3.0.scores \
	gnibbles.3.1.scores gnibbles.4.0.scores gnibbles.4.1.scores \
	gnobots2.classic_robots-safe.scores \
	gnobots2.classic_robots-super-safe.scores \
	gnobots2.classic_robots.scores gnobots2.nightmare-safe.scores \
	gnobots2.nightmare-super-safe.scores gnobots2.nightmare.scores \
	gnobots2.robots2-safe.scores gnobots2.robots2-super-safe.scores \
	gnobots2.robots2.scores gnobots2.robots2_easy-safe.scores \
	gnobots2.robots2_easy-super-safe.scores gnobots2.robots2_easy.scores \
	gnobots2.robots_with_safe_teleport-safe.scores \
	gnobots2.robots_with_safe_teleport-super-safe.scores \
	gnobots2.robots_with_safe_teleport.scores gnome-stones.scores \
	gnometris.scores gnomine.Custom.scores gnomine.Large.scores \
	gnomine.Medium.scores gnomine.Small.scores gnotravex.2x2.scores \
	gnotravex.3x3.scores gnotravex.4x4.scores gnotravex.5x5.scores \
	gnotravex.6x6.scores gnotski.1.scores gnotski.11.scores \
	gnotski.12.scores gnotski.13.scores gnotski.14.scores \
	gnotski.15.scores gnotski.16.scores gnotski.17.scores gnotski.2.scores \
	gnotski.21.scores gnotski.22.scores gnotski.23.scores \
	gnotski.24.scores gnotski.25.scores gnotski.26.scores gnotski.3.scores \
	gnotski.4.scores gnotski.5.scores gnotski.6.scores gnotski.7.scores \
	gtali.scores mahjongg.bridges.scores mahjongg.cloud.scores \
	mahjongg.confounding.scores mahjongg.difficult.scores \
	mahjongg.dragon.scores mahjongg.easy.scores mahjongg.pyramid.scores \
	mahjongg.tictactoe.scores same-gnome.scores; do
	if [ ! -f %{_gamesdir}/$i.scores ]; then
		touch %{_gamesdir}/$i.scores
		chown root:games %{_gamesdir}/$i.scores
		chmod 664 %{_gamesdir}/$i.scores
	fi
done

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
%attr(755,root,root) %{_bindir}/blackjack
%attr(2755,root,games) %{_bindir}/glines
%attr(2755,root,games) %{_bindir}/gnibbles
%attr(2755,root,games) %{_bindir}/gnobots2
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
%attr(664,root,games) %ghost %{_gamesdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-stones/objects/lib*.a
