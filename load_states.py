import json

# loading json object from states.json
with open('states.json') as state_file:
    data = json.load(state_file)

# print the entire entry and with its abbreviation separately
for state in data['states']:
    print(state)
    print(state['abbreviation'])

# delete area codes from each entry
for state in data['states']:
    del state['area_codes']

# create new_states.json file automatically in the same directory using data from state_file
with open('new_states.json', 'w' ) as state_file:
    json.dump(data, state_file, indent=2)