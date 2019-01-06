INSTALL = install
UPSTART = $(shell test -d /etc/init && echo upstart)
SYSTEMD = $(shell test -d /run/systemd && echo systemd)

all:
	@echo "usage:"
	@echo "  - 'make systemd' to install scripts if your system is using systemd as the init system"
	@echo "  - 'make sysv' to install scripts if your system is using sysv init"

install:
	@echo "installing nilfs2_ss_manager"
	python setup.py install --record installed-files.txt
	@echo "/etc/nilf_ss.conf" >> installed-files.txt

ifeq ($(SYSTEMD), systemd)
	@echo "system seems to be using systemd"
	$(INSTALL) -d $(DEST)/etc/
	$(INSTALL) -d $(DEST)/etc/systemd
	$(INSTALL) -d $(DEST)/etc/systemd/system
	$(INSTALL) systemd/system/nilfs.service $(DEST)/etc/systemd/system
	@echo "$(DEST)/etc/systemd/system/nilfs.service" >> installed-files.txt

else # system seems to be using sysv init -- openrc is currently not tested for
	@echo "system seems to be using sysv init"
	$(INSTALL) -d $(DEST)/etc/
	$(INSTALL) -d $(DEST)/etc/default
	$(INSTALL) default/nilfs $(DEST)/etc/default
  @echo "$(DEST)/etc/default/nilfs" >> installed-files.txt
	$(INSTALL) -d $(DEST)/etc/init.d

ifeq ($(UPSTART), upstart)
		@echo "system seems to be using upstart"
		$(INSTALL) -d $(DEST)/etc/init
		$(INSTALL) -m 0644 init/nilfs.conf $(DEST)/etc/init
		@echo "$(DEST)/etc/init/nilfs.conf" >> installed-files.txt
		test -e $(DEST)/etc/init.d/nilfs || ln -s $(DEST)/lib/init/upstart-job $(DEST)/etc/init.d/nilfs
		@echo "$(DEST)/etc/init.d/nilfs" >> installed-files.txt
else
		$(INSTALL) init.d/nilfs $(DEST)/etc/init.d
		@echo "$(DEST)/etc/init.d/nilfs" >> installed-files.txt
endif

endif

uninstall:
	@echo "removing installed files"
	cat installed-files.txt | xargs sudo rm -f
