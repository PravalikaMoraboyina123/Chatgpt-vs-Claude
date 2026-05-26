# ChatGPT vs Claude

ChatGPT vs Claude is a professional AI comparison platform developed using Streamlit, OpenRouter API, OpenAI SDK, and Anthropic Claude models. The application enables users to compare responses from two advanced AI systems side by side in real time. The project is designed to provide a modern and interactive interface where users can analyze how different AI models respond to the same question, coding problem, research query, or uploaded document.

The platform supports multiple use cases including general conversations, coding assistance, cybersecurity discussions, research queries, document analysis, and image-based interactions. Users can upload PDF files, text documents, and images, allowing both AI models to process the uploaded content and generate intelligent responses.

The project focuses on delivering a clean user experience similar to modern AI chat platforms. Responses are displayed in a professional chat interface with structured formatting, bullet points, headings, syntax-highlighted code blocks, and copyable code sections. The interface is optimized for readability and comparison between models.

---

# Features

- Side-by-side AI response comparison
- ChatGPT and Claude integration
- Real-time AI responses
- Professional chat interface
- Structured AI responses
- Syntax-highlighted code blocks
- Copyable code sections
- PDF document analysis
- Text file analysis
- Image upload support
- Task-based AI optimization
- Modern responsive UI
- Streamlit-based deployment
- Secure API key management using environment variables

---

# Supported Tasks

The application supports multiple AI-driven tasks such as:

- General Chat
- Coding Assistance
- Research Queries
- Cybersecurity Discussions
- Document Analysis
- Image Analysis

Depending on the selected task, the platform automatically chooses the most suitable AI model configuration for better performance and optimized responses.

---

# Technologies Used

This project is built using modern Python-based AI and web development technologies.

- Python
- Streamlit
- OpenRouter API
- OpenAI SDK
- Anthropic Claude
- PyPDF2
- python-dotenv

---

# AI Models Used

## ChatGPT Model

```python
openai/gpt-4.1-mini
```

## Claude Model

```python
anthropic/claude-3-haiku
```

These models are accessed through OpenRouter API, which provides a unified interface for multiple AI providers.

---

# Project Structure

```text
chatgpt-vs-claude/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

- `app.py` contains the main Streamlit application.
- `requirements.txt` stores all required dependencies.
- `.gitignore` prevents sensitive or unnecessary files from being uploaded.
- `README.md` contains project documentation.
- `.env` stores secret API keys securely.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/chatgpt-vs-claude.git
```

## Navigate to Project Directory

```bash
cd chatgpt-vs-claude
```

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### Linux / Debian

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory of the project and add your OpenRouter API key.

```env
OPENROUTER_API_KEY=your_api_key_here
```

This API key is required for accessing AI models through OpenRouter.

---

# Running the Application

After installing dependencies and configuring the environment variables, run the application using the following command:

```bash
streamlit run app.py
```

The application will start locally and can be accessed through the browser.

---

# OpenRouter API

This project uses OpenRouter API to access multiple AI models from different providers using a unified API interface.

Official Website:

https://openrouter.ai

---

# Deployment

The project can be deployed globally using Streamlit Community Cloud. Streamlit provides a simple deployment workflow directly integrated with GitHub repositories.

## Deployment Steps

1. Push the project to GitHub
2. Open Streamlit Community Cloud
3. Connect your GitHub account
4. Select the repository
5. Choose `app.py`
6. Deploy the application

---

# Streamlit Secrets Configuration

After deployment, add your API key inside Streamlit Secrets.

```toml
OPENROUTER_API_KEY="your_api_key"
```

This ensures that the API key remains secure and is not exposed publicly.

---

# Security Notes

For security purposes:

- Do not upload `.env`
- Keep API keys private
- Use `.gitignore` properly
- Never expose secrets publicly

---

# .gitignore

```text
.env
venv/
__pycache__/
```

---

# Requirements

```txt
streamlit
openai
python-dotenv
PyPDF2
```

---

# Future Improvements

The project can be further enhanced with advanced features such as:

- Multi-model support
- Voice input
- Chat history database
- Authentication system
- Dark mode
- AI voting system
- PDF summarization
- Export chat functionality
- Custom model selector
- Advanced analytics dashboard

---

# Author

Pravalika Moraboyina

---

# License

This project is developed for educational, learning, and demonstration purposes.
