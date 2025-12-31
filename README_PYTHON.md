# 🤖 Career Digital Twin - Python + OpenAI SDK Version

An AI-powered digital twin chatbot built with **Python Flask backend** and **OpenAI SDK** for enhanced AI capabilities and better control.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=for-the-badge&logo=flask)
![OpenAI](https://img.shields.io/badge/OpenAI-SDK-green?style=for-the-badge&logo=openai)
![Status](https://img.shields.io/badge/Status-Live-4ade80?style=for-the-badge)

---

## 🌟 What's New in Python Version?

### **Why Python + OpenAI SDK?**

✅ **Official OpenAI SDK** - Direct integration with OpenAI's official library  
✅ **Better Security** - API keys stay on the backend server  
✅ **More Control** - Advanced error handling and rate limiting  
✅ **RESTful API** - Scalable backend that can serve multiple frontends  
✅ **Easy Scaling** - Add features like database, caching, analytics  
✅ **Production Ready** - Better suited for deployment  

---

## 🚀 Quick Start

### **Prerequisites**

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key

### **1. Clone the Repository**

```bash
git clone https://github.com/Rithik-Sharon-A/career-digital-twin-.git
cd career-digital-twin-
```

### **2. Set Up Python Environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure API Key**

1. Copy `.env.example` to `.env`:
```bash
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux
```

2. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

**Get your OpenAI API key:** https://platform.openai.com/api-keys

### **5. Run the Application**

```bash
# Start the Flask backend
python app.py
```

The backend will run on `http://localhost:5000`

### **6. Open the Frontend**

Open `index.html` in your browser. The chatbot will connect to your Python backend!

---

## 📁 Project Structure

```
career-digital-twin/
├── app.py                  # Flask backend with OpenAI SDK
├── knowledge_base.py       # Professional knowledge base for RAG
├── requirements.txt        # Python dependencies
├── .env                    # API keys (git-ignored)
├── .env.example           # Template for .env
├── .gitignore             # Git ignore file
├── index.html             # Frontend HTML
├── chatbot.js             # Frontend JavaScript
├── styles.css             # Frontend styles
└── README_PYTHON.md       # This file
```

---

## 🔧 How It Works

### **Architecture:**

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Browser   │ ──HTTP─→│ Flask Backend│ ──SDK──→│  OpenAI API │
│ (Frontend)  │ ←─JSON─ │  (Python)    │ ←─JSON─ │   GPT-4o    │
└─────────────┘         └──────────────┘         └─────────────┘
                              │
                              ↓
                        ┌──────────────┐
                        │ Knowledge    │
                        │ Base (RAG)   │
                        └──────────────┘
```

### **Flow:**

1. User types a message in the browser
2. Frontend sends HTTP POST to `http://localhost:5000/api/chat`
3. Flask backend receives the message
4. Backend uses OpenAI SDK with RAG (knowledge base)
5. OpenAI returns intelligent response
6. Backend sends response to frontend
7. User sees the AI response

---

## 🎯 API Endpoints

### **POST /api/chat**

Send a chat message and get AI response.

**Request:**
```json
{
  "message": "What are your technical skills?"
}
```

**Response:**
```json
{
  "response": "Rithik is a MERN Stack Developer specializing in...",
  "source": "openai",
  "model": "gpt-4o-mini"
}
```

### **GET /api/health**

Check backend health and configuration.

**Response:**
```json
{
  "status": "healthy",
  "model": "gpt-4o-mini",
  "api_configured": true
}
```

---

## ⚙️ Configuration

Edit `app.py` to change settings:

```python
CONFIG = {
    'MODEL': 'gpt-4o-mini',      # OpenAI model
    'MAX_TOKENS': 250,           # Response length
    'TEMPERATURE': 0.7           # Creativity (0-1)
}
```

### **Available Models:**

- `gpt-4o-mini` - **Recommended** - Best balance of cost/quality
- `gpt-4o` - Latest GPT-4 optimized model
- `gpt-4-turbo` - More powerful, higher cost
- `gpt-3.5-turbo` - Faster, cheaper

---

## 🔒 Security

✅ **API keys in .env** - Never committed to Git  
✅ **Backend validation** - Input sanitization  
✅ **CORS enabled** - Controlled access  
✅ **Error handling** - Graceful fallbacks  

---

## 🚢 Deployment Options

### **Option 1: Render (Recommended)**

1. Push to GitHub
2. Connect to Render.com
3. Add environment variable: `OPENAI_API_KEY`
4. Deploy!

### **Option 2: Heroku**

```bash
heroku create career-digital-twin
heroku config:set OPENAI_API_KEY=your-key
git push heroku main
```

### **Option 3: Railway**

1. Connect GitHub repo
2. Add `OPENAI_API_KEY` in settings
3. Deploy automatically

---

## 💰 Cost Estimate

Using **GPT-4o-mini**:

- **Input:** ~$0.15 per 1M tokens
- **Output:** ~$0.60 per 1M tokens

**For your chatbot:**
- Average conversation: ~500 tokens
- **1,000 conversations ≈ $0.30**
- **10,000 conversations ≈ $3.00**

Extremely affordable! 💸

---

## 🛠️ Development

### **Run in Development Mode**

```bash
python app.py
```

The app runs with `debug=True` for auto-reload.

### **Test the API**

```bash
# Health check
curl http://localhost:5000/api/health

# Send a message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are your skills?"}'
```

### **Add New Features**

- **Database:** Add SQLAlchemy for conversation history
- **Caching:** Use Redis for faster responses
- **Analytics:** Track popular questions
- **Rate Limiting:** Prevent abuse
- **Authentication:** Secure the API

---

## 📝 Customization

### **Update Knowledge Base**

Edit `knowledge_base.py` with your information:

```python
KNOWLEDGE_BASE = """
Your professional information here...
"""
```

### **Change System Prompt**

Edit the `SYSTEM_PROMPT` in `app.py` to change AI behavior.

---

## 🐛 Troubleshooting

### **"Module not found" Error**

```bash
pip install -r requirements.txt
```

### **"OPENAI_API_KEY not found" Warning**

Create `.env` file with your API key:
```
OPENAI_API_KEY=sk-your-key-here
```

### **CORS Error in Browser**

Make sure Flask-CORS is installed:
```bash
pip install flask-cors
```

### **Connection Refused**

Make sure Flask backend is running:
```bash
python app.py
```

---

## 🔄 Migrate from JavaScript Version

The JavaScript files (`chatbot.js`, `knowledge-base.js`) now call the Python backend instead of OpenRouter directly. Both versions coexist:

- **JavaScript files:** Frontend UI
- **Python files:** Backend API with OpenAI SDK

---

## 📚 Tech Stack

**Backend:**
- Python 3.8+
- Flask (Web framework)
- OpenAI SDK (AI integration)
- Flask-CORS (Cross-origin requests)
- python-dotenv (Environment variables)

**Frontend:**
- Vanilla JavaScript
- HTML5/CSS3
- Responsive design

---

## 🤝 Contributing

Feel free to fork and improve! Some ideas:

- Add conversation history
- Implement streaming responses
- Add voice input/output
- Multi-language support
- Analytics dashboard

---

## 📄 License

MIT License - Feel free to use for your own projects!

---

## 📧 Contact

**Rithik Sharon A**  
Email: rithiksharon.a@gmail.com  
LinkedIn: [linkedin.com/in/rithik-sharon](https://www.linkedin.com/in/rithik-sharon/)  
GitHub: [github.com/Rithik-Sharon-A](https://github.com/Rithik-Sharon-A)

---

## 🎉 Credits

Built with ❤️ using:
- OpenAI GPT-4o-mini
- Flask
- Python
- Lots of coffee ☕

---

**Ready to deploy your own AI Digital Twin? Let's go! 🚀**


