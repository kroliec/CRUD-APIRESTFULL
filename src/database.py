from pymongo import MongoClient
import certifi

MONGO_URI='mongodb+srv://shadow:sololeveling@clustersockets.7tvakqr.mongodb.net/'
ca=certifi.where()

def dbConnection():
    try:
        client=MongoClient(MONGO_URI, tlsCAFile=ca)
        db=client["db_crud"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db