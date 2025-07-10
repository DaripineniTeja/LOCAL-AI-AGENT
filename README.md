# 🍕 Local AI Pizza Assistant

This is a LangChain-based local AI chatbot that answers user questions about a pizza restaurant using real customer reviews. It runs fully offline using Ollama and features both a terminal CLI and a Gradio web interface.

---

## 📌 Features

- 🔍 Answers questions using retrieved pizza reviews
- 🧠 Powered by LLaMA3.2 via Ollama
- 🛜 Runs completely offline on your local machine
- 🌐 Gradio GUI for easy interaction
- ⚡ Fast response using LangChain chaining logic

---

## 🚀 How It Works

1. The user asks a question (e.g., "Are vegan options available?")
2. The system retrieves relevant reviews
3. LLaMA3 generates a response using the reviews as context

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Gradio](https://www.gradio.app/)
- Python 3.10+
- Local Model: `llama3.2` (or any Ollama-supported model)

---

## 📁 Project Structure

📦 Local AI Agent/
├── main.py # CLI mode (manual Q&A)
├── app.py # Gradio web app interface
├── vector.py # Review retrieval logic
├── requirements.txt # Python dependencies
├── README.md # You’re here!
└── .gitignore # Ignore venv, cache, etc.



---

## 🖥️ Installation

### 🔧 1. Clone this repo
```bash
git clone https://github.com/DaripineniTeja/local-ai-pizza-assistant.git
cd local-ai-pizza-assistant

###🔧 2. Install dependencies
pip install -r requirements.txt

###🔧 3. Install Ollama & Run the model
# Install ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model
ollama pull llama3

# Start the Ollama server
ollama serve



✨ Author
Daripineni Teja
🔗 Instagram
📧 aiwithteja

