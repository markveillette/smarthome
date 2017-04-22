A set of python scripts I use for home automation with my Amazon Echo.

The method used to control smart home devices is based on fauxmo found here:
https://github.com/makermusings/fauxmo

To control these devices, I followed the method described here:
http://www.makermusings.com/2015/07/13/amazon-echo-and-home-automation/

Included here are scripts for

--  A TV remote controlled by my raspberry pi using lirc
--  Music streamer on Ubuntu using pianobar

The list of devices controlled are set by the TRIGGERS variable in main.py.  Each trigger uses a handler defined in separate .py files.

The TV remote uses LIRC package and a simple LED hooke dup to the GPIO pins on the pi.  To design the IR LED circut, I followed
http://randomtutor.blogspot.gr/2013/01/web-based-ir-remote-on-raspberry-pi.html

#####
## Setting up LIRC for your remote
#####

1.  Follow tutorial at http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/

2. Grab .conf file for your remote at http://lirc-remotes.sourceforge.net/remotes-table.html

3. Copy contents of this file to /etc/lirc/lircd.conf

4. In python script(s), make sure the correct name of the remote is passed to ir_remoste handlers. 

#####
## Setting up pianobar
#####

This is a bit ugly, but it works. pianobar.py sshes into a linux machine with pianobar installed on local network and runs a script called run_pianobar.  In my case, this computer is named 'quinn'.  This script that runs on the streaming machine contains the following:
    #!/bin/bash
    pianobar &
    sleep 3600 
In order for this to work, ssh keys but be used so the ssh doesn't require a password. If you are adapting this, you'll need to change pianobar.py to ssh into the machine you want (or, if your pi is connected to the speakers, just run pianobar).






