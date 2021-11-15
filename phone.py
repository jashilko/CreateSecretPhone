import os
import sys
import random
import pymysql.cursors


def get_rand(conn):
    """Get and check random number"""
    rand = random.randint(100000, 999999)
    try:
        with conn.cursor() as cursor:
            sql = "select random from phones where random=%s"
            cursor.execute(sql, (rand))
            oneRow = cursor.fetchone()
            if oneRow:
                get_rand(conn)
            else:
                return rand
    except Exception as e:
        print("Ошибка: %s" % str(e))


phone_arg = ""
if len(sys.argv) > 1:
    phone_arg = sys.argv[1]
    phone_arg = phone_arg[-10:]
else:
    print("No phones")

if phone_arg:
    try:
        connection = pymysql.connect(host=os.getenv("HOST", ""),
                                     user=os.getenv("USER", ""),
                                     password=os.getenv("PASS"),
                                     db=os.getenv("DB"),
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "select random from phones where phone=%s"
                cursor.execute(sql, (phone_arg))
                oneRow = cursor.fetchone()
                if oneRow:
                    print("phone exists. random: {}".format(oneRow["random"]))
                else:
                    random = get_rand(connection)
                    sql = "insert into phones (phone, random, datetime) values(%s, %s, now())"
                    cursor.execute(sql, (phone_arg, str(random)))
                    connection.commit()
                    print(random)
        finally:
            connection.close()
    except Exception as e:
        print("Ошибка: %s" % str(e))