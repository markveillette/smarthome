#!/usr/bin/env python
from fauxmo.fauxmo import poller,upnp_broadcast_responder,fauxmo
import os
import time

# Import handler classes
from ir_remote import tv_power_handler,tv_mute_handler
from pianobar  import play_workout_handler

# List all triggers here
TRIGGERS = {"TV":           {'port':52000,'action':tv_power_handler()},
            "TV Speakers":  {'port':0,    'action':tv_mute_handler()},
            "Basement speakers" :{'port':0,    'action':play_workout_handler()}}

# Main method, sets up devices and continually polls
if __name__ == "__main__":
    print "Setting up"
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
