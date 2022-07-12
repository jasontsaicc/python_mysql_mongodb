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


# 使用sa.create_engine設定數據庫的連接信息
engine = sa.create_engine('mysql+pymysql://root:00065638@localhost:3306/demo')
# 定義session 可以去連接數據庫 用來插入數據, 查詢數據
Session = sa.orm.sessionmaker(bind=engine)

# 通過調用Base裡面的metadata.create_all()方法把engine傳入去建立數據庫
# 會把BASE CLASS的子類(現在是user) 建立到數據庫裡面
BASE.metadata.create_all(engine)

# insert 數據 插入一個對象(User)的實例
user1 = User(username='test1', password='test1', email='test1@test1.com')
user2 = User(username='test2', password='test2', email='test2@test1.com')
user3 = User(username='test3', password='test3', email='test3@test1.com')

# 建立一個session
session = Session()
# 有了session後 就可以調用session.add()去插入數據

# 插入單筆數據
# session.add(user1)

# 插入多筆數據
session.add_all([user1, user2, user3])

# 提交數據
session.commit()