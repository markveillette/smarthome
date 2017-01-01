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

# List triggers here
TRIGGERS = {"TV":  {'port':52000,'action':tv_power_handler()},
            "TV Speakers":{'port':0,'action':tv_mute_handler()} }
#TRIGGERS = {"tv speakers":{'port':0,'action':tv_mute_handler()} }

# Main method, sets up devices and continually polls
if __name__ == "__main__":
    print "Setting up IR remote.."
    # Startup the fauxmo server
    #fauxmo.DEBUG = True
    p = poller()
    u = upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    for trig, d in TRIGGERS.items():
        fauxmo(trig, u, p, None, d['port'],d['action'])

    # Loop and poll for incoming Echo requests
    print "Entering fauxmo polling loop"
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            
            print "An error har occured.."
            break


