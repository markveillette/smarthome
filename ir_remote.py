#!/usr/bin/env python
from fauxmo.fauxmo import poller,upnp_broadcast_responder,fauxmo
import os
import time

# Set a default remote name
DEFAULT_REMOTE='SamsungBN59-01054A'

# Base class for various TV handlers
class tv_remote_handler(object):
    def __init__(self,remote_name=DEFAULT_REMOTE):
        """
        Handler for controling TV with lirc

        Parameters
        ----------
        remote_name:  Name of remote in /etc/lirc/lircd.conf file
        """
        self.on_cmd = 'on'
        self.off_cmd = 'off'
        self.remote_name=remote_name
        self.key = 'KEY_POWER' # Set in superclass
        self.cmd = 'irsend {s} {r} {k}'
    
    def issue(self,cmd):
        """
        Issues system command cmd
        
        Parameters
        ----------
             cmd  Command to run
        """
        os.system(cmd)
   
    def send(self,key,n=1):
        """
        Sends key one or more times

        Parameters
        ----------
               key  Remote command to send, e.g. KEY_POWER
                 n  Number of times to send
        """
        for i in range(n):
            self.issue(self.cmd.format(s='SEND_ONCE',
                                   r=self.remote_name,
                                   k=key))
            time.sleep(0.1)               

    def send_continuous(self,key,send_length=0.1):
        """
        Sends IR signal continuously for length send_length seconds
         
        Parameters
        ----------
                key  Remote command to send, e.g. KEY_POWER
        send_length  Length of time that command is being sent

        """
        self.issue(self.cmd.format(s='SEND_START',
                              r=self.remote_name,
                              k=key))
        time.sleep(send_length)
        self.issue(self.cmd.format(s='SEND_STOP',
                              r=self.remote_name,
                              k=key)) 
        
   


# This handler class is used to control TV power button.
class tv_power_handler(tv_remote_handler):
    def __init__(self,remote_name=DEFAULT_REMOTE):
        """
        Handler for tuning TV power on and off

        Parameters
        ----------
        remote_name:  Name of remote in /etc/lirc/lircd.conf file

        """
        tv_remote_handler.__init__(self,remote_name=remote_name)

    def on(self):
        """
        Turns on TV

        Note: I needed to send multiple "on" signals to my TV for 
        this to work.
        """
        self.send_continuous(key='KEY_POWER',send_length=0.1)
        print "TV power on"
        return True
    def off(self):
        """
        Turns off TV
        """
        self.send('KEY_POWER',n=1)
        print "TV power off"
        return True

class tv_mute_handler(tv_remote_handler):
    def __init__(self,remote_name=DEFAULT_REMOTE):
        """
        Constructor
        Parameters
        ----------
        remote_name:  Name of remote in /etc/lirc/lircd.conf file
        """
	tv_remote_handler.__init__(self,remote_name=remote_name)

    def on(self):
        """
        Turns on Mute
        """
        self.send('KEY_MUTE',n=1)
        print "TV mute on"
        return True
    def off(self):
        """ 
        Turns off mute
        """
        self.send('KEY_MUTE',n=1)
        print "TV mute off"
        return True



