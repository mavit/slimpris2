AC_INIT(slimpris2, 3.1.1
AM_INIT_AUTOMAKE()
AM_PATH_PYTHON([3.6])
GETTEXT_PACKAGE=slimpris2
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE",
    [The prefix for our gettext translation domains.])
IT_PROG_INTLTOOL(0.26)

PKG_PROG_PKG_CONFIG
AC_ARG_WITH([systemduserpresetdir],
        AS_HELP_STRING([--with-systemduserpresetdir=DIR], [Directory for systemd preset files]),
        [], [with_systemduserpresetdir=$($PKG_CONFIG --variable=systemduserpresetdir systemd)])
AC_ARG_WITH([systemduserunitdir],
        AS_HELP_STRING([--with-systemduserunitdir=DIR], [Directory for systemd service files]),
        [], [with_systemduserunitdir=$($PKG_CONFIG --variable=systemduserunitdir systemd)])
AC_SUBST([systemduserpresetdir], [$with_systemduserpresetdir])
AC_SUBST([systemduserunitdir], [$with_systemduserunitdir])
AM_CONDITIONAL(HAVE_SYSTEMD, [test -n "$with_systemduserpresetdir"])
AM_CONDITIONAL(HAVE_SYSTEMD, [test -n "$with_systemduserunitdir"])

AC_OUTPUT([
Makefile
doc/Makefile
src/Makefile
po/Makefile.in
])

dnl Warn user sysconfdir is not /etc, if necessary.
make sysconfdirwarning

