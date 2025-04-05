# HarmonyKeyToActivity
Send pre-defined remote control button presses to the running activity on Logitech Harmony Hub.

This script gets the running activity from the hub and sends a configured remote control command to 
a device specific to that activity.

Use case: initiating a "Pause", "Play", "Mute" (or any other) command using the same program/trigger, without needing
to know which device is actualy playing.  

I wrote this as a quick and dirty way to mimic voice commands like "Pause on TV", that the official
Harmony google assistant integration offers, since i can no longer get the officiel integration working.
The running of this script and voice control are -in my case- handled by Domoticz (virtual switches) and DZGA.

The script needs te be configured for your setup. The configurartion section is insde the script and mostly self explaining.
To get started:
1. change the HUP_IP
2. Modify the "keyByActivity" dict to your setup (the use of constants is optional)
3. run from the command line like ./harmony_key_to_active.py Mute (the button name on the command line is case-insensitive)

Requires aioharmony and asyncio python modules.

Shared as-is, without any warranty or support.
