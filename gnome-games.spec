Summary:	GNOME games
Summary(pl):	GNOME - Gry
Name:		gnome-games
Version:	1.0.2
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Patch:		gnome-games-DESTDIR.patch
Icon:		gnome-games.gif
Requires:	gnome-libs >= 1.0.0, ORBit >= 0.4.3, libaudiofile >= 0.1.5
Requires:	glib >= 1.2.0, gtk+ >= 1.2.0, guile >= 1.3, esound >= 0.2.7
BuildRequires:	gnome-libs-devel
URL:		http://www.gnome.org
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
GNOME games.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%package devel
Summary:	GNOME games libraries - header files
Summary(pl):	Pliki nag³ówkowedo tworzenia programów opartych o GNOME games
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description -l pl devel
Pliki nag³ówkowedo tworzenia programów opartych o GNOME games.

%package static
Summary:	GNOME games static libraries
Summary(pl):	Biblioteki statyczne do GNOME games
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static
Biblioteki statyczne do GNOME games

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--localstatedir=/var

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT \
	localstatedir=$RPM_BUILD_ROOT/var

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*so.*.*}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz
%config /etc/X11/GNOME/sound/events/*

%attr(755,root,  root) /usr/X11R6/bin/GnomeScott
%attr(755,root,  root) /usr/X11R6/bin/ctali
%attr(755,root,  root) /usr/X11R6/bin/freecell
%attr(2755, games, games) /usr/X11R6/bin/gnibbles
%attr(2755, games, games) /usr/X11R6/bin/gnobots
%attr(2755, games, games) /usr/X11R6/bin/gnobots2
%attr(2755, games, games) /usr/X11R6/bin/gnome-stones
%attr(2755, games, games) /usr/X11R6/bin/gnomine
%attr(2755, games, games) /usr/X11R6/bin/gnometris
%attr(2755, games, games) /usr/X11R6/bin/iagno
%attr(2755, games, games) /usr/X11R6/bin/gnotravex
%attr(2755, games, games) /usr/X11R6/bin/gturing
%attr(2755, games, games) /usr/X11R6/bin/gtali
%attr(2755, games, games) /usr/X11R6/bin/mahjongg
%attr(2755, games, games) /usr/X11R6/bin/metatris
%attr(2755, games, games) /usr/X11R6/bin/same-gnome

%attr(755,root,  root) /usr/X11R6/lib/lib*.so.*.*
%attr(755,root,  root) /usr/X11R6/lib/gnome-stones/objects/lib*.so.*.*

/usr/X11R6/share/gnibbles/*
/usr/X11R6/share/gnobots2/*
/usr/X11R6/share/gnome-stones/*
/usr/X11R6/share/gturing/*
/usr/X11R6/share/metatris/*
/usr/X11R6/share/mime-info/*
/usr/X11R6/share/pixmaps/*
/usr/X11R6/share/sounds/*
/usr/X11R6/share/gnome/apps/Games/*
/usr/X11R6/share/gnome/help/*
/usr/X11R6/share/gnome-stonesrc*

%attr(664, games, games) /var/games/*

%files devel
%defattr(644,root,root,755)
%attr(0755,root,  root) /usr/X11R6/lib/lib*.so
%attr(0755,root,  root) /usr/X11R6/lib/gnome-stones/objects/lib*.so
/usr/X11R6/include/*

%files static
%attr(664,root,root) /usr/X11R6/lib/lib*.a
%attr(664,root,root) /usr/X11R6/lib/gnome-stones/objects/lib*.a
