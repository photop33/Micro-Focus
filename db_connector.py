import pymysql
import datetime
from flask import request
from Backend_test import test



def Create_Table():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='AFKTvDpMGV', passwd='MXSpb3808w', db='AFKTvDpMGV')
    cursor = conn.cursor()
    conn.autocommit(True)
    name_table = "user"
    cursor.execute(
        "CREATE TABLE `AFKTvDpMGV`.`" + name_table + "` (`ID` INT UNSIGNED NOT NULL,`name` VARCHAR(50) NOT NULL,`time_column_datetime` VARCHAR(50) NOT NULL)")
    print("Ready table " + name_table + "")
    cursor.close()
    conn.close()


def get_users(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='oPWyaB1d82', db='xiDsE9WxzQ')
    cursor = conn.cursor()
    conn.autocommit(True)
    x = cursor.execute("SELECT * FROM xiDsE9WxzQ.users;")
    result = cursor.fetchall()
    for row in result:
        show2= str(row[0])
        if show2 == user_id:
            user_name = row[1]
            print(row,"success get_users")
            return user_name
        else:
            print(show2,'Fail get_user')
    cursor.close()
    conn.close()

users = {}


def insert_user(user_id) :
    user_name = test()
    print(user_name,user_id)
    # user_name = request_data.get('user_name')
    # users[user_id] = user_name
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='oPWyaB1d82', db='xiDsE9WxzQ')
    conn.autocommit(True)
    # request_data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO xiDsE9WxzQ.users (name, user_id ) VALUES (%s,%s)", (user_name, user_id))
    cursor.close()
    conn.close()
    print("success insert_user")
    return user_name



users = {}


def update_user(user_id):
    request_data = request.json
    request_data.get('user_name')
    user_name = request_data.get('user_name')
    users[user_id] = user_name
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='oPWyaB1d82', db='xiDsE9WxzQ')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE xiDsE9WxzQ.users SET name = '" + user_name + "'  WHERE user_id=" + user_id + "")
    cursor.close()
    conn.close()
    print("success update_user")

    return user_name


def delete_user(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='xiDsE9WxzQ', passwd='oPWyaB1d82', db='xiDsE9WxzQ')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AFKTvDpMGV.users;")
    result = cursor.fetchall()
    for row in result:
        show = str(row[0])
        if show == user_id:
            print(row[1])
            user_name = row[1]
    cursor.execute("DELETE FROM xiDsE9WxzQ.users WHERE user_id = " + user_id + "")
    cursor.close()
    conn.close()
    print("success delete_user")
    return user_name
