# The-Second-Mind

Research AI Assistant - README

Overview

This is a Flask-based AI-powered research assistant that processes research-related queries and generates responses using the OpenRouter AI API. The system consists of:
	1.	Sub-agents that specialize in different research tasks.
	2.	A Master AI Agent that orchestrates responses and ranks them.
	3.	An API Endpoint (/ask) to interact with the system.

The assistant strictly handles research-based queries and filters out non-research questions.

⸻

Features

 Handles Research-Based Queries – Only responds to research-related topics like AI research, scientific studies, academic analysis, and data processing.

 Multiple Sub-Agents – The AI system includes specialized sub-agents:
	•	Research_Assistant – General research queries.
	•	Data_Analyzer – Analyzes research-related data.
	•	Paper_Summarizer – Summarizes academic papers.

 AI-Powered Response Ranking – Uses OpenRouter AI to rank responses and provide the best answer.

Flask API with CORS Support – Designed for easy frontend integration.

⸻

Technology Stack
	•	Python – Programming language.
	•	Flask – Web framework for API development.
	•	Flask-CORS – Enables cross-origin requests.
	•	OpenRouter AI API – Processes research queries.
	•	requests – Handles API requests to OpenRouter.

⸻

Installation

1. Clone the Repository

git clone https://github.com/Niteshkris/The-Second-Mind/tree/main

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up OpenRouter API Key

Replace the API key in the code:

OPENROUTER_API_KEY = "your-api-key-here"

5. Run the Flask App

python app.py

The API will start at: http://127.0.0.1:5000

⸻

API Usage

Endpoint: /ask
	•	Method: POST
	•	Request Body:

{
    "query": "What is the impact of AI on scientific research?"
}


	•	Response:

{
    "response": "AI has revolutionized scientific research by automating data analysis, improving efficiency..."
}



⸻

Code Structure

research-ai-assistant/
│── index.html            #front end 
│── main.py               # Main Flask application
│── requirements.txt      # Dependencies
│── README.md            # Documentation



⸻

How It Works
	1.	Receives a Query:
	•	Users send a research-related question via the /ask endpoint.
	2.	Filters Non-Research Queries:
	•	If the query is not research-related, the system rejects it.
	3.	Generates Responses from Sub-Agents:
	•	The system calls different sub-agents to generate responses.
	4.	Ranks Responses:
	•	OpenRouter AI ranks the responses and returns the best answer.

⸻

Customization
	•	To add more research-related keywords, update the RESEARCH_KEYWORDS list:

RESEARCH_KEYWORDS = ["research", "study", "thesis", "scientific", "AI research"]


	•	To change AI models, modify the model parameter in SubAgent:

self.model = "mistralai/mistral-7b-instruct"



⸻

Future Improvements

 Add more sub-agents for specialized research topics.
 Improve ranking logic with AI-based response scoring.
 Enhance error handling for better stability.

⸻

