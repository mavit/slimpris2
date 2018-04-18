desktopdir = ${datadir}/applications/
dbusdir = ${datadir}/dbus-1/services/
autostartdir = ${sysconfdir}/xdg/autostart/

dist_bin_SCRIPTS = slimpris2
dist_desktop_DATA = slimpris2.desktop
autostart_DATA = slimpris2.desktop
dist_doc_DATA = slimpris2.conf
nodist_dbus_DATA = org.mpris.MediaPlayer2.squeezebox.service

EXTRA_DIST = org.mpris.MediaPlayer2.squeezebox.service.in slimpris2.in
CLEANFILES = org.mpris.MediaPlayer2.squeezebox.service slimpris2.py slimpris2

edit = sed -e 's|@bindir[@]|$(bindir)|g' \
	   -e 's|@datadir[@]|$(datadir)|g' \
	   -e 's|@PYTHON[@]|$(PYTHON)|g'

slimpris2: Makefile
	rm -f $@ $@.tmp
	$(MKDIR_P) $(@D)
	srcdir=''
	test -f ./$@.in || srcdir=$(srcdir)/
	$(edit) $${srcdir}$@.in > $@.tmp
	mv $@.tmp $@
	ln -sf $@ $@.py

org.mpris.MediaPlayer2.squeezebox.service: Makefile
	rm -f $@ $@.tmp
	$(MKDIR_P) $(@D)
	srcdir=''
	test -f ./$@.in || srcdir=$(srcdir)/
	$(edit) $${srcdir}$@.in > $@.tmp
	mv $@.tmp $@
