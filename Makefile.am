AUTOMAKE_OPTIONS = foreign
SUBDIRS = src po
dist_doc_DATA = README.md COPYING AUTHORS

EXTRA_DIST = autogen.sh

DISTCHECK_CONFIGURE_FLAGS = \
        --with-systemduserpresetdir=$$dc_install_base/$(systemduserpresetdir)
        --with-systemduserunitdir=$$dc_install_base/$(systemduserunitdir)

dist-hook:
	rm -rf `find $(distdir) -name *~`

sysconfdirwarning:
	@if test "${sysconfdir}" != "/etc"; then \
		echo '###'; \
		echo '### $${sysconfdir} evaluates to '${sysconfdir}': this is probably not what you want !'; \
		echo '### You may want to launch ./configure --sysconfdir=/etc.'; \
		echo '###'; \
	fi

test:
	$(MAKE) -C src $@

.PHONY = sysconfdirwarning
