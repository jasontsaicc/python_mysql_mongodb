import pymysql

# 連接資料庫
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='demo'
)
# 類似在終端機輸入mysql命令
cursor = connection.cursor()

# table create
sql = "CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))"

# 通過cursor.execute()執行sql語句
cursor.execute(sql)
# 通過connection.commit()提交 像是按enrter鍵
connection.commit()

# insert data into table
# %s 占位符 可以放入任意值 後面再放入值
sql = "INSERT INTO users(username, password) VALUES (%s, %s)"

# ('user1', 'password1') 這就是上面的%s 占位符
cursor.execute(sql, ('user1', 'password1'))
cursor.execute(sql, ('user2', 'password2'))
cursor.execute(sql, ('user3', 'password3'))
# 提交
connection.commit()

# select data 也可以在加where.... order,,
sql = "SELECT id, username from users"
cursor.execute(sql)

# 取得結果
# 因為是select 所以會回傳一個數據tuple 需要接收
# fetchall() 取得所有資料 (不建議使用)
results = cursor.fetchall()
print(results)

# 取得資料可以用 fetchall() 跟 fetchone() 但是 一般都是用fetchone()
# fetchone() 取得一筆資料 才不會一次傳入幾千幾萬筆資料 塞爆電腦

while True:
    # 取得一筆資料
    result = cursor.fetchone()
    # 如果沒有資料就跳出迴圈 注意這裡使用None
    if result is None:
        break
    print(result)

# # update
sql = "update users set password=%s where username=%s"
cursor.execute(sql, ('password1111', 'user1'))
connection.commit()
#
# # delete
sql = 'DELETE from users where id=%s'
cursor.execute(sql, (2,))
connection.commit()

# 關掉文件 像是open()的close()
connection.close()
