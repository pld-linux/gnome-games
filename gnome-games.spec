Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	���� ��� GNOME
Summary(uk):	���� Ц� GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.6.2
Release:	4
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

for i in glines gnibbles.1.0 gnibbles.1.1 gnibbles.2.0 gnibbles.2.1 \
	gnibbles.3.0 gnibbles.3.1 gnibbles.4.0 gnibbles.4.1 \
	gnobots2.classic_robots-safe gnobots2.classic_robots-super-safe \
	gnobots2.classic_robots gnobots2.nightmare-safe \
	gnobots2.nightmare-super-safe gnobots2.nightmare \
	gnobots2.robots2-safe gnobots2.robots2-super-safe \
	gnobots2.robots2 gnobots2.robots2_easy-safe \
	gnobots2.robots2_easy-super-safe gnobots2.robots2_easy \
	gnobots2.robots_with_safe_teleport-safe \
	gnobots2.robots_with_safe_teleport-super-safe \
	gnobots2.robots_with_safe_teleport gnome-stones gnometris \
	gnomine.Custom gnomine.Large gnomine.Medium gnomine.Small \
	gnotravex.2x2 gnotravex.3x3 gnotravex.4x4 gnotravex.5x5 \
	gnotravex.6x6 gnotski.1 gnotski.11 gnotski.12 gnotski.13 gnotski.14 \
	gnotski.15 gnotski.16 gnotski.17 gnotski.2 gnotski.21 gnotski.22 \
	gnotski.23 gnotski.24 gnotski.25 gnotski.26 gnotski.3 gnotski.4 \
	gnotski.5 gnotski.6 gnotski.7 gtali mahjongg.bridges mahjongg.cloud \
	mahjongg.confounding mahjongg.difficult mahjongg.dragon mahjongg.easy \
	mahjongg.pyramid mahjongg.tictactoe same-gnome; do
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
