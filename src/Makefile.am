desktopdir = ${datadir}/applications/
dbusdir = ${datadir}/dbus-1/services/

dist_bin_SCRIPTS = slimpris2
dist_desktop_DATA = org.mpris.MediaPlayer2.squeezebox.desktop
dist_doc_DATA = slimpris2.conf
nodist_dbus_DATA = org.mpris.MediaPlayer2.squeezebox.service

if HAVE_SYSTEMD
nodist_systemduserunit_DATA = slimpris2.service
systemduserpreset_DATA = 80-slimpris2.preset
endif

EXTRA_DIST = org.mpris.MediaPlayer2.squeezebox.service.in slimpris2.service.in slimpris2.in
CLEANFILES = org.mpris.MediaPlayer2.squeezebox.service slimpris2.service slimpris2.py slimpris2

edit = sed -e 's|@bindir[@]|$(bindir)|g' \
	   -e 's|@datadir[@]|$(datadir)|g' \
	   -e 's|@PYTHON[@]|$(PYTHON)|g'

slimpris2: slimpris2.in
	$(edit) $< > $@
	chmod +x $@
	ln -sf $@ $@.py

%.service: %.service.in
	$(edit) $< > $@

test: test-desktop

test-desktop: org.mpris.MediaPlayer2.squeezebox.desktop
	desktop-file-validate $<
