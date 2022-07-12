import sqlalchemy as sa
from datetime import datetime

# 對應數據庫裡面的table
class User:
    # 定義table的名稱
    __tablename__ = 'users'

    # 有 table了 再來就要定義欄位
    # 定義column的名稱, 形態, PK值, autuincrement, 默認值...

    id = sa.Column(sa.Integer, primary_key=True, autuincrement=True)
    # unique=True 表示唯一
    username = sa.Column(sa.String(64), unique=True)
    password = sa.Column(sa.String(64))
    email = sa.Column(sa.String(128), unique=True)
    # 注意 這裡傳入的是函數而不是函數值 所以不能加()
    create_at = sa.Column(sa.DateTime, default=datetime.now)
    # 只要傳入 username, password, email
    # ID, create_at 都會自動填入


