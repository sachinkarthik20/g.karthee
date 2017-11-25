#!/usr/bin/env python
from __future__ import print_function

import json
import urllib
import boto3
import os
import gzip
print('Loading function')
#tag_list = ['Server Name','Name','Cost Center','Purpose']
tag_list = ['name']
tag_names = []
instances_to_be_terminated=[]
#s3 = boto3.client('s3')
#print("Received event: " + json.dumps(event, indent=2))

# Get the object from the event and show its content type
#bucket = event['Records'][0]['s3']['bucket']['name']
#key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
def stop_instances(instances_to_be_stopped=[]):
    ec2 = boto3.client('ec2', region_name='eu-west-1')
    ec2.stop_instances(InstanceIds=instances_to_be_stopped)
    print('Stopping the identified tags which are not meeting tagging requirements')

for filename in os.listdir('/tmp/ctlogs/'):
	file_path = '/tmp/ctlogs/'+filename
	input=gzip.open(file_path, "r")
	response = json.loads(input.readlines()[0])["Records"]
	for i in response:
		if i.get('eventName') == 'RunInstances':
			if 'requestParameters' in i.keys():
				if i.get('requestParameters') != None and 'tagSpecificationSet' in i.get('requestParameters').keys():
					#if i.get('requestParameters').get('instancesSet').get('items')[0].get('maxCount') == 2:
					for type in i.get('requestParameters').get('tagSpecificationSet').get('items'):
						if type.get('resourceType') == 'instance':
							assigned_tags = type.get('tags')
							for temp in assigned_tags:
								tag_names.append(temp.get('key'))
							if set(tag_list).issubset(tag_names):
								print(tag_names)
								print('All required tags are present')
								tag_names=[]
								continue
							else: 
								print(tag_names)
								tag_names=[]
								for instance in i.get('responseElements').get('instancesSet').get('items'):
									instances_to_be_terminated.append(instance.get('instanceId'))
								stop_instances(instances_to_be_stopped)
								print(instances_to_be_terminated)
								instances_to_be_terminated=[]
