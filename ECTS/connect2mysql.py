import pymysql
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
MYSQL_HOST = '124.71.19.9'
MYSQL_DBNAME = 'newbee_mall_db'
MYSQL_USER = 'zhu'
MYSQL_PASSWD = 'Zhu#cpss'
MYSQL_CHARSET = 'utf8'


class connect2mysql:

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


    def getfromnow(self):
    # 指定数据库模块名和数据库参数
        try:
            conn = pymysql.connect(**self.dbparms)
            cursor = conn.cursor()
        except Exception as e:
            print(e)
        sql = "SELECT cast(create_time as date ) as day_time , COUNT(distinct order_id) as day_count FROM tb_newbee_mall_order GROUP BY cast(create_time as date)  ORDER BY day_time DESC ;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()

            # day_time = cursor.fetchone()['day_time']
            now = datetime.now()
            foredate = []
            for i in reversed(range(30)):
                day = now - timedelta(days=i)
                day = day.strftime("%Y-%m-%d")
                # print(day, type(day))
                foredate.append(day)
            count = np.zeros(31)
            for item in result:
                if str(item['day_time']) not in foredate:
                    continue
                else:
                    count[foredate.index(str(item['day_time'])) + 1] = item['day_count']
            count = count.reshape(1, 31)
            res = pd.DataFrame(count).astype(int)
            res.to_csv('pred.txt', index=False)
        except Exception as e:
            print(e)
            print("销售数据获取错误")
        cursor.close()
        conn.close()

def run_connection():
    connection = connect2mysql()
    connection.getfromnow()