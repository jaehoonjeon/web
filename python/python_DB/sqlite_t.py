import sqlite3

class Port:
    Port = None
    PortID = None

    def __init__(self, dictionary):
        if type(dictionary) == dict:
            for k, v in dictionary.items():
                if hasattr(self, k): 
                    setattr(self, k, v)

def getKor(obj):
    if type(obj) == str:
        return (obj.encode('ISO-8859-1')).decode('euc-kr')
    return obj

def getData(query):
    returnData = []
    try:
        conn = sqlite3.connect('Ticket30DB.db')
        cursor = conn.cursor()
        cursor.execute(query)
        for row in cursor:
            print(row)

        #for row in cursor:
            #returnData.append(row)

        #return returnData
    except Exception as e:
        print('Exception :: {}'.format(e))
    finally:
        cursor.close()
        conn.close()


query = ' SELECT * FROM Port Limit 10 '
returnData = getData(query)
