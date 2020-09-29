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

Restart your session or `slimpris2` after changing `slimpris2.conf`.
