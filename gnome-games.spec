Summary:	Video games for GNOME
Summary(pl.UTF-8):	Gry wideo dla GNOME
Name:		gnome-games
Version:	3.34.2
Release:	1
Epoch:		1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-games/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	f9cdbaaecab5100bb2c84f2210c07fe0
URL:		https://wiki.gnome.org/Apps/Games
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	grilo-devel >= 0.3
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	libarchive-devel
BuildRequires:	libhandy-devel >= 0.0.10
BuildRequires:	libmanette-devel >= 0.2.0
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.46.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	retro-gtk-devel >= 0.18.0
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0
BuildRequires:	vala >= 2:0.15.1
BuildRequires:	vala-grilo >= 0.3
BuildRequires:	vala-libhandy >= 0.0.10
BuildRequires:	vala-libmanette >= 0.2.0
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	vala-retro-gtk >= 0.18.0
BuildRequires:	vala-tracker >= 2.0
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.38
Requires:	glib2-devel >= 1:2.38
Requires:	hicolor-icon-theme
Requires:	libhandy >= 0.0.10
Requires:	librsvg >= 1:2.32.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games is a GNOME 3 application to browse your video games library and
to easily pick and play a game from it. It aims to do for games what
Music already does for your music library.

%description -l pl.UTF-8
GNOME Games to aplikacja GNOME 3 do przeglądania biblioteki gier wideo
i łatwego wybierania gier i grania w nie. Celem jest, aby robić z
grami to, co GNOME Music robi z biblioteką muzyczną.

%prep
%setup -q

%build
%meson build \
	-Dmame-plugin=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-games
%dir %{_libdir}/gnome-games
%dir %{_libdir}/gnome-games/plugins
%attr(755,root,root) %{_libdir}/gnome-games/plugins/libgames-*-plugin.so
%attr(755,root,root) %{_libdir}/gnome-games/plugins/*.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.Games.gschema.xml
%{_datadir}/gnome-games
%{_datadir}/metainfo/org.gnome.Games.appdata.xml
%{_desktopdir}/org.gnome.Games.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Games.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Games-symbolic.svg
