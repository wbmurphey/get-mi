#!/usr/bin/python3

import json
import subprocess


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

while True:
    # Searching entries dict for user input
    user_input = str(input('Enter a string to search for: \n'))
    search_dict = get_inventory(user_input)

    if search_dict:
        print('')
        for k, v in search_dict.items():
            print(f'{k}\n{v}\n\n')
        break
    else:
        print(f'Search returned no results. Try again.')
        continue