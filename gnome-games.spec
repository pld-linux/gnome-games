Summary:	GNOME games
Summary(pl):	GNOME - Gry
Name:		gnome-games
Version:	1.0.2
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Icon:		gnome-games.gif
Requires:	gnome-libs >= 1.0.0, ORBit >= 0.4.3, libaudiofile >= 0.1.5
Requires:	glib >= 1.2.0, gtk+ >= 1.2.0, guile >= 1.3, esound >= 0.2.7
BuildPrereq:	gnome-libs-devel
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

%build
autoconf
gettextize --copy --force
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--localstatedir=/var

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT \
	localstatedir=$RPM_BUILD_ROOT/var \
	same_gnome_helpdir=$RPM_BUILD_ROOT/usr/X11R6/share/gnome/help/samegnome/C

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*so.*.*}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gnome-games.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz
%config /etc/X11/GNOME/sound/events/*

%attr(755,root,  root) /usr/X11R6/bin/GnomeScott
%attr(755,root,  root) /usr/X11R6/bin/cyahtzee
%attr(755,root,  root) /usr/X11R6/bin/freecell
%attr(755,root,  root) /usr/X11R6/bin/sol
%attr(2755, games, games) /usr/X11R6/bin/gnobots
%attr(2755, games, games) /usr/X11R6/bin/gnome-stones
%attr(2755, games, games) /usr/X11R6/bin/gnomine
%attr(2755, games, games) /usr/X11R6/bin/gnothello
%attr(2755, games, games) /usr/X11R6/bin/gnotravex
%attr(2755, games, games) /usr/X11R6/bin/gturing
%attr(2755, games, games) /usr/X11R6/bin/gyahtzee
%attr(2755, games, games) /usr/X11R6/bin/mahjongg
%attr(2755, games, games) /usr/X11R6/bin/same-gnome

%attr(755,root,  root) /usr/X11R6/lib/lib*.so.*.*

/usr/X11R6/share/pixmaps/*
/usr/X11R6/share/sol-games
/usr/X11R6/share/apps/Games/*
/usr/X11R6/share/gnome/help/*

%attr(664, games, games) /var/games/*

%files devel
%defattr(644,root,root,755)
%attr(0755,root,  root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%attr(664,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Wed Jun  9 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [1.0.2-1]
- added find_lang macro

* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.1-1]
- added LDFLAGS="-s" to ./configure enviroment,
- added more Requires,
- changed permission to %attr(2755, games, games) on some
  executables and to %attr(664, games, games) on game score
  files (/var/games/*),
- more locales (fi, pl).

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-3]
- added package Icon,
- changed prefix to /usr/X11R6.

* Mon Aug 31 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.27-2]
- added pl translation.

* Mon Aug 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.27-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added %post{un} with runing /sbin/ldconfig,
- added "Requires: gnome-libs >= %%{version}" to main package,
- added stripping shared libraries.

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-games CVS source tree
