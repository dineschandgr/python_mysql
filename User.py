from flask import json



countries = [
        {
            "name": "Afghanistan",
            "region": "Asia"
        },
        {
            "name": "Albania",
            "region": "Europe"
        },
        {
            "name": "Algeria",
            "region": "Africa"
        },
        {
            "name": "India",
            "region": "Asia"
        }
    ]

print(type(countries[0]))

filtered_list = [c for c in countries if c['region'] == 'Asia']
print(filtered_list)

class User:
    id = 0
    email = ''
    password = ''
    role = ''
    user_name = ''

    def __init__(self, id, email, password, role, user_name ):
        self.id = id
        self.email = email
        self.password = password
        self.role = role
        self.user_name = user_name

    def __str__(self) -> str:
        return f"{self.id} - {self.email}  - {self.password} - {self.role} - {self.user_name})"

    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)

