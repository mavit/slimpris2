# `slimpris2`

`slimpris2` provides [MPRIS 2](https://specifications.freedesktop.org/mpris-spec/latest/) remote control of [Lyrion Music Server](https://lyrion.org/), allowing it to be controlled using the user interface integrated into your Linux desktop.

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

Ensure that you have GLib, Gio, and Soup-3.0 installed.

Log out and back in to your session.

## Configuration

By default, `slimpris2` will auto-discover LMS on the local network.  To set a specific host or port, copy the example configuration file `/usr/[local]/share/doc/slimpris2/slimpris2.conf` to `~/.config/slimpris2/slimpris2.conf`.

If you have more than one non-synced player attached to your LMS, youʼll also want to specify the name or MAC address of the particular player you want to control.

Restart your session or `slimpris2` after changing `slimpris2.conf`.

## Some examples of compatible remote controls

- [BlueZ](http://www.bluez.org/) `mpris-proxy` for Bluetooth [AVRCP](https://en.wikipedia.org/wiki/List_of_Bluetooth_profiles#Audio/Video_Remote_Control_Profile_(AVRCP)) remote controls.
- Gnome Shell [time and date drop-down](https://wiki.gnome.org/Projects/GnomeShell/CheatSheet#The_top_bar).
- [GSConnect](https://github.com/GSConnect/gnome-shell-extension-gsconnect/wiki) for Android phones.
- [`playerctl`](https://github.com/altdesktop/playerctl) from the command line.
