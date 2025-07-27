from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBPzrnIAvg4rRMUQunBQYNm8Rd31D44xdA")
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://15977628.databases.neo4j.io")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "baFds01UoVD93dwOOAhZPWEziFhjXfq9NVz0YtMtq9A")
