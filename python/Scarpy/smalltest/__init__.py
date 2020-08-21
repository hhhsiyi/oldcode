import pymongo


def db():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    # db1 = client['test1']
    # collection1 = db1['test1-collection']
    # dblist = client.list_database_names()
    # if "test1" in dblist:
    #     print("数据库已经存在")
    # # data = {
    # #     'id':132,
    # #     'name':'seee',
    # #     #'id':123,
    # #     'male':'man',
    # #     'size':'big'
    # # }
    # # result = collection1.insert(data)
    # # data_list = [{"_id":"test{}".format(i),"name":"test{}".format(i)}for i in range(10)]
    # # result = collection1.insert({"id":123,"name":"何文","male":"man"})
    # # collection1.insert(data_list)
    # # if result:
    # #     print("插入成功")
    # ret = collection1.find({"name":"何文"})
    # print(ret)
    # print(list(ret))
    # for i in ret:
    #     print(ret)
    db2 = client['test2']
    collection2 = db2['test2-collection']
    if "test2" in client.list_database_names():
        print("数据表已经存在")

    # data_list = [{"_id":"{}".format(i),"name":"py{}".format(i)}for i in range(1000)]
    # collection2.insert(data_list)

    ret = collection2.find()
    # print(list(ret))
    data_list = list(ret)
    #data_list = [i for i in data_list if i['_id'] % 100 == 0]
    #print(data_list)
    # for i in getall:
    #     print(i)
    data_list = [i for i in data_list if int(i["_id"])%100==0]
    print(data_list)

if __name__ == '__main__':
    db()
