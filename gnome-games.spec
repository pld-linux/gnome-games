Summary:	GNOME games
Summary(es):	Juegos de GNOME
Summary(fr):	Jeux pour GNOME
Summary(pl):	GNOME - gry
Summary(ru):	���� ��� GNOME
Summary(uk):	���� Ц� GNOME
Summary(wa):	Djeus po GNOME
Name:		gnome-games
Version:	2.0.4
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.1/sources/gnome-games/%{name}-%{version}.tar.bz2
Patch0:		%{name}-makefile.patch
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	scrollkeeper
PreReq:		scrollkeeper
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnect

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2
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
Requires:	%{name} = %{version}
Requires:	gtk+-devel

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
Requires:	%{name}-devel = %{version}

%description static
GNOME games static libraries.

%description static -l pl
Biblioteki statyczne do GNOME games.

%prep
%setup -q
%patch0 -p1

%build
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
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 
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
%{_sysconfdir}/gconf/schemas/*

%attr(755,root,root) %{_bindir}/ctali
%attr(755,root,root) %{_bindir}/freecell
%attr(755,root,root) %{_bindir}/gataxx
%attr(755,root,root) %{_bindir}/sol
%attr(2755,root,games) %{_bindir}/glines
%attr(2755,root,games) %{_bindir}/gnect
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
%{_datadir}/applications/*
%{_datadir}/gnect

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
