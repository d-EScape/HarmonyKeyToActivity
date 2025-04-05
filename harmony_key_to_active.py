#! /usr/bin/python3

import asyncio
import sys
from aioharmony.harmonyapi import HarmonyAPI, SendCommandDevice

# ---- configuration starts here --------

HUB_IP = '192.168.19.223'

#Constants like these are not required, but can be helpful when a devicename changes and 
#to keep the configuration readable. Adapt to your setup and expand to your liking.
DEFAULT_TV = "KPN iTV+ tivo"
DEFAULT_VOLUME = "Denon X4500h"
DEFAULT_APPLETV = "Tv Apple 4"
DEFAULT_ANDROID = "NVIDIA Game Console"

DEFAULT_KEY_PLAY = "Play"
DEFAULT_KEY_PAUSE = "Pause"
DEFAULT_KEY_STOP = "Stop"
DEFAULT_KEY_MUTE = "Mute"

#Configure the correct keypresses for any activity
#[activity name][lowercase button name] contains [device] to respond and (case sensitive!) key to [press] 
keyByActivity={
   "Apple TV kijken" : {
   						'play': { 
   									"device" : DEFAULT_APPLETV,
   									"press" : DEFAULT_KEY_PLAY
   								},
   						'pause': { 
   									"device" : DEFAULT_APPLETV,
   									"press" : DEFAULT_KEY_PAUSE
   								},
   						'stop': { 
   									"device" : DEFAULT_APPLETV,
   									"press" : "Back"
   								},
   						'mute': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_MUTE
   								}   							
   						},
    "TV Kijken" : {
   						'play': { 
   									"device" : DEFAULT_TV,
   									"press" : DEFAULT_KEY_PLAY
   								},
   						'pause': { 
   									"device" : DEFAULT_TV,
   									"press" : DEFAULT_KEY_PAUSE
   								},
   						'stop': { 
   									"device" : "KPN iTV+ keyboard ",
   									"press" : DEFAULT_KEY_STOP
   								},
   						'mute': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_MUTE
   								}
   						},  	  								
    "SHIELD TV" : {
   						'play': { 
   									"device" : DEFAULT_ANDROID,
   									"press" : DEFAULT_KEY_PLAY
   								},
   						'pause': { 
   									"device" : DEFAULT_ANDROID,
   									"press" : DEFAULT_KEY_PAUSE
   								},
   						'stop': { 
   									"device" : DEFAULT_ANDROID,
   									"press" : DEFAULT_KEY_STOP
   								},
   						'mute': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_MUTE
   								}
   						},
    "Muziek luisteren" : {
   						'play': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_PLAY
   								},
   						'pause': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_PAUSE
   								},
   						'stop': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_STOP
   								},
   						'mute': { 
   									"device" : DEFAULT_VOLUME,
   									"press" : DEFAULT_KEY_MUTE
   								}
   						}
   				} 		    		   

# ---- configuration ends here --------

async def pressactive(key):
	hub = HarmonyAPI(HUB_IP)
	await hub.connect()
	actid, actname = hub.current_activity
	print('Send key corresponding to', key, 'for running activity', actid, '('+actname+')')
	
	if actname in keyByActivity and key in keyByActivity[actname]:
		targetdevicename = keyByActivity[actname][key]["device"]
		targetdevice = hub.get_device_id(targetdevicename)
		targetbutton = keyByActivity[actname][key]["press"]
		payload = SendCommandDevice(
      		device=targetdevice,
      		command=targetbutton,
      		delay=0
      		)
		print('Sending', str(payload))
		await hub.send_commands(payload)
	else:
		print('There is no configuration for the current activity and key', actname, key)
	
try:
	button = sys.argv[1]
except:
	print('Requires a button to be pressed as argument (play, pause, mute or others that are configured within the program)')
else:
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.run_until_complete(pressactive(button.lower()))
	
