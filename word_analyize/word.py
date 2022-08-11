import json
import pymysql

MYSQL_HOST = '124.71.19.9'
MYSQL_DBNAME = 'newbee_mall_db'
MYSQL_USER = 'zhu'
MYSQL_PASSWD = 'Zhu#cpss'
MYSQL_CHARSET = 'utf8'


class connect2MySQL:

    dbparms = dict(
        host=MYSQL_HOST,
        db=MYSQL_DBNAME,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWD,
        charset=MYSQL_CHARSET,
        cursorclass=pymysql.cursors.DictCursor,
        use_unicode=True,
        autocommit=True,
    )
    def getTriplet(self, goods_id):
    # 指定数据库模块名和数据库参数
        try:
            conn = pymysql.connect(**self.dbparms)
            cursor = conn.cursor()
        except Exception as e:
            print(e)
        sql = "SELECT Triplet FROM tb_newbee_mall_comment WHERE goods_id = " + goods_id + ";"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)


c = connect2MySQL()
goods_id = "10930"
result = c.getTriplet(goods_id=goods_id)
for value in result:
    if value["Triplet"] != None and value["Triplet"] != "[]":

