import pymongo

client = pymongo.MongoClient("mongodb+srv://markkvu4:12345@cluster0.niyzzif.mongodb.net/?retryWrites=true&w=majority")

db = client['test']
col = db["test"]

obj = {
  "name":"Mark",
  "age":13,
  "info":"Boy"
}
x = col.insert_one({"test":"My test data"})