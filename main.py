from pythonmongo import Connection

connection = Connection()

cluster = connection.conection()

db = cluster["base"]
collection = db["alumnos"]
post = {"id" : 1, "nombre": "admin", "pass": "pass"}

#insertar una colección
collection.insert_one(post)

results = collection.find({"id":1})
for result in results:
    print(result["nombre"])