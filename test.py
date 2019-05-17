import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


print(myclient.database_names())
mydb = myclient['local']

mycol = mydb['logined']

mydata = {"name":"John Doe", "password":"Doe"}

x = mycol.insert_one(mydata)
