from pymysql import connect
from pymysql.cursors import DictCursor

db = connect(
    host= 'finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_202112_python',
    charset='utf8',
    cursorclass=DictCursor
)