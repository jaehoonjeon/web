import sqlite3

class Port:
    Port = None
    PortID = None

    def __init__(self, dictionary):
        if type(dictionary) == dict:
            for k, v in dictionary.items():
                if hasattr(self, k): 
                    setattr(self, k, v)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getData(query):
    returnData = []
    try:
        conn = sqlite3.connect('Ticket30DB.db')
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute(query)
        
        returnData = []
        for row in cursor:
            returnData.append(Port(row))
        return returnData
            
    except Exception as e:
        print('Exception :: {}'.format(e))
    finally:
        cursor.close()
        conn.close()


query = ' SELECT * FROM Port Limit 10 '
returnData = getData(query)
printData = ''
for obj in returnData:
    printData = printData + obj.Port  + ',' + obj.PortID + '\t'

print(printData + '\n\n\n')