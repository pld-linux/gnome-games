Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	Игры под GNOME
Summary(uk):	╤гри п╕д GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	1.4.0.4
Release:	3
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-games/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-scrollkeeper.patch
Patch2:		%{name}-ac_fix.patch
Patch3:		%{name}-pixbuf_cflags.patch
Patch4:		%{name}-applnk.patch
Patch5:		%{name}-fix-help-paths.patch
Patch6:		%{name}-am16.patch
Patch7:		%{name}-xbill.patch
Patch8:		%{name}-omf.patch
Icon:		gnome-games.gif
BuildRequires:	ORBit >= 0.4.3
BuildRequires:	audiofile-devel >= 0.1.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
PreReq:		scrollkeeper
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnect

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
Requires:	%{name} = %{version}
Requires:	gtk+-devel

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
Requires:	%{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static -l pl
Biblioteki statyczne do GNOME games.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
mv xbill/xbill.png xbill/gnome-xbill.png
%patch8 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config %{_sysconfdir}/sound/events/*

%attr(755,root,root) %{_bindir}/ctali
%attr(755,root,root) %{_bindir}/freecell
%attr(755,root,root) %{_bindir}/gataxx
%attr(755,root,root) %{_bindir}/sol
%attr(2755,root,games) %{_bindir}/glines
%attr(2755,root,games) %{_bindir}/gnibbles
%attr(2755,root,games) %{_bindir}/gnobots2
%attr(2755,root,games) %{_bindir}/gnome-stones
%attr(2755,root,games) %{_bindir}/gnome-xbill
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
%attr(755,root,root) %{_libdir}/gnome-stones/objects/lib*.la

%{_datadir}/gnibbles
%{_datadir}/gnobots2
%{_datadir}/gnome-stones
%{_datadir}/sol-games
%{_datadir}/xbill

%{_datadir}/gnome-stonesrc
%lang(ko) %{_datadir}/gnome-stonesrc.ko

%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/sounds/*

%{_applnkdir}/Games/*.desktop
%{_applnkdir}/Games/*/*.desktop

%{_omf_dest_dir}/%{name}
%attr(664,root,games) %ghost %{_localstatedir}/games/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnome-stones/objects/lib*.a
