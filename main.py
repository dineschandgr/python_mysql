import pymysql

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


def open_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="password",
        db='user_schema',
    )
    return conn

def close_connection(conn):
    conn.close()

# Select query
def get_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("select * from user")
    output = cur.fetchall()

    for i in output:
        print("select query output ",i)

    close_connection(conn)

def get_user(user_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("select * from user where id = " + user_id)
    output = cur.fetchall()

    for i in output:
        print("select query output ", i)

    close_connection(conn)


def insert_static_value(user_list):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
                insert into user(id, email, password, user_name ) values ( %s, %s, %s, %s)
                """,
                (1111, 'test@test.com', 'password', 'test'))
    print(conn.insert_id())
    conn.commit()

def insert_dynamic_value(user_list):
    conn = open_connection()
    cur = conn.cursor()
    for user in user_list:
        cur.execute("""
             insert into user(id, email, password, user_name ) values ( %s, %s, %s, %s)
             """,
                    (user.id, user.email, user.password, user.user_name))
    print(conn.insert_id())
    conn.commit()

get_users()
get_user('1919191919192')

user1 = User(3333,'a@test.com', 'password','USER', 'test')
print("user ", user1)
user_list = []
user_list.append(user1)
insert_dynamic_value(user_list)
get_user('3333')