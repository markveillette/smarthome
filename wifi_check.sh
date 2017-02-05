#!/bin/bash
# This continuously checks if wifi is connection to local network, and trys to restart
# if not.
# Code taken from https://www.raspberrypi.org/forums/viewtopic.php?t=16054
while true ; do
   if ifconfig wlan0 | grep -q "inet addr:" ; then
      sleep 60
   else
      echo "Network connection down! Attempting reconnection."
      ifup --force wlan0
      sleep 10
   fi
done
