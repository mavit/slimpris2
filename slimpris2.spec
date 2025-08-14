Name:                   slimpris2
Version:                3.3.1
Release:                %{autorelease}
Summary:                MPRIS remote control of Lyrion Music Server

License:                GPL-3.0-only
URL:                    https://github.com/mavit/slimpris2
Source0:                %{url}/archive/refs/tags/%{version}.tar.gz#slimpris2-%{version}.tar.gz

BuildArch:              noarch
BuildRequires:          autoconf
BuildRequires:          automake
BuildRequires:          desktop-file-utils
BuildRequires:          intltool
BuildRequires:          libappstream-glib
BuildRequires:          make
BuildRequires:          pandoc
BuildRequires:          python3-devel
BuildRequires:          systemd
BuildRequires:          systemd-rpm-macros

Requires:               glib2
Requires:               hicolor-icon-theme
Requires:               libsoup3
Requires:               python3dist(dbus-python)
Requires:               python3dist(pygobject)
Requires:               python3dist(pyxdg)
Requires:               python3dist(simplejson)
Requires:               python3dist(six)

%description
slimpris2 provide MPRIS 2 remote control support for Lyrion Music
Server, allowing it to be controlled using the user interface integrated
into your desktop.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install
rm %{buildroot}/%{_docdir}/%{name}/COPYING
install -m 0644 -p -D %{buildroot}/%{_docdir}/%{name}/%{name}.conf \
                      %{buildroot}/%{_sysconfdir}/%{name}.conf


%check
make test


%post
%systemd_user_post %{name}.service


%preun
%systemd_user_preun %{name}.service


%postun
%systemd_user_postun_with_restart %{name}.service
%systemd_user_postun_with_reload %{name}.service
%systemd_user_postun %{name}.service


%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%doc %{_mandir}/*/*
%doc AUTHORS
%doc README.md
%doc src/%{name}.conf
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/io.github.mavit.slimpris2.desktop
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.slimpris2.service
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_iconsdir}/hicolor/22x22/apps/io.github.mavit.slimpris2.png
%{_iconsdir}/hicolor/512x512/apps/io.github.mavit.slimpris2.png
%{_iconsdir}/hicolor/scalable/apps/io.github.mavit.slimpris2.svg
%{_iconsdir}/hicolor/symbolic/apps/io.github.mavit.slimpris2-symbolic.svg
%{_metainfodir}/io.github.mavit.slimpris2.metainfo.xml
%{_userpresetdir}/80-%{name}.preset
%{_userunitdir}/%{name}.service


%changelog
%autochangelog
