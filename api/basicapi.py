#coding=gbk
__author__ = 'pw.guo'
import pymysql
class BasicApi:


    def __init__(self,userName):
        self.__userName=userName
        try:
              self._db = pymysql.connect(host='127.0.0.1',port=3306, user=self.__userName, passwd = "root" , db='funddata', charset='utf8')
              self._cursor =  self._db.cursor()
        except pymysql.err.OperationalError:
            print("数据连接错误！")

    def __del__(self):
        self._cursor.close()
        self._db.close()


    def stock_basic(self,exchange="", list_status="",ts_code="", fields=""):
        try:

            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from stockBasic where 1=1"
            if  list_status.strip():
                 sql=sql +" and list_status='"+list_status+"'"
            if  exchange.strip():
                 sql=sql +" and exchange='"+exchange+"'"
            if  ts_code.strip():
                 sql=sql +" and ts_code='"+ts_code+"'"
            print(sql)
            self._cursor.execute(sql)
            results = self._cursor.fetchall()
            return results;
        except pymysql.err.OperationalError:
            print("数据连接错误！")
        except Exception as err:
            print(err )
        return []

    def daily(self,start_date="", end_date="",ts_code="", fields=""):

        try:

            if  not fields.strip():
                fields="*"
            sql="select "+ fields+\
                " from daily where 1=1"
            if  start_date.strip():
                 sql=sql +" and trade_date>='"+start_date+"'"
            if  end_date.strip():
                 sql=sql +" and trade_date<='"+end_date+"'"
            if  ts_code.strip():
                 sql=sql +" and ts_code='"+ts_code+"'"
            print(sql)
            self._cursor.execute(sql)
            results = self._cursor.fetchall()
            return results;
        except pymysql.err.OperationalError:
            print("数据连接错误！")
        except Exception as err:
            print(err )
        return []