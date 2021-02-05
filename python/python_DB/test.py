
# 객체에 있는 변수에만 값을 넣기

class Port:
    PortID = None
    Port = None
    Note = None
    Seq = None

    def __init__(self):
        self.PortID = None
        self.Port = None
        self.Note = None        
        self.Seq = None

    def __init__(self, dictionary):
        if type(dictionary) == str:
            self.PortID = dictionary
        elif type(dictionary) == dict:
            for k, v in dictionary.items():
                # 현재 클래스에 k(변수) 가 있으면 k에 값넣기
                if hasattr(self, k): 
                    setattr(self, k, v)


dic = {
    "PortID" : "1009",
    "Port" : "제주",
    "PortEng" : "jeju", 
    "Seq" : 1,
}
dic2 = {
    "PortID" : "1010",
    "Port" : "인천",
    "PortEng" : "incheon",
    "Seq" : 2,
}

p = Port(dic)
print('{} {} {} {}'.format(p.PortID, p.Port, p.Note, p.Seq))
p = Port(dic2)
print('{} {} {} {}'.format(p.PortID, p.Port, p.Note, str(p.Seq)))


