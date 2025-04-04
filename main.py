import os
import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Set OpenRouter API key (replace with your actual key)
OPENROUTER_API_KEY = "sk-or-v1"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# ✅ Research-Based Keywords
RESEARCH_KEYWORDS = [
    "research", "study", "academic", "experiment", "data analysis",
    "AI research", "scientific", "thesis", "hypothesis", "peer review"
]

class SubAgent:
    """A sub-agent that only handles research-related questions."""
    
    def __init__(self, role, model="mistralai/mistral-7b-instruct"):
        self.role = role
        self.model = model

    def is_research_query(self, query):
        """Check if the query is research-related."""
        return any(keyword in query.lower() for keyword in RESEARCH_KEYWORDS)

    def get_response(self, user_query):
        """Only answer research-related questions."""
        if not self.is_research_query(user_query):
            return f"❌ {self.role}: I only handle research-based questions."

        try:
            print(f"🟢 {self.role} processing research query...")

            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": self.model,
                "messages": [{"role": "user", "content": user_query}]
            }
            response = requests.post(API_URL, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"❌ API Error: {response.text}"
        
        except Exception as e:
            return f"❌ Error in {self.role}: {str(e)}"


class MasterAIAgent:
    """Master AI orchestrator that manages research-focused sub-agents."""
    
    def __init__(self):
        self.agents = {
            "Research_Assistant": SubAgent("Research_Assistant"),
            "Data_Analyzer": SubAgent("Data_Analyzer"),
            "Paper_Summarizer": SubAgent("Paper_Summarizer")
        }

    def get_responses(self, user_query):
        """Get responses from sub-agents if the query is research-based."""
        responses = {}

        for agent_name, agent in self.agents.items():
            response = agent.get_response(user_query)
            responses[agent_name] = response

        return responses

    def rank_responses(self, responses):
        """Rank responses using OpenRouter AI."""
        ranking_prompt = "Rank these research responses from best to worst:\n\n"
        for agent, response in responses.items():
            ranking_prompt += f"{agent}: {response}\n\n"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": ranking_prompt}]
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        print("hello",response)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ API Error in ranking: {response.text}"

    def respond(self, user_query):
        """Process the query, filter research topics, and rank responses."""
        print("\n🔵 Master Agent processing query...")

        if not any(keyword in user_query.lower() for keyword in RESEARCH_KEYWORDS):
            return "❌ This system only handles research-based queries."

        responses = self.get_responses(user_query)
        ranked_response = self.rank_responses(responses)

        print("✅ Response ranking complete!")
        return ranked_response


# Initialize AI Orchestrator
orchestrator = MasterAIAgent()


@app.route("/ask", methods=["POST"])
def ask_ai():
    """API Endpoint to interact with the AI agent."""
    data = request.get_json()
    print(data)
    if not data or "query" not in data:
        return jsonify({"error": "Invalid request. Please provide a 'query' field."}), 400

    user_query = data["query"]
    response = orchestrator.respond(user_query)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
