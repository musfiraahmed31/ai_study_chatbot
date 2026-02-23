Study Bot: AI-Powered Study Assistant API
An intelligent, context-aware RESTful API built to act as a virtual study assistant. This project demonstrates the integration of Large Language Models (LLMs) with a persistent NoSQL database to create a chatbot that remembers past conversations and provides highly relevant, academic-focused answers.

🚀 Features
Conversational Memory: Utilizes MongoDB to store and retrieve user-specific chat histories, allowing the AI to maintain context across multiple interactions.

Academic Persona: Powered by a carefully crafted system prompt that restricts the AI to focus on educational and learning-related topics.

High-Performance Backend: Built with FastAPI for lightning-fast request handling and automatic API documentation generation.

LLM Orchestration: Uses LangChain to seamlessly bridge the gap between the database history and the Groq LLM inference engine.

🛠️ Tech Stack
Language: Python 3.11+

Framework: FastAPI, Uvicorn

AI & LLM: LangChain, Groq API (mixtral-8x7b-32768)

Database: MongoDB Atlas (PyMongo)

Deployment: Render

⚙️ Local Setup & Installation
1. Clone the Repository
Bash
git clone https://github.com/yourusername/study-bot-project.git
cd study-bot-project
2. Create a Virtual Environment
Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your unique API keys and connection strings:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
MONGODB_URI=your_mongodb_connection_string_here
PYTHON_VERSION=3.11.9
5. Run the Server
Bash
uvicorn main:app --reload
The API will start locally at http://127.0.0.1:8000.

🌐 API Endpoints
GET /
Health check endpoint to verify the server is running.

Response: {"message": "Welcome to the Study Bot API! The server is running."}

POST /chat
The primary endpoint for interacting with the AI.

Request Body (JSON):

JSON
{
  "user_id": "student_123",
  "question": "Explain the concept of inheritance in Java."
}
Response: Returns the AI's generated, context-aware answer.

🧪 Testing the API
FastAPI provides an automatic, interactive Swagger UI. Once the local server is running, navigate to:
http://127.0.0.1:8000/docs to test the endpoints directly from your browser.

👨‍💻 Author
Musfira Ahmed Pak-Austria Fachhochschule (IAST) Haripur
