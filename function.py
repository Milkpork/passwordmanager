import pymysql.cursors


def mainUI():
    print("--------------------")
    print("1 ----------- insert")
    print("2 ----------- update")
    print("3 ----------- output")
    print("4 ----------- delete")



def insert(cursor):
    try:
        print("please input the platform")
        platform = input()
        print("please input the user_name")
        user_name = input()
        print("please input the password:")
        password = input()
        print("please input the addition:")
        addition = input()
        sql = f'INSERT INTO pw' \
              f'(platform, user_name, user_password, addition)' \
              f'VALUES' \
              f'("{platform}", "{user_name}", "{password}", "{addition}");'
        cursor.execute(sql)
        print("success")
    except:
        print("error")


def update(cursor):
    # print("input the mode(1:vague/2:accurate)")
    mode = "2"
    if mode == "2":
        try:
            print("please input the user_name")
            user_name = input()
            print("please input the password:")
            password = input()
            sql = f'update pw set user_password="{password}" where user_name="{user_name}"'
            cursor.execute(sql)
            print("success")
        except:
            print("error")
    elif mode == "1":
        # 模糊查询功能未实现
        try:
            print("please input the user_name")
            user_name = input()
            print("please input the password:")
            password = input()
            sql = f'update pw set user_password="{password}" where user_name REGEXP "%{user_name}%"'
            cursor.execute(sql)
            print("success")
        except:
            print("error")
    else:
        print("error input")
        return


def select(cursor):
    print("{:10} {:10} {:10}".format("name", "password", "addition"))
    sql = "select * from pw"
    cursor.execute(sql)
    ls = cursor.fetchall()
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            print("{:10}".format(ls[i][j]), end=' ')
        print()

def delete(cursor):
    print("the name you want to delete")
    name = input()
    sql = f'delete from pw where user_name = "{name}"'
    cursor.execute(sql)
    print("success")

def main():
    print("please input the password")
    pw = input()
    try:
        connect = pymysql.Connect(host='localhost', port=3306, user='root', password=pw, database='passwords',
                                  charset='utf8')
    except pymysql.err.OperationalError:
        print("password error")
        exit(0)
    cursor = connect.cursor()  # 执行完毕返回的结果集默认以元组显示
    while True:
        mainUI()
        order = input()
        if order == "1":
            insert(cursor)
            connect.commit()
        elif order == "2":
            update(cursor)
            connect.commit()
        elif order == "3":
            select(cursor)
            connect.commit()
        elif order == "4":
            delete(cursor)
            connect.commit()
        else:
            break
    cursor.close()
    connect.close()


if __name__ == '__main__':
    main()
