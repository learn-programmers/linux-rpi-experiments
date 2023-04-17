obj-m += led_control.o
KDIR = /lib/modules/$(shell uname -r)/build
PWD = $(shell pwd)

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean

install:
	$(MAKE) -C $(KDIR) M=$(PWD) modules_install
	depmod -A

uninstall:
	rm -f /lib/modules/$(shell uname -r)/extra/led_control.ko
	depmod -A

