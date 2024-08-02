from flask import Flask, request, jsonify

from UserService import user_service
from User import User

app = Flask(__name__)

service = user_service()

@app.route('/user', methods = ['POST'])
def create_user():
    data = request.get_json()
    user = User(data['id'], data['email'], data['password'], data['role'], data['user_name'])
    service.create_user(user)
    doc_json = jsonify(user)
    print("doc json ", doc_json)
    return doc_json

@app.route('/users', methods = ['GET'])
def get_all_users():
    users_list = service.get_users()
    return users_list

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user(user_id)
    return user

@app.route('/test1', methods = ['GET'])
def get_countries_by_region():
    region = request.args.get('region')
    #region = 'asia'
    load_countries(region)
    return load_countries(region)


#http://localhost:5005/api.country.com/countries?region=asia
@app.route('/api.country.com/countries')
def hello():
    region = request.args.get('region')
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

    if region is None:
        return countries


    filtered_list = [c for c in countries if c['region'].lower() == region.lower()]
    print(filtered_list)
    return filtered_list

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5005)



@staticmethod
def load_countries(region):
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

    filtered_list = [c for c in countries if c['region'].lower() == region.lower()]
    print(filtered_list)
    return filtered_list