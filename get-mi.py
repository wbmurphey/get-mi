#!/usr/bin/python3

import json
import subprocess

def 

inventory = json.loads(subprocess.getoutput('aws ssm get-inventory'))
inventory = inventory['Entities']

for i in inventory:
    entries[i['Id']] = i['Data']['AWS:InstanceInformation']['Content'][0]['ComputerName']