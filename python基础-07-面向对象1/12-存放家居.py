class Home:
    def __init__(self,new_area,new_info,new_addf):
        self.area = new_area
        self.info = new_info
        self.addr = new_addf
        self.left_area = new_area
        self.contain = []
    
    def __str__(self):
        msg = "房子的面积有:%d,房子的户型是：%s,房子所在的位置:%s"%(self.area,self.info,self.addr)
        
        msg += "房子的剩余面积:%d,房子已搬进的物品有:%s"%(self.left_area,str(self.contain))        
        
        return msg

    def add_item(self,item):
        self.left_area = self.left_area - item.get_area()
        self.contain.append(item.get_name())  


class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "床的名字是：%s,床的面积是:%d"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

fangzi = Home(120,"三室一厅","湖南省 长沙市 岳麓区 白鹤家园")
print(fangzi)

bed1 = Bed("席梦思",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)
