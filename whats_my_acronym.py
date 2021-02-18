''' Ask the user for an organization name and return the acronym for it'''

user_organization_input = input("What is an organizations name? ")
user_organization_split = user_organization_input.split()
organization_acronym = ''

for word in user_organization_split:
    organization_acronym += word[0]
    
print("{}'s acronym is {}".format(user_organization_input,organization_acronym))
