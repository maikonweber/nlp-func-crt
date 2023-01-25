import psycopg2


def select_data(id):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5732",
            user="cook",
            password="cook",
            dbname="cook"
        )

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM travel_book WHERE id = {id}")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except psycopg2.Error as e:
        print(e)


def cursor():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5732",
            user="cook",
            password="cook",
            dbname="cook"
        )
        cur = conn.cursor()
        return cur
    except psycopg2.Error as e:
        print(e)

def createTestAndInsert(name):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5732",
            user="cook",
            password="cook",
            dbname="cook"
        )

        cur = conn.cursor()
        cur.execute(f"Alter Table travel_book Add Columns {name}")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except psycopg2.Error as e:
        print(e)
