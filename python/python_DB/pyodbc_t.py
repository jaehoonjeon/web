# 1. install MSSQL DB 모듈
# pip install pyodbc 
# ojdbc 드라이버 설치해야함
# https://docs.microsoft.com/ko-kr/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

import pyodbc
import dbConfig as db

# make class
class Port:
    Port = None
    PortID = None

    def __init__(self, dictionary):
        if type(dictionary) == dict:
            for k, v in dictionary.items():
                if hasattr(self, k): 
                    setattr(self, k, v)
    
    def __str__(self):
        return 'Port : {} PortID : {}'.format(str(self.Port), str(self.PortID))

# euc-kr
def getKor(obj):
    if type(obj) == str:
        return (obj.encode('ISO-8859-1')).decode('euc-kr')
    return obj


def getConnection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db.HOST+';DATABASE='+db.DB+';UID='+db.USER+';PWD='+ db.PW)
    return conn

try:
    conn = getConnection()
    cursor = conn.cursor()
    # cursor.execute(" SELECT TOP 10 Port, PortID, PortSubID, PortEng FROM Port ")
    query = """
        exec up_FastPreSale_Get_PortList @CompanyID = 'ONG1', @Method = '', @PortID = '', @PortSubID = '', @Search = ''
    """
    cursor.execute(query)

    rows = cursor.fetchone()
    for row in rows:
        print(row)
except Exception as e:
    print('Exception :: {}'.format(e))
finally:
    cursor.close()
    conn.close()
    