Summary:     GNOME games
Name:        gnome-games
Version:     0.27
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
Requires:    gnome-libs >= %{version}
Obsoletes:   gnome
URL:         http://www.gnome.org

%description
GNOME games.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%package devel
Summary:     GNOME games libraries - header files
Group:       X11/Libraries
Requires:    %{name} =%{version}

%description devel
GNOME games libraries - header files.

Right now this is just stuff to develop care games. I think.

%package static
Summary:     GNOME games static libraries
Group:       X11/Libraries
Requires:    %{name}-devel =%{version}

%description static
GNOME games static libraries.

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh \
			--prefix=/usr \
			--localstatedir=/var
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure \
			--prefix=/usr \
			--localstatedir=/var
fi

make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	localstatedir=$RPM_BUILD_ROOT/var

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*so.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(2755, root, games) /usr/bin/*
%attr(0755, root,  root) /usr/lib/lib*.so.*.*
/usr/share/pixmaps/*
/usr/share/sol-games
/usr/share/apps/Games/*
/usr/share/gnome/help/*
%lang(cs) /usr/share/locale/cs/LC_MESSAGES/gnome-games.mo
%lang(da) /usr/share/locale/da/LC_MESSAGES/gnome-games.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnome-games.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/gnome-games.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnome-games.mo
%lang(ga) /usr/share/locale/ga/LC_MESSAGES/gnome-games.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnome-games.mo
%lang(ja) /usr/share/locale/ja/LC_MESSAGES/gnome-games.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/gnome-games.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/gnome-games.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gnome-games.mo
%attr(664, root, games) /var/games/*

%files devel
%defattr(644, root, root, 755)

/usr/lib/lib*.so
/usr/include/*

%files static
/usr/lib/lib*.a

%changelog
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
