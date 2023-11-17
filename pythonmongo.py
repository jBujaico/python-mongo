from pymongo.mongo_client import MongoClient

class Connection():

    def conection(self):

        uri = "mongodb+srv://admin:1234@cluster0.a06dch0.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        cluster = MongoClient(uri)

        # Send a ping to confirm a successful connection
        try:
            cluster.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        return cluster
    