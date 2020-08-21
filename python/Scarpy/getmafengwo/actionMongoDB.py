import pymongo


class Mongo(object):

    def __init__(self):
        #初始化
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.collection = self.client['mafengwo_test']['city']


    def save(self,datas):#保存数据
        self.collection.save(datas)

    def find_city_count(self,city):
        #获取景点城市数量
        return self.collection.count({'city':city})

    def find_city(self,city_name,count=20):
        #
        c = self.collection.find({'address':{'$regex':city_name}},limit = count).\
                sort([('comments',pymongo.DESCENDING)])#倒序排
        se = []
        for s in c:
            se.append(s)
        return se



mongo = Mongo()