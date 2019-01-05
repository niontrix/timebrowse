INSTALL = install

all:
	@echo "'make install' to install scripts"

install:
	python setup.py install
	$(INSTALL) -d $(DEST)/etc/
	$(INSTALL) systemd/system/nilfs.service $(DEST)/etc/systemd/system
