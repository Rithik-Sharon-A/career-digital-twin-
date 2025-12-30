// Career Digital Twin - Chatbot Logic
// NOTE: Configuration is loaded from config.js (not committed to Git)

// Verify CONFIG is loaded
if (typeof CONFIG === 'undefined') {
    console.error('❌ CONFIG not loaded! Make sure config.js is included before chatbot.js');
    alert('Configuration error: config.js not found or not loaded properly!');
}

// DOM Elements
const messagesContainer = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const typingIndicator = document.getElementById('typing-indicator');
const quickQuestionsContainer = document.getElementById('quick-questions');
const initialTime = document.getElementById('initial-time');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initialTime.textContent = getCurrentTime();
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    sendBtn.addEventListener('click', handleSendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    });

    // Quick question buttons
    document.querySelectorAll('.quick-question-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const question = btn.getAttribute('data-question');
            userInput.value = question;
            handleSendMessage();
            quickQuestionsContainer.style.display = 'none';
        });
    });
}

// Handle sending messages
async function handleSendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Add user message
    addMessage(message, 'user');
    userInput.value = '';
    
    // Hide quick questions after first message
    quickQuestionsContainer.style.display = 'none';

    // Show typing indicator
    typingIndicator.style.display = 'flex';
    sendBtn.disabled = true;

    try {
        const response = await getAIResponse(message);
        addMessage(response, 'bot');
    } catch (error) {
        console.error('Error:', error);
        addMessage(
            "I apologize, but I'm having trouble connecting right now. Please try again or contact Rithik directly at rithiksharon.a@gmail.com",
            'bot'
        );
    } finally {
        typingIndicator.style.display = 'none';
        sendBtn.disabled = false;
        userInput.focus();
    }
}

// Get AI response
async function getAIResponse(userMessage) {
    // Check if API key is configured
    if (!CONFIG.OPENROUTER_API_KEY || CONFIG.OPENROUTER_API_KEY === 'YOUR_OPENROUTER_API_KEY_HERE') {
        return getFallbackResponse(userMessage);
    }

    try {
        const response = await fetch(CONFIG.API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${CONFIG.OPENROUTER_API_KEY}`,
                'HTTP-Referer': window.location.origin,
                'X-Title': 'Career Digital Twin - Rithik Sharon A'
            },
            body: JSON.stringify({
                model: CONFIG.MODEL,
                messages: [
                    {
                        role: 'system',
                        content: `You are Rithik Sharon A's AI-powered Digital Twin. Use the following comprehensive knowledge base to answer questions accurately, professionally, and conversationally.

KNOWLEDGE BASE:
${knowledgeBase}

GUIDELINES:
- Answer based on the knowledge base provided
- Be friendly, professional, and conversational
- Keep responses concise but informative (2-4 sentences typically)
- If asked something not in the knowledge base, politely suggest contacting Rithik directly
- Include relevant links when mentioning contact info or projects
- Show enthusiasm about Rithik's skills and accomplishments
- Be honest and authentic
- If unsure, recommend reaching out directly rather than making up information`
                    },
                    {
                        role: 'user',
                        content: userMessage
                    }
                ],
                temperature: CONFIG.TEMPERATURE,
                max_tokens: CONFIG.MAX_TOKENS
            })
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }

        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        console.error('OpenRouter API Error:', error);
        return getFallbackResponse(userMessage);
    }
}

// Fallback responses when API is unavailable
function getFallbackResponse(message) {
    const msg = message.toLowerCase();

    if (msg.includes('skill') || msg.includes('technology') || msg.includes('tech stack')) {
        return "Rithik is a MERN Stack Developer specializing in React, Node.js, Express, and MongoDB. He also has expertise in Agentic AI and OpenAI APIs, combining full-stack development with cutting-edge AI integration!";
    }
    
    if (msg.includes('project')) {
        return "Rithik has built several exciting projects including a modern Portfolio Website, this Career Digital Twin using AI, and various AI-powered applications. Check out his GitHub at github.com/Rithik-Sharon-A to see more!";
    }
    
    if (msg.includes('ai') || msg.includes('artificial intelligence') || msg.includes('openai')) {
        return "Rithik specializes in Agentic AI and OpenAI APIs! He uses these technologies to automate complex workflows, build intelligent chatbots, and create AI-powered web applications that enhance user experiences.";
    }
    
    if (msg.includes('experience') || msg.includes('work') || msg.includes('background')) {
        return "Rithik is a MERN Stack Developer with strong expertise in building scalable, responsive web applications. He specializes in integrating Agentic AI and OpenAI APIs to create intelligent, automated solutions.";
    }
    
    if (msg.includes('contact') || msg.includes('email') || msg.includes('reach') || msg.includes('hire')) {
        return "You can reach Rithik at rithiksharon.a@gmail.com (he usually responds within 24-48 hours) or connect on LinkedIn at linkedin.com/in/rithik-sharon/. He's open to full-time opportunities and freelance projects!";
    }
    
    if (msg.includes('available') || msg.includes('looking for work')) {
        return "Yes! Rithik is open to exciting opportunities including full-time positions, freelance projects, and collaborations. Feel free to reach out at rithiksharon.a@gmail.com to discuss opportunities.";
    }
    
    if (msg.includes('resume') || msg.includes('cv')) {
        return "You can download Rithik's resume from his portfolio website. It contains detailed information about his education, experience, skills, and projects. Visit his portfolio or email him directly at rithiksharon.a@gmail.com!";
    }
    
    if (msg.includes('github') || msg.includes('code')) {
        return "Check out Rithik's GitHub at github.com/Rithik-Sharon-A to see his projects and code. He has several full-stack MERN applications and AI-powered projects showcased there!";
    }

    // Default response
    return "That's a great question! I'm Rithik's Digital Twin powered by AI. Feel free to ask me about his skills, projects, experience with AI, or how to contact him. What would you like to know?";
}

// Add message to chat
function addMessage(text, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    const avatarDiv = document.createElement('div');
    avatarDiv.className = 'message-avatar';
    avatarDiv.textContent = type === 'user' ? '👤' : '🤖';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const textP = document.createElement('p');
    textP.textContent = text;
    
    const timeSpan = document.createElement('span');
    timeSpan.className = 'message-time';
    timeSpan.textContent = getCurrentTime();
    
    contentDiv.appendChild(textP);
    contentDiv.appendChild(timeSpan);
    
    messageDiv.appendChild(avatarDiv);
    messageDiv.appendChild(contentDiv);
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Get current time
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// Console info
console.log('%c🤖 Career Digital Twin Loaded', 'color: #7c3aed; font-size: 16px; font-weight: bold');
console.log('To enable AI responses, update the OPENROUTER_API_KEY in chatbot.js');
console.log('Get your free API key at: https://openrouter.ai/keys');
console.log('Without an API key, the chatbot will use smart fallback responses.');

