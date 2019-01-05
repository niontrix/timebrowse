INSTALL = install

all:
	@echo "'make systemd' to install scripts if your system is using systemd as the init system"
  @echo "'make sysv' to install scripts if your system is using sysv init"

systemd:
	python setup.py install
	$(INSTALL) -d $(DEST)/etc/
	$(INSTALL) systemd/system/nilfs.service $(DEST)/etc/systemd/system

sysv:
	$(INSTALL) -d $(DEST)/etc/
	$(INSTALL) -d $(DEST)/etc/default
	$(INSTALL) default/nilfs $(DEST)/etc/default
	$(INSTALL) -d $(DEST)/etc/init.d
ifeq ($(UPSTART), upstart)
	$(INSTALL) -d $(DEST)/etc/init
	$(INSTALL) -m 0644 init/nilfs.conf $(DEST)/etc/init
	test -e $(DEST)/etc/init.d/nilfs || ln -s $(DEST)/lib/init/upstart-job $(DEST)/etc/init.d/nilfs
else
	$(INSTALL) init.d/nilfs $(DEST)/etc/init.d
endif
