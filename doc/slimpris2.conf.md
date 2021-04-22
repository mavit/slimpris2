# NAME

**slimpris2.conf** — `slimpris2` configuration file

# DESCRIPTION

## Connection

*scheme*
: Defaults to `http`.  LMS cannot currently use `https` unless it is behind a reverse proxy.

*host*
: The hostname where LMS is running.  Defaults to `localhost` if not specified here or on the command line.

*port*
: The port number where LMS is running.  Defaults to `9000` if not specified here or in the configuration file.

*player*
: The name or MAC address of the Squeezebox that you wish to control.  Defaults to the first connected, if not specified here or on the command line.

*username*
: The username needed to connect to LMS, if required by LMS.

*password*
: The password needed to connect to LMS, if required by LMS.

## Bling

*mmkeys*
: Should we react to multimedia keys?  Defaults to false.

# FILES

1. `@sysconfdir@/slimpris2.conf`
1. `$XDG_CONFIG_HOME/slimpris2/slimpris2.conf` or `~/.config/slimpris2/slimpris2.conf`

Last takes precedence.

# SEE ALSO

- slimpris2(1)
- slimpris2.service(7)
- [Source code, bug reports, etc.](https://github.com/mavit/slimpris2)

---
title: slimpris2.conf
section: 5
header: slimpris2
footer: slimpris2 @VERSION@
date: April 2021
author: Peter Oliver <git@mavit.org.uk>
...
