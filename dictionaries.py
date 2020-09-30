# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict

person = {
    'first_name': 'Jesse',
    'last_name': 'Pinkman',
    'age': 25
}

# Get value

print(person['first_name'])
print(person.get('last_name'))


# Add key value

person['phone'] = 522222
print(person)

# Get dict keys

print(person.keys())

# Get dict items

print(person.items())

# copy dictt

person2 = person.copy()
person2['city'] = 'boston'

# list of dicts

people = [
    {
        'name': 'Aruvi',
        'age': 18
    },
    {
        'name': 'Sudhev',
        'age': 34
    }
]
