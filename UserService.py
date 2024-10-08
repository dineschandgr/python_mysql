# Select query
import pymongo

from dbconfig import dbconfig
from User import User
import json

class user_service:

    def get_users(self):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from users")
        output = cur.fetchall()

        users_list = []
        for i in output:
            print("select query output ",i)
            user = User(i[0], i[1], i[2],"Dummy", i[3]);
            users_list.append(json.loads(user.to_json()))

        dbconfig.close_connection(conn)
        return users_list

    def get_user(self, user_id):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from user where id = " + str(user_id))
        output = cur.fetchall()
        user = ''
        for i in output:
            print("select query output ", i)
            user = User(i[0], i[1], i[2], "Dummy", i[3]);

        dbconfig.close_connection(conn)
        return user.to_json()


    def insert_static_value(user_list):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                    insert into user(id, email, password, user_name ) values ( %s, %s, %s, %s)
                    """,
                    (1111, 'test@test.com', 'password', 'test'))
        print(conn.insert_id())
        conn.commit()

    def create_user(self, user):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                insert into users(id, email, password, username ) values ( %s, %s, %s, %s)
                """,
                    (user.id, user.email, user.password, user.user_name))
        print(conn.insert_id())
        conn.commit()

    def insert_dynamic_value(user_list):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        for user in user_list:
            cur.execute("""
                 insert into user(id, email, password, user_name ) values ( %s, %s, %s, %s)
                 """,
                        (user.id, user.email, user.password, user.user_name))
        print(conn.insert_id())
        conn.commit()

    def insert_mongo(self, student):
         connection_url = "mongodb+srv://livewirecbehopecollege:test1234@livewire.3r9b77u.mongodb.net"
         client = pymongo.MongoClient(connection_url)

         db = client['Python-Mongo']

         collection = db['Python-Mongo-Collection']
         collection.insert_one(student)

# user_service = user_service()
# user_list_json = user_service.get_users()
# print("user list ",user_list_json)
#
# user = User(1,"a.acom","password","admin","admin")
# user_service.create_user(user)

# user_service = user_service()
# user_service.get_users()
# user_service.get_user('1919191919192')
#
# user1 = User(3333,'a@test.com', 'password','USER', 'test')
# print("user ", user1)
# user_list = []
# user_list.append(user1)
# user_service.insert_dynamic_value(user_list)
# user_service.get_user('3333')