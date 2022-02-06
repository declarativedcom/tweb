thttpd
+++
Named version thttpd 2.26 fixes a lot of patches, and introduces a way to avoid
the shellshock security vulnerability, before bash is executed.

Main changes done in libhttpd.c, check DEBUG_SHOCK define.
The define IGNORE_SHELLSHOCK should never be 'defined'.


How to test:
	firstly, be sure port 8080 is blocked at the outside network;
	./thttpd -u $USER -c '*'.cgi -nov -p 8080 -D -d ../tweb

