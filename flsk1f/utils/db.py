from dbutils.pooled_db import PooledDB
import  pymysql
POOL=PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    setsession=[],
    ping=0,
    host='localhost',user='root',passwd='11111111',db='xjgldm',charset='utf8'
)
def fetch_one(sql, params):
    