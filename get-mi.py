#!/usr/bin/python3

import json
import subprocess
import sys


def get_inventory(input: str):
    '''Returns a dictionary of FQDNs and mi numbers'''
    inventory = json.loads(subprocess.getoutput('aws ssm get-inventory'))
    inventory = inventory['Entities']

    entries = {}
    mi_dict = {}

    # Populating dictionary w/ key as Mi Number, value as FQDN.
    for i in inventory:
        entries[i['Id']] = i['Data']['AWS:InstanceInformation']['Content'][0]['ComputerName']

    search = []
    for k, v in entries.items():
        if input.lower() in v:
            search.append(v)

    for i in search:
        mi = [k for k, v in entries.items() if v == i]
        mi_dict[i] = mi[0]

    return mi_dict

# Gets a string from first argument passed.
try:
    guardian_search = str(sys.argv[1])
except IndexError:
    exit()

# Gets an integer from second argument passed, or uses default integer of 1 if no argument is passed.
# Will not accept 0 or less as a selection.
try:
    selection = int(sys.argv[2])
except IndexError:
    selection = 1
except ValueError:
    exit()

if selection > 0:
    selection -= 1
else:
    exit()

# Parses AWS inventory for arguments passed
search_dict = get_inventory(guardian_search)

# Prints to stdout mi number based on arguments passed
if search_dict:
    try:
        sys.stdout.write(search_dict[list(search_dict)[selection]])
    except IndexError:
        exit()