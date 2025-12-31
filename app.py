"""
Career Digital Twin - Python Backend with OpenAI SDK
A Flask API that serves the chatbot with RAG capabilities
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
from knowledge_base import KNOWLEDGE_BASE

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
    'MODEL': 'meta-llama/llama-3.1-8b-instruct:free',  # FREE model from OpenRouter!
    'MAX_TOKENS': 250,
    'TEMPERATURE': 0.7
}

# System prompt with RAG
SYSTEM_PROMPT = f"""You are Rithik Sharon A's AI-powered Digital Twin. Use the following comprehensive knowledge base to answer questions accurately, professionally, and conversationally.

KNOWLEDGE BASE:
{KNOWLEDGE_BASE}

GUIDELINES:
- Answer based on the knowledge base provided
- Be friendly, professional, and conversational
- Keep responses concise but informative (2-4 sentences typically)
- If asked something not in the knowledge base, politely suggest contacting Rithik directly
- Include relevant links when mentioning contact info or projects
- Show enthusiasm about Rithik's skills and accomplishments
- Be honest and authentic
- If unsure, recommend reaching out directly rather than making up information"""


def get_fallback_response(message):
    """Fallback responses when API is unavailable"""
    msg = message.lower()
    
    if 'skill' in msg or 'technology' in msg or 'tech stack' in msg:
        return "Rithik is a MERN Stack Developer specializing in React, Node.js, Express, and MongoDB. He also has expertise in Agentic AI and OpenAI APIs, combining full-stack development with cutting-edge AI integration!"
    
    if 'project' in msg:
        return "Rithik has built several exciting projects including a modern Portfolio Website, this Career Digital Twin using AI, and various AI-powered applications. Check out his GitHub at github.com/Rithik-Sharon-A to see more!"
    
    if 'ai' in msg or 'artificial intelligence' in msg or 'openai' in msg:
        return "Rithik specializes in Agentic AI and OpenAI APIs! He uses these technologies to automate complex workflows, build intelligent chatbots, and create AI-powered web applications that enhance user experiences."
    
    if 'experience' in msg or 'work' in msg or 'background' in msg:
        return "Rithik is a MERN Stack Developer with strong expertise in building scalable, responsive web applications. He specializes in integrating Agentic AI and OpenAI APIs to create intelligent, automated solutions."
    
    if 'contact' in msg or 'email' in msg or 'reach' in msg or 'hire' in msg:
        return "You can reach Rithik at rithiksharon.a@gmail.com (he usually responds within 24-48 hours) or connect on LinkedIn at linkedin.com/in/rithik-sharon/. He's open to full-time opportunities and freelance projects!"
    
    if 'available' in msg or 'looking for work' in msg:
        return "Yes! Rithik is open to exciting opportunities including full-time positions, freelance projects, and collaborations. Feel free to reach out at rithiksharon.a@gmail.com to discuss opportunities."
    
    if 'resume' in msg or 'cv' in msg:
        return "You can download Rithik's resume from his portfolio website. It contains detailed information about his education, experience, skills, and projects. Visit his portfolio or email him directly at rithiksharon.a@gmail.com!"
    
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
        print("⚠️  WARNING: OPENROUTER_API_KEY not found in .env file")
        print("The chatbot will use fallback responses")
    else:
        print("✅ OpenRouter API key loaded successfully")
    
    # Use PORT from environment for production (Render, etc.) or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    print(f"🤖 Career Digital Twin API")
    print(f"📊 Using FREE model: {CONFIG['MODEL']} via OpenRouter")
    print(f"💰 Cost: $0.00 - Completely FREE!")
    print(f"🌐 Running on http://0.0.0.0:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=False)

