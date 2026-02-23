import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timezone
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Load Environment Variables
load_dotenv()

app = FastAPI(title="Study Bot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Database Setup
MONGO_URI = os.getenv("MONGODB_URI")
try:
    client = MongoClient(MONGO_URI)
    db = client["study_bot_db"]
    collection = db["chats"]
except Exception as e:
    print(f"MongoDB Error: {e}")

# LLM Setup
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI Study Assistant. Help the student with academic questions."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | llm

class ChatRequest(BaseModel):
    user_id: str
    question: str

def get_history(user_id: str):
    chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []
    for chat in chats:
        if chat["role"] == "human":
            history.append(HumanMessage(content=chat["message"]))
        elif chat["role"] == "ai":
            history.append(AIMessage(content=chat["message"]))
    return history[-10:]

@app.get("/")
def home():
    return {"message": "Welcome to the Study Bot API!"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        chat_history = get_history(request.user_id)
        
        response = chain.invoke({
            "history": chat_history,
            "question": request.question
        })
        
        collection.insert_one({
            "user_id": request.user_id,
            "role": "human",
            "message": request.question,
            "timestamp": datetime.now(timezone.utc)
        })
        
        collection.insert_one({
            "user_id": request.user_id,
            "role": "ai",
            "message": response.content,
            "timestamp": datetime.now(timezone.utc)
        })
        
        return {"response": response.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
