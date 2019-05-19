import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


print(myclient.database_names())
mydb = myclient['local']

mycol = mydb['logined']

mydata = {"email":"vashie@yahoo.com", "password":"123"}

x = mycol.insert_one(mydata)

x=mycol.find_one(mydata)

print(x)