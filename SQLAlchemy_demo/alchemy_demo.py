import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# 當去調用declarative_base()這個方法 會返回一個BASE CLASS
# 也就是說declarative_base()像是工廠類 可以去創建BASE類
BASE = declarative_base()


# 對應數據庫裡面的table
# 讓User 去繼承BASE 這個類
class User(BASE):
    # 定義table的名稱
    __tablename__ = 'users'

    # 有 table了 再來就要定義欄位
    # 定義column的名稱, 形態, PK值, autuincrement, 默認值...

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # unique=True 表示唯一
    username = sa.Column(sa.String(64), unique=True)
    password = sa.Column(sa.String(64))
    email = sa.Column(sa.String(128), unique=True)
    # 注意 這裡傳入的是函數而不是函數值 所以不能加()
    # create_at = sa.Column(sa.DateTime, default=datetime.utcnow)

    # 這裡要改成sa.func.now()
    create_at = sa.Column(sa.DateTime, server_default=sa.func.now())

    # 只要傳入 username, password, email
    # ID, create_at 都會自動填入

    # 添加repr方法 返回的是print的結果
    def __repr__(self):
        return "id={}, username={}, email={}".format(self.id, self.username, self.email)


# 使用sa.create_engine設定數據庫的連接信息
engine = sa.create_engine('mysql+pymysql://root:00065638@localhost:3306/demo')
# 定義session 可以去連接數據庫 用來插入數據, 查詢數據
Session = sa.orm.sessionmaker(bind=engine)

# 通過調用Base裡面的metadata.create_all()方法把engine傳入去建立數據庫
# 會把BASE CLASS的子類(現在是user) 建立到數據庫裡面
BASE.metadata.create_all(engine)

# insert 數據 插入一個對象(User)的實例
# user1 = User(username='test1', password='test1', email='test1@test1.com')
# user2 = User(username='test2', password='test2', email='test2@test2.com')
# user3 = User(username='test3', password='test3', email='test3@test3.com')
#
# # 建立一個session
# session = Session()
# # 有了session後 就可以調用session.add()去插入數據
# # 插入單筆數據
# # session.add(user1)
# # 插入多筆數據
# session.add_all([user1, user2, user3])
# # 提交數據
# session.commit()

# s = Session()
# # 查詢數據
# users = s.query(User)
# # print(users)
# # SELECT users.id AS users_id, users.username AS users_username, users.password AS users_password, users.email AS users_email, users.create_at AS users_create_at
# # FROM users
# for u in users:
#     print(u)

# ## filter()過濾數據
# 這時候的filter 相當於where 再用users來迭代
# s = Session()
# users = s.query(User).filter(User.username == 'test1')
# # print(users)
# for u in users:
#     print(u)

# 排序 order_by desc是降序
# s = Session()
# users = s.query(User).order_by(User.id.desc())
# for u in users:
#     print(u)

# query().all() 用list返回迭代後的值
# 會一次性印出全部的數據 有可能塞爆記憶體

# s = Session()
# users = s.query(User).all()
# print(users)

# 只跑出第一筆數據query().first()
# s = Session()
# users = s.query(User).first()
# print(users)

# 可以用來判斷數據是否存在query().first()
# s = Session()
# users = s.query(User).filter(User.username == 'test1').first()
# print(users)

# 在需要驗證用戶名是否存在 也可以這樣寫
# if users:
#     print('用戶名已存在')
# else:
#     print('用戶名可以使用')

# query().limit() 只取前n筆數據
# s = Session()
# users = s.query(User).limit(2)
# for u in users:
#     print(u)


# filter 過濾條件的寫法
# query.filter(User.name.in_([’test1’, ‘test2’…]))
# s = Session()
# users = s.query(User).filter(User.username.in_(['test1', 'test2']))
# for u in users:
#     print(u)

# s = Session()
# users = s.query(User).filter(User.username.like("%es%"))
# for u in users:
#     print(u)

s = Session()

# SELECT id, username FROM user
u1 = s.query(User)
for u in u1:
    print(u, type(u))
# 可以看出上下兩者的區別
# id=1, username=test1, email=test1@test1.com <class '__main__.User'>


p2 = s.query(User.id, User.username)
for u in p2:
    print(u, type(u))
    # (1, 'test1') <class 'sqlalchemy.engine.row.Row'>