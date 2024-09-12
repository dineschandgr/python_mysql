from dbconfig import dbconfig
from User import User

def get_users():
    conn = dbconfig.open_connection()
    cur = conn.cursor()
    cur.execute("select * from users")
    output = cur.fetchall()

    users_list = []
    for i in output:
        print("select query output ",i)
        user = User(i[0], i[1], i[2],"Dummy", i[3]);
        users_list.append(user)

    dbconfig.close_connection(conn)
    return users_list

def get_user(user_id):
    conn = dbconfig.open_connection()
    cur = conn.cursor()
    cur.execute("select * from users where id = " + str(user_id))
    output = cur.fetchall()
    user = ''
    for i in output:
        print("select query output ", i)
        user = User(i[0], i[1], i[2], "Dummy", i[3]);

    dbconfig.close_connection(conn)
    return user

def create_user(user):
    conn = dbconfig.open_connection()
    cur = conn.cursor()
    cur.execute("""
            insert into users(id, email, password, username ) values ( %s, %s, %s, %s)
            """,
                (user.id, user.email, user.password, user.user_name))
    print(conn.insert_id())
    conn.commit()


print("enter a value \n")
print("1. Select All Users \n")
print("2. Select One User \n")
print("3. Insert One User \n")

input1 = input()

if input1 == '1':
    user_list_json = get_users()
    print("user list ", user_list_json)
elif input1 == '2':
    get_user('11')
elif input1 == '3':
    user = User(11, "a.acom", "password", "admin", "admin")
    create_user(user)
else:
    print("invalid input")