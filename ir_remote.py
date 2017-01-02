#!/usr/bin/env python
from fauxmo.fauxmo import poller,upnp_broadcast_responder,fauxmo
import os
import time

# This handler class is used to control TV power button.
# In this case, "on" and "off" do the same thing - transmit the 
# power LED sequence
class tv_power_handler(object):
    def __init__(self):
        self.on_cmd = 'on'
        self.off_cmd = 'off'

    def on(self):
        os.system('irsend SEND_START Samsung_BN59-00861A KEY_POWER')
        time.sleep(0.1)
        os.system('irsend SEND_STOP Samsung_BN59-00861A KEY_POWER')
        print "TV power on"
        return True
    def off(self):
        os.system('irsend SEND_ONCE Samsung_BN59-00861A KEY_POWER')
        print "TV power off"
        return True

class tv_mute_handler(object):
    def __init__(self):
        self.on_cmd = 'on'
        self.off_cmd = 'off'

    def on(self):
        os.system('irsend SEND_ONCE Samsung_BN59-00861A KEY_MUTE')
        print "TV mute on"
        return True
    def off(self):
        os.system('irsend SEND_ONCE Samsung_BN59-00861A KEY_MUTE')
        print "TV mute off"
        return True



