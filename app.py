"""
Career Digital Twin - Python Backend with OpenAI SDK
A Flask API that serves the chatbot with RAG capabilities
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
from knowledge_base import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize OpenAI client with OpenRouter
client = OpenAI(
    api_key=os.getenv('OPENROUTER_API_KEY'),
    base_url="https://openrouter.ai/api/v1"
)

# Configuration
CONFIG = {
    'MODEL': os.getenv('OPENROUTER_MODEL', 'mistralai/mistral-7b-instruct:free'),  # default free model
    'MAX_TOKENS': 250,
    'TEMPERATURE': 0.7
}

def get_fallback_response(message):
    """Fallback responses when API is unavailable"""
    msg = message.lower()
    
    if 'skill' in msg or 'technology' in msg or 'tech stack' in msg:
        return "Rithik Sharon A is a fresher MERN Stack Developer based in Chennai, Tamil Nadu, India. His skills include React.js, Node.js, Express.js, MongoDB, and JavaScript (ES6+)."
    
    if 'project' in msg:
        return "Rithik has project-based experience. Notable projects include an Agentic AI Digital Twin (integrated into a MERN-based portfolio) and a MERN E-commerce Platform."
    
    if 'ai' in msg or 'artificial intelligence' in msg or 'openai' in msg:
        return "Rithik works on Agentic AI, prompt engineering, autonomous agents, and OpenAI API integration (project-based)."
    
    if 'experience' in msg or 'work' in msg or 'background' in msg:
        return "Rithik Sharon A is a fresher MERN Stack Developer based in Chennai, Tamil Nadu, India. His skills include React.js, Node.js, Express.js, MongoDB, and JavaScript (ES6+)."
    
    if 'contact' in msg or 'email' in msg or 'reach' in msg or 'hire' in msg:
        return "You can reach Rithik at rithiksharon.a@gmail.com. GitHub: github.com/Rithik-Sharon-A. LinkedIn: linkedin.com/in/rithik-sharon/."
    
    if 'available' in msg or 'looking for work' in msg:
        return "The knowledge base does not specify availability details. You can contact Rithik at rithiksharon.a@gmail.com."
    
    if 'resume' in msg or 'cv' in msg:
        return "Resume download information is not available in the knowledge base. You can contact Rithik at rithiksharon.a@gmail.com."
    
    if 'github' in msg or 'code' in msg:
        return "Check out Rithik's GitHub at github.com/Rithik-Sharon-A to see his projects and code. He has several full-stack MERN applications and AI-powered projects showcased there!"
    
    return "That's a great question! I'm Rithik's Digital Twin powered by AI. Feel free to ask me about his skills, projects, experience with AI, or how to contact him. What would you like to know?"


@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Check if API key is configured
        if not os.getenv('OPENROUTER_API_KEY'):
            return jsonify({
                'response': get_fallback_response(user_message),
                'source': 'fallback'
            })
        
        # Call OpenRouter API with RAG (using OpenAI SDK)
        response = client.chat.completions.create(
            model=CONFIG['MODEL'],
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_message}
            ],
            max_tokens=CONFIG['MAX_TOKENS'],
            temperature=CONFIG['TEMPERATURE'],
            extra_headers={
                "HTTP-Referer": "https://github.com/Rithik-Sharon-A/career-digital-twin-",
                "X-Title": "Career Digital Twin - Rithik Sharon A"
            }
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({
            'response': ai_response,
            'source': 'openai',
            'model': CONFIG['MODEL']
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'response': get_fallback_response(user_message),
            'source': 'fallback',
            'error': str(e)
        })


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model': CONFIG['MODEL'],
        'api_configured': bool(os.getenv('OPENROUTER_API_KEY'))
    })


@app.route('/')
def home():
    """Home route"""
    return jsonify({
        'message': 'Career Digital Twin API',
        'version': '1.0.0',
        'endpoints': {
            'chat': '/api/chat (POST)',
            'health': '/api/health (GET)'
        }
    })


if __name__ == '__main__':
    # Check for API key
    if not os.getenv('OPENROUTER_API_KEY'):
        print('WARNING: OPENROUTER_API_KEY not found (set it in Render env vars or local .env)')
        print('The chatbot will use fallback responses')
    else:
        print('OpenRouter API key loaded successfully')

    # Use PORT from environment for production (Render, etc.) or default to 5000
    port = int(os.getenv('PORT', 5000))

    print('Career Digital Twin API')
    print(f'Using model: {CONFIG["MODEL"]} via OpenRouter')
    print(f'Listening on: http://0.0.0.0:{port}')

    app.run(host='0.0.0.0', port=port, debug=False)
