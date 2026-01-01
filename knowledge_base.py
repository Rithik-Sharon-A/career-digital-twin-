"""
Knowledge Base for Rithik Sharon A's Digital Twin
Structured data + strict system prompt (fresher-friendly, no exaggeration).
"""

from __future__ import annotations

from typing import Any, Dict, List


KNOWLEDGE_BASE_DATA: Dict[str, Any] = {
    "metadata": {
        "owner": "Rithik Sharon A",
        "role": "MERN Stack Developer (Fresher)",
        "location": "Chennai, Tamil Nadu, India",
        "source": "Resume PDF",
        "usage": "Portfolio RAG Chatbot",
        "rules": [
            "Answer strictly from this knowledge base",
            "Do not exaggerate experience",
            "Do not claim industry employment",
            "If information is missing, say it is not available",
        ],
    },
    "system_prompt": (
        "You are an AI portfolio assistant for Rithik Sharon A. "
        "Answer only using the provided knowledge base. "
        "Be honest, professional, and concise. "
        "Do not assume industry experience."
    ),
    "knowledge_base": [
        {"id": "profile_01", "type": "profile", "content": "Rithik Sharon A is a MERN Stack Developer based in Chennai, Tamil Nadu, India."},
        {"id": "profile_02", "type": "profile", "content": "He is an early-career developer with strong hands-on experience through full-stack and AI-driven projects."},
        {"id": "profile_03", "type": "contact", "content": "Contact details include email rithiksharon.a@gmail.com, GitHub username Rithik-Sharon-A, and LinkedIn profile rithik-sharon."},
        {"id": "career_01", "type": "career_level", "content": "Rithik Sharon A is a fresher and has not yet worked in a full-time industry role."},
        {"id": "career_02", "type": "career_level", "content": "His experience is primarily project-based, focusing on real-world problem solving through personal and academic projects."},
        {"id": "education_01", "type": "education", "content": "Rithik completed his Bachelor of Technology in Electronics and Communication Engineering from SASTRA Deemed University, Thanjavur, between 2021 and 2025."},
        {"id": "education_02", "type": "education", "content": "He completed his Senior Secondary School (Class XII) education at SBIOA Senior Secondary School, Trichy, during 2020-2021."},
        {"id": "skills_lang_01", "type": "skills_languages", "content": "Rithik is proficient in JavaScript (ES6+), Python, HTML5, and CSS3."},
        {"id": "skills_frontend_01", "type": "skills_frontend", "content": "Frontend technologies include React.js, Next.js, Tailwind CSS, responsive design principles, and Vite."},
        {"id": "skills_backend_01", "type": "skills_backend", "content": "Backend development skills include Node.js, Express.js, API handling, bcrypt for password hashing, and JWT-based authentication."},
        {"id": "skills_db_01", "type": "skills_database", "content": "Rithik has hands-on experience using MongoDB as a NoSQL database."},
        {"id": "skills_tools_01", "type": "tools", "content": "Development tools include Git, GitHub, VS Code, and Cursor AI."},
        {"id": "ai_01", "type": "ai_expertise", "content": "Rithik specializes in Agentic AI, prompt engineering, autonomous agents, and OpenAI API integration."},
        {"id": "ai_02", "type": "ai_expertise", "content": "He has implemented function calling and tool usage within AI agents to enable dynamic behavior."},
        {"id": "proj1_overview", "type": "project_overview", "project": "Agentic AI Digital Twin", "content": "Rithik developed an Agentic AI-powered digital twin integrated into a MERN-based portfolio website."},
        {"id": "proj1_ai", "type": "project_ai", "project": "Agentic AI Digital Twin", "content": "The digital twin uses a custom agent framework and OpenAI APIs to enable conversational interactions and autonomous responses."},
        {"id": "proj1_backend", "type": "project_backend", "project": "Agentic AI Digital Twin", "content": "The backend was implemented using Node.js and Express.js to manage AI requests, routing, and persona control."},
        {"id": "proj1_frontend", "type": "project_frontend", "project": "Agentic AI Digital Twin", "content": "The frontend portfolio was built using React.js and Framer Motion to deliver a responsive and animated user interface."},
        {"id": "proj1_stack", "type": "project_stack", "project": "Agentic AI Digital Twin", "content": "Technologies used include Python, OpenAI API, React.js, Node.js, Express.js, MongoDB, Framer Motion, and Vite."},
        {"id": "proj2_overview", "type": "project_overview", "project": "MERN E-commerce Platform", "content": "Rithik developed a full-stack MERN e-commerce application with secure authentication and real-time product management."},
        {"id": "proj2_security", "type": "project_security", "project": "MERN E-commerce Platform", "content": "The platform implements JWT-based authentication with bcrypt for secure password hashing."},
        {"id": "proj2_api", "type": "project_backend", "project": "MERN E-commerce Platform", "content": "A RESTful API was built to support dynamic product search, filtering, and pagination."},
        {"id": "proj2_state", "type": "project_state", "project": "MERN E-commerce Platform", "content": "Redux Toolkit was used to manage global application state, including cart persistence and user sessions."},
        {"id": "proj2_ui", "type": "project_frontend", "project": "MERN E-commerce Platform", "content": "The application features a mobile-first UI built with Tailwind CSS and includes a simulated payment gateway."},
        {"id": "proj2_stack", "type": "project_stack", "project": "MERN E-commerce Platform", "content": "Technologies used include MongoDB, Express.js, React.js, Node.js, Redux Toolkit, Tailwind CSS, JWT, and bcrypt."},
        {"id": "rules_01", "type": "rules", "content": "If a question is outside the resume or portfolio scope, respond that the information is not available."},
        {"id": "rules_02", "type": "rules", "content": "Do not claim professional work experience or company employment."},
    ],
}


def _format_kb_items(items: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    for item in items:
        item_id = item.get("id", "")
        item_type = item.get("type", "")
        project = item.get("project")
        content_item = item.get("content", "")
        if project:
            lines.append(f"- [{item_id}] ({item_type}) [{project}] {content_item}")
        else:
            lines.append(f"- [{item_id}] ({item_type}) {content_item}")
    return "\n".join(lines)


KNOWLEDGE_BASE_TEXT: str = _format_kb_items(KNOWLEDGE_BASE_DATA["knowledge_base"])


SYSTEM_PROMPT: str = (
    f"{KNOWLEDGE_BASE_DATA['system_prompt']}\n\n"
    "RULES:\n"
    + "\n".join([f"- {r}" for r in KNOWLEDGE_BASE_DATA["metadata"]["rules"]])
    + "\n\n"
    "KNOWLEDGE BASE:\n"
    + KNOWLEDGE_BASE_TEXT
)
