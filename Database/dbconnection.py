import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

try:
    connectionString = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    connectionString.admin.command("ping")  # fail fast if DB unreachable
except ConnectionFailure as e:
    raise RuntimeError(f"Could not connect to MongoDB: {e}")

DatabaseName = connectionString["SMS1"]
CollectionName = DatabaseName["AllStudents"]

# Ensure roll numbers are unique at the DB level
CollectionName.create_index("roll", unique=True)