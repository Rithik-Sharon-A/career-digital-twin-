# Career Digital Twin - Rithik Sharon A

An AI-powered digital twin chatbot that represents me professionally. Recruiters, colleagues, and anyone interested can chat with this AI to learn about my skills, experience, projects, and more - 24/7!

![Digital Twin](https://img.shields.io/badge/AI-Digital%20Twin-7c3aed?style=for-the-badge)
![OpenRouter](https://img.shields.io/badge/OpenRouter-AI%20API-ff6b6b?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-4ade80?style=for-the-badge)

---

## What Is This?

This is my **Career Digital Twin** - an AI chatbot that knows everything about my professional profile. It uses:
- **RAG (Retrieval-Augmented Generation)** with a comprehensive knowledge base
- **OpenRouter API** with Llama 3.1 8B (FREE model)
- **Vanilla JavaScript** - No frameworks, lightweight and fast
- **Beautiful UI** - Modern, responsive design

---

## Features

- **AI-Powered Responses** - Natural, intelligent conversations
- **Comprehensive Knowledge** - Knows about skills, projects, experience
- **Quick Questions** - Pre-defined buttons for common queries
- **Fully Responsive** - Works perfectly on all devices
- **Fast & Lightweight** - No heavy frameworks
- **Beautiful Design** - Modern gradient UI with animations
- **Fallback System** - Works even without API key
- **Free to Use** - Uses free AI model

---

## Quick Start

### Option 1: With AI (Recommended)

1. **Get OpenRouter API Key** (FREE)
 ```
 Visit: https://openrouter.ai/keys
 Sign up and create a new key
 ```

2. **Setup Configuration**
 - Copy `config.example.js` to `config.js`
 - Open `config.js`
 - Replace `YOUR_OPENROUTER_API_KEY_HERE` with your actual API key
 - The `config.js` file is git-ignored for security

3. **Open in Browser**
 ```
 Simply open index.html in your browser!
 ```

### Option 2: Without AI (Still Works!)

1. **Just Open It**
 ```
 Open index.html in your browser
 ```
 The chatbot will use smart keyword-based responses. Still helpful!

---

## Project Structure

```
career-digital-twin/
 index.html # Main HTML file
 styles.css # All styles and animations
 chatbot.js # Chatbot logic with OpenRouter integration
 knowledge-base.js # Comprehensive knowledge about me
 README.md # This file
 SETUP.md # Detailed setup guide
```

---

## How It Works

```
User asks question

Chatbot receives message

Sends to OpenRouter AI with knowledge base

AI generates intelligent response

User receives answer
```

### With AI:
- Natural language understanding
- Context-aware responses
- Powered by Llama 3.1 8B

### Without AI (Fallback):
- Keyword-based responses
- Still answers common questions
- Never breaks!

---

## Cost

**FREE!**

- Uses `meta-llama/llama-3.1-8b-instruct:free` model
- OpenRouter free tier
- No credit card required
- Perfect for portfolio projects

---

## Customization

### Update Information

Edit `knowledge-base.js` to update:
- Skills and technologies
- Projects
- Experience
- Contact information
- Any other details

### Change AI Model

In `chatbot.js`, change the model:
```javascript
MODEL: 'meta-llama/llama-3.1-8b-instruct:free' // Current (FREE)
// Or upgrade to:
MODEL: 'openai/gpt-4o-mini' // Premium
MODEL: 'anthropic/claude-3-haiku' // Premium
```

### Styling

Edit `styles.css`:
- Change colors
- Modify animations
- Adjust layout
- Customize theme

---

## Deployment

### GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages in settings
3. Select `main` branch
4. Done! Your Digital Twin is live

### Netlify
1. Drag and drop the folder
2. Instant deployment
3. Custom domain support

### Vercel
```bash
npm i -g vercel
vercel
```

**Note:** Add your API key as an environment variable when deploying!

---

## Security

### API Key Safety
- Don't commit API key to public repos
- Use environment variables for production
- Enable domain restrictions in OpenRouter dashboard
- Monitor usage regularly

### For Production:
Create a `.env` file:
```env
OPENROUTER_API_KEY=your-key-here
```

Update `chatbot.js` to read from environment.

---

## Troubleshooting

### Chatbot Not Responding
- Check API key is correct
- Check console for errors (F12)
- Verify internet connection
- Try fallback mode (remove API key temporarily)

### Fallback Responses Only
- API key not configured
- Invalid API key
- Network issues
**Solution:** Still works! Add API key for AI responses

### Styling Issues
- Clear browser cache
- Check CSS file is loaded
- Verify no conflicting styles

---

## Features Breakdown

### Current Features:
- AI-powered conversations
- RAG with knowledge base
- Quick question buttons
- Typing indicators
- Message timestamps
- Responsive design
- Smooth animations
- Error handling
- Fallback system

### Potential Enhancements:
- Chat history (localStorage)
- Voice input/output
- Multi-language support
- File sharing
- Analytics tracking
- Custom themes
- Export chat

---

## What I Learned Building This

- OpenRouter API integration
- RAG (Retrieval-Augmented Generation)
- Vanilla JavaScript DOM manipulation
- CSS animations and responsive design
- AI chatbot UX best practices
- Fallback systems for reliability

---

## About Me

**Rithik Sharon A**
- MERN Stack Developer
- AI Specialist (Agentic AI, OpenAI APIs)
- Building innovative web applications
- rithiksharon.a@gmail.com
- [LinkedIn](https://www.linkedin.com/in/rithik-sharon/)
- [GitHub](https://github.com/Rithik-Sharon-A)

---

## Contributing

Want to improve this Digital Twin?
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License - Feel free to use this for your own Digital Twin!

---

## Acknowledgments

- OpenRouter for free AI API
- Llama 3.1 8B for powerful model
- The developer community for inspiration

---

## Contact

Questions about this project or want to work together?
- Email: rithiksharon.a@gmail.com
- LinkedIn: https://www.linkedin.com/in/rithik-sharon/
- Portfolio: [Your Portfolio URL]

---

## Star This Repo!

If you find this Digital Twin useful, please star the repo!

---

**Built with by Rithik Sharon A**

*Combining MERN Stack expertise with AI to create innovative solutions*

---

## Quick Links

- [Live Demo](#) - See it in action!
- [Setup Guide](SETUP.md) - Detailed setup instructions
- [Portfolio](your-portfolio-url) - My main portfolio
- [GitHub](https://github.com/Rithik-Sharon-A) - More projects

---

Last Updated: December 2025

