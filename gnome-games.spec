Summary:     GNOME games
Summary(pl): GNOME - Gry
Name:        gnome-games
Version:     0.27
Release:     3
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Icon:        foot.gif
Requires:    gnome-libs >= %{version}
URL:         http://www.gnome.org
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

%description
GNOME games.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Gry pod GNOME.

%package devel
Summary:     GNOME games libraries - header files
Summary(pl): Pliki nag³ówkowedo tworzenia programów opartych o GNOME games
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%description -l pl devel
Pliki nag³ówkowedo tworzenia programów opartych o GNOME games.

%package static
Summary:     GNOME games static libraries
Summary(pl): Biblioteki statyczne do GNOME games
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static
Biblioteki statyczne do GNOME games

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh \
			--prefix=/usr/X11R6 \
			--localstatedir=/var
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure \
			--prefix=/usr/X11R6 \
			--localstatedir=/var
fi

make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	localstatedir=$RPM_BUILD_ROOT/var

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*so.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(2755, root, games) /usr/X11R6/bin/*
%attr(0755, root,  root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/pixmaps/*
/usr/X11R6/share/sol-games
/usr/X11R6/share/apps/Games/*
/usr/X11R6/share/gnome/help/*
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/gnome-games.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/gnome-games.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-games.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-games.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-games.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-games.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-games.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-games.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-games.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-games.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-games.mo
%attr(664, root, games) /var/games/*

%files devel
%defattr(644, root, root, 755)

/usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%attr(664, root, root) /usr/X11R6/lib/lib*.a

%changelog
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
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added %post{un} with runing /sbin/ldconfig,
- added "Requires: gnome-libs >= %%{version}" to main package,
- added striping shared libraries.

* Mon Mar 16 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-games CVS source tree
