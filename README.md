# `slimpris2`

`slimpris2` provides [MPRIS 2](https://specifications.freedesktop.org/mpris-spec/latest/) remote control of [Logitech Media Server](http://wiki.slimdevices.com/index.php/Logitech_Media_Server), allowing it to be controlled using the user interface integrated into your Linux desktop.

`slimpris2` is run in the user session and monitors a local or distant `squeezeboxserver`.

## Installation

### Fedora

```sh
dnf copr enable mavit/slimpris2
dnf install slimpris2
```

### From source

```sh
git clone https://github.com/mavit/slimpris2.git
cd slimpris2
./autogen.sh
./configure --sysconfdir=/etc
make
sudo make install
```

Logout/login from your session.  Default prefix is `/usr/local`.

## Configuration

By default, `slimpris2` will try to connect to LMS at `localhost:9000`.

To set a different host or port, copy the example configuration file `/usr/[local]/share/doc/slimpris2/slimpris2.conf` to `~/.config/slimpris2/slimpris2.conf`.

If you have more than one non-synced player attached to your LMS, youʼll also want to specify the name or MAC address of the particular player you want to control.

Restart your session or `slimpris2` after changing `slimpris2.conf`.

## Some examples of compatible remote controls

- Gnome Shell [time and date drop-down](https://wiki.gnome.org/Projects/GnomeShell/CheatSheet#The_top_bar)
- [GSConnect](https://github.com/GSConnect/gnome-shell-extension-gsconnect/wiki) for Android phones.
- [`playerctl`](https://github.com/altdesktop/playerctl) from the command line.
