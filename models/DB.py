from pymongo import MongoClient
import os

class DB:
    def __init__(self) -> None:
        self.connection = None
        # do not forget to change the connection string after creating the cluster
        self.url = f"mongodb+srv://{os.environ.get('user_name')}:{os.environ.get('password')}@myatlasclusteredu.fz1s1hm.mongodb.net/?retryWrites=true&w=majority"
    def get_all_questions(self):
        try:
            client = MongoClient(self.url)
            questions_coll = client.PyTestApp.questions
            data = list(questions_coll.find())
            return data
        except Exception as e:
            print(e)
            return None
    def get_answers(self):
        try:
            client = MongoClient(self.url)
            questions_coll = client.PyTestApp.questions
            data = list(questions_coll.find({}))
            return data
        except Exception as e:
            print(e)
            return None   
