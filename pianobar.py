#!/usr/bin/env python
from fauxmo.fauxmo import poller,upnp_broadcast_responder,fauxmo
import os
import time

# Name of computer playin music. This should be the host name 
# in the .ssh config file.  Also there should be an identity file 
# set up so that ssh can send command without a password.
HOST_NAME = 'quinn'

# Music will stop after this time
PLAY_TIME = '3600'

# In this handler, the raspberry pi will send a command to another 
# computer with the command to launch pianobar
#
# This will only play for PLAY_TIME and stop in case someone forgets 
# to turn it off
#
class play_workout_handler(object):
    def __init__(self):
        self.on_cmd = 'on'
        self.off_cmd = 'off'

    def on(self):
        # launch and ki
        #os.system("ssh {host} pianobar &; sleep {time};".format(host=HOST_NAME,time=PLAY_TIME))
        os.system("ssh {host} /home/markv/run_pianobar &".format(host=HOST_NAME))
        print 'pianobar on'
        return True
    def off(self):
        os.system("ssh {host} pkill -f pianobar".format(host=HOST_NAME))
        print "pianobar off"
        return True


