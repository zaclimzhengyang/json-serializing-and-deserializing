import json

# serialized string
# multi line string when attached to variable is considered a string
# if not, it will be considered as a block comment
# false > False
# null > None
# true > True
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bugosemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# deserialize a JSON document to a Python object.
# convert back to dictionary
dataz = json.loads(people_string)
print(dataz)

# return dictionary class type
print(type(dataz))

# return list class type for value of 'people'
print(type(dataz['people']))

# return names of the people in json file
for people in dataz['people']:
    print(people['name'])

# remove phone number in each record in json file
for people in dataz['people']:
    del people['phone']

# serialize object as a JSON formatted stream
# Converts input dictionary into string and stores it in json_string
# indent makes it easier to read
# sort_keys allows to sort by keys
new_string = json.dumps(dataz, indent = 2, sort_keys=False)
sorted_string = json.dumps(dataz, indent = 2, sort_keys=True)

print(new_string)
print(sorted_string)