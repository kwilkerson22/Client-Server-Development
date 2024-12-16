from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection variables for Kenneth Wilkerson's
        # instance of MongoDB
        #
        # Connection Variables
        #
        USER = username # created username for MongoDB
        PASS = password # created password for MongoDB
        HOST = 'nv-desktop-services.apporto.com' # MongoDB host address
        PORT = 31894 # MongoDB port number
        DB = 'AAC' # database name
        COL = 'animals' # collection name
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)] # access database
        self.collection = self.database['%s' % (COL)] # access collection

# Create method (CRUD)
    def create(self, data):
        """
        Insert a new document into the collection.
        :param data: Dictionary containing data to be inserted.
        :return: True if the insertion was successful, False otherwise.
        """
        try:  
            entry = self.database.animals.insert_one(data) # attempt to insert document into collection
            # check if operation was acknowledged
            if entry.acknowledged:
                return True # success 
            else:
                return False # failure
            
        except Exception as e:
            # handle exceptions and provide an error message
            print(f"Error inserting data {e}")
            return False
                       
# Read method (CRUD)
    def read(self, pair):
        """
        Query documents from the collection.
        :param pair: Dictionary containing query criteria.
        :return: Cursor object containing the query results.
        """
        try:
            query = self.collection.find(pair) # query the collection with the specified criteria
            return query # returns the results of the query
        
        except Exception as e:
            # handle exceptions and provide an error message
            print(f"Error querying documents: {e}")
            return [] # returns empty list if query is unsuccessful
        
# Update method (CRUD)    
    def update(self, pair, update_data, multiple=False):
        """
        Update documents in the collection.
        :param pair: Dictionary containing query criteria for the documents to be updated.
        :param update_data: Dictionary containing the fields and values to update.
        :param multiple: Boolean to determine whether to update one or multiple documents.
        :return: Number of documents updated.
        """
        try:
            if multiple:
                # update multiple documents that match the criteria using update_many
                result = self.collection.update_many(pair, {"$set": update_data}) 
                count = result.modified_count # number of documents modified
                return count 
            else:
                # update a single document that matches the criteria using update_one
                result = self.collection.update_one(pair, {"$set": update_data}) 
                count = result.modified_count # number of documents modified
                return count   
            
        except Exception as e:
            # handle exceptions and provide an error message
            print(f"Error updating documents: {e}")
            return 0 #Returns zero if the update fails
        
# Delete method (CRUD)    
    def delete(self, pair, multiple=False):
        """
        Delete documents from the collection.
        :param pair: Dictionary containing query criteria for the documents to be deleted.
        :param multiple: Boolean to determine whether to delete one or multiple documents.
        :return: Number of documents deleted.
        """
        try:
            if multiple:
                # delete multiple documents that match the criteria using delete_many
                result = self.collection.delete_many(pair) 
                count = result.deleted_count # number of documents deleted
                return count  

            else:
                # delete a single document that matches the criteria using delete_one
                result = self.collection.delete_one(pair) 
                count = result.deleted_count # number of documents deleted
                return count 
            
        except Exception as e:
            # handle exceptions and provide an error message
            print(f"Error deleting documents: {e}")
            return 0 #Returns zero if the delete operation fails
       
            
            
