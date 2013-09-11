#!/bin/bash
# GET interface to send xdotool key commands via web requests. Basically, send
# keystrokes over the network!
# 
# WARNING: *Incredibly* unsafe. No sanitized input means that it's trivial to
#          inject arbitrary shell code to be run at web permissions on the
#          server (www-data). This should never be public-facing, and should
#          at least be protected by .htaccess. Like, seriously.
#          Not to mention the fact that this thing allows ARBITRARY KEYSTROKES
#          to be simulated in X. It should go without saying that this thing
#          is a security nightmare. Please be careful with its use. No warranty,
#          and not recommended for any important systems.
# 
# Requires: Apache with CGI-BIN enabled (usually on by default).
#           xdotool
# 
# Usage: Plop in cgi-bin (default apache2 location on Ubuntu: /usr/lib/cgi-bin),
#        add www-data (or whatever uid apache runs under) to the active user's
#        xhost whitelist ("xhost +SI:localuser:www-data"; this is also not
#        exactly secure), and then call the script via GET'ing it, with keys in
#        the query string.
# 
# Example: curl "127.0.0.1/cgi-bin/keytest.cgi?shift+d"
export DISPLAY=":0.0"

printf "Content-type: text/html\n\n"
echo "Running: xdotool key --clearmodifiers $QUERY_STRING"
xdotool key --clearmodifiers $QUERY_STRING
