#!/usr/bin/env python
import json
import gzip
import os
instance_list=[]
dir_path='/tmp/ctlogs/'
for filename in os.listdir(dir_path):
	file_path=dir_path+filename
	input=gzip.open(file_path, "r")
	response=json.loads(input.readlines()[0])["Records"]
	for i in response:
		if i.get('eventName') == 'RunInstances':
			for instance in i.get('responseElements').get('instancesSet').get('items'):
				instance_list.append(instance.get('instanceId'))
			print i.get('responseElements').get('reservationId') + "::" + str(instance_list)
			instance_list=[]	
	
