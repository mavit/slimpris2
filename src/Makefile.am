desktopdir = ${datadir}/applications/
dbusdir = ${datadir}/dbus-1/services/

dist_bin_SCRIPTS = slimpris2
dist_desktop_DATA = io.github.mavit.slimpris2.desktop
dist_doc_DATA = slimpris2.conf
nodist_dbus_DATA = org.mpris.MediaPlayer2.slimpris2.service

if HAVE_SYSTEMD
nodist_systemduserunit_DATA = slimpris2.service
systemduserpreset_DATA = 80-slimpris2.preset
endif

EXTRA_DIST = org.mpris.MediaPlayer2.slimpris2.service.in slimpris2.service.in slimpris2.in
CLEANFILES = org.mpris.MediaPlayer2.slimpris2.service slimpris2.service slimpris2.py slimpris2

edit = sed \
	-e 's|@bindir[@]|$(bindir)|g' \
	-e 's|@datadir[@]|$(datadir)|g' \
	-e 's|@sysconfdir[@]|$(sysconfdir)|g' \
	-e 's|@PYTHON[@]|$(PYTHON)|g' \
	-e 's|@VERSION[@]|$(VERSION)|g'

slimpris2: slimpris2.py.in Makefile
	rm -f $@ $@.tmp
	$(edit) $< > $@.tmp
	chmod +x,a-w $@.tmp
	mv $@.tmp $@

%.service: %.service.in Makefile
	rm -f $@ $@.tmp
	$(edit) $< > $@.tmp
	chmod a-w $@.tmp
	mv $@.tmp $@

test: test-desktop

test-desktop: io.github.mavit.slimpris2.desktop
	desktop-file-validate $<
