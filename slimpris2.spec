Name:                   slimpris2
Version:                1.0.1
Release:                0.1%{?dist}
Summary:                MPRIS remote control of Logitech Media Server

License:                GPLv3
URL:                    https://github.com/mavit/slimpris2/
Source0:                https://github.com/mavit/slimpris2/archive/master.tar.gz#slimpris2-master.tar.gz

BuildArch:              noarch
BuildRequires:          autoconf
BuildRequires:          automake
BuildRequires:          intltool
BuildRequires:          python3-devel
BuildRequires:          systemd
BuildRequires:          systemd-rpm-macros


%description
slimpris2 provide MPRIS 2 remote control support for Logitech Media
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


%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%doc AUTHORS
%doc README.md
%doc src/%{name}.conf
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.mpris.MediaPlayer2.squeezebox.desktop
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.squeezebox.service
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_userpresetdir}/80-%{name}.preset
%{_userunitdir}/%{name}.service


%changelog
