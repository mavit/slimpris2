# NAME

**slimpris2** — Control Logitech Media Server via MPRIS

# SYNOPSIS

**slimpris2** [**-d**] [*hostname* *port* [*player*]]

# OPTIONS

*hostname*
: The hostname where LMS is running.  If not specified here or in the configuration file, auto-discovery will be attempted.

*port*
: The port number where LMS is running.

*player*
: The name or MAC address of the Squeezebox that you wish to control.  Defaults to the first connected if not specified here or in in the configuration file.

**--debug** | **-d**
: Output debugging information.

**--version** | **-V**
: Display version and copyright information.

# DESCRIPTION

Provide a bridge between the MPRIS media player remote control protocol and Logitech Media Server, allowing it to be controlled using the user interfaces integrated into your Linux desktop.

`slimpris2` is run in the user session and monitors a local or distant `squeezeboxserver`.

# SEE ALSO

- slimpris2.conf(5)
- slimpris2.service(7)
- [Source code, bug reports, etc.](https://github.com/mavit/slimpris2)
- [Discussion on Slim Devices forum](https://forums.slimdevices.com/showthread.php?108956-MPRIS-support-via-slimpris2)
- [Logitech Media Server](https://wiki.slimdevices.com/index.php/Logitech_Media_Server)
- [MPRIS specification](https://specifications.freedesktop.org/mpris-spec/latest/)

---
title: slimpris2
section: 7
header: slimpris2
footer: slimpris2 @VERSION@
date: April 2021
author: Peter Oliver <git@mavit.org.uk>
...
