man1_MANS = slimpris2.man
man5_MANS = slimpris2.conf.man
man7_MANS = slimpris2.service.man

CLEANFILES = $(MANS)

edit = sed \
	-e 's|@VERSION[@]|$(VERSION)|g' \
	-e 's|@sysconfdir[@]|$(sysconfdir)|g'

%.man: %.md Makefile
	rm -f $@ $@.tmp
	$(edit) $< | pandoc --to=man --standalone --output=$@.tmp
	chmod a-w $@.tmp
	mv $@.tmp $@
