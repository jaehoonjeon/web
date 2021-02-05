# 1. install MSSQL DB 모듈
# pip install pymssql 
# http://www.pymssql.org/pymssql_examples.html#basic-features-strict-db-api-compliance

import pymssql
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

# connection
def getConnection():
    conn = pymssql.connect(host=db.HOST, user=db.USER, password=db.PW, database=db.DB, charset='utf8')
    return conn

# get data from DB (query)
def get_data_query(query):
    returnData = []
    try:
        conn = getConnection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(query)
        for row in cursor:
            returnData.append(row)
        
        return returnData
    except Exception as e:
        print("Exception :: {}".format(e))
    finally:
        cursor.close()
        conn.close()

# query = ' select top 5 Port, PortID, PortEng, Note FROM Port '
query = """
    exec up_FastPreSale_Get_PortList @CompanyID = 'ONG1', @Method = '', @PortID = '', @PortSubID = '', @Search = ''
"""

listData = get_data_query(query)
listPort = []
for obj in listData:
    listPort.append(Port(obj))
printData = 'get data from db using query\n'
for obj in listPort:
    printData = printData + getKor(obj.Port)  + ',' + obj.PortID + '\t'

print(printData + '\n\n\n')




# get data from DB (sp)
def get_data_sp(sp_name, sp_args):
    returnData = []
    try:
        conn = getConnection()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc(sp_name, sp_args)
        for row in cursor:
            returnData.append(row)

        return returnData
    except Exception as e:
        print("Exception :: {}".format(e))
    finally:
        cursor.close()
        conn.close()

# issue :: 빈칸이 null로 전송됨 , SET @CompanyID  = ISNULL(@CompanyID, '')
# issue :: 파라미터 전송시 파라미터명 명명할 수 없음
listData = get_data_sp('up_App_Get_PortList', ('INTZ',))
listPort = []

if type(listData) == list:
    for obj in listData:
        listPort.append(Port(obj))
    printData = 'get data from db using stored procedure\n'
    for obj in listPort:
        printData = printData + getKor(obj.Port) + ',' + obj.PortID + '\t'

    print(printData)
else:
    print("has no data")