from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["autogen_db"]
collection = db["chat_memory"]

def save_message(session_id, agent_name, role, content):
    collection.insert_one({
        "session_id": session_id,
        "agent": agent_name,
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow()
    })

def load_session(session_id):
    return list(collection.find(
        {"session_id": session_id},
        {"_id": 0}
    ))
