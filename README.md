remotekey-cgi
=============

A RESTful (kinda, not really) means of triggering keyboard events on a Linux system via GET commands.


### Requirements
- Apache with CGI-BIN enabled (usually on by default).
- xdotool

### Usage
Plop in cgi-bin (default apache2 location on Ubuntu: /usr/lib/cgi-bin), add www-data (or whatever uid apache runs under) to the active user's xhost whitelist ("xhost +SI:localuser:www-data"; this is not exactly secure), and then call the script via GET'ing it, with keys in the query string.
 
### Example
> curl "127.0.0.1/cgi-bin/keytest.cgi?shift+d"
