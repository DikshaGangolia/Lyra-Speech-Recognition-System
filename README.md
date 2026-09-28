# 🎙️ Lyra – Voice-Activated Virtual Assistant

> **A Python-based intelligent voice assistant that listens, understands spoken commands, performs useful tasks, and responds naturally using speech and AI.**

## 📌 Project Overview

**Lyra** is a voice-activated virtual assistant designed to provide a hands-free and interactive user experience. It listens for the wake word **“Lyra”**, converts spoken commands into text, processes the user's request, and responds using natural-sounding speech.
The assistant can open popular websites, play music from a local library, read current news headlines, and answer general questions using an AI-powered fallback system.

---

## ✨ Key Features

- 🎤 **Wake-word activation** — Say **“Lyra”** to activate listening.
- 🗣️ **Speech recognition** — Converts spoken commands into text.
- 🔊 **Natural voice responses** — Responds using text-to-speech technology.
- 🌐 **Website shortcuts** — Opens platforms such as Google, YouTube, LinkedIn, Facebook, and Instagram.
- 🎵 **Music playback** — Plays songs from a local music library.
- 📰 **News headlines** — Fetches and reads current top headlines.
- 🤖 **AI-powered responses** — Handles general questions that do not match predefined commands.
- 🔐 **Secure configuration** — Loads API keys through environment variables.

---

## 🏗️ How Lyra Works

```text
🎤 User Voice
      │
      ▼
Wake Word Detection
      │
      ▼
Speech Recognition
      │
      ▼
Command Processing
      │
 ┌────┼────┐
 ▼    ▼    ▼
Web  Music News / AI
      │
      ▼
🔊 Voice Response
```

Lyra follows a simple workflow: it listens for activation, understands the user's spoken command, determines the appropriate action, and provides feedback through speech.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application development |
| **SpeechRecognition** | Captures and converts voice input into text |
| **gTTS** | Converts text responses into speech |
| **pygame** | Plays generated audio responses |
| **pydub** | Processes audio and adjusts playback |
| **FFmpeg** | Supports audio processing functionality |
| **Groq API** | Provides AI-powered conversational responses |
| **Llama 3.3 70B** | Language model used for general queries |
| **NewsAPI** | Fetches current news headlines |
| **python-dotenv** | Loads environment variables securely |

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DikshaGangolia/Lyra-Speech-Recognition-System.git
```

### 2. Open the Project Directory

```bash
cd Lyra-Speech-Recognition-System
```

### 3. Create a Virtual Environment *(Recommended)*

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages used by the project.

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project directory and store the required API keys there.

Example:

```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_news_api_key
```

> ⚠️ Never upload your real API keys or `.env` file to a public GitHub repository.

---

## 🎤 How to Use Lyra

1. Start the application.
2. Say **“Lyra”** to activate the assistant.
3. Speak your command clearly.
4. Lyra processes the command and performs the appropriate action.
5. If the command is not predefined, the AI system can provide a conversational response.

### Example Commands

- “Open YouTube”
- “Open Google”
- “Play music”
- “Tell me the news”
- Ask a general question

---

## 🧠 Concepts Demonstrated

This project demonstrates several important concepts in Python and AI-based application development:
- Speech recognition
- Text-to-speech processing
- Audio playback and processing
- API integration
- Environment variable management
- Voice-command processing
- AI-powered conversational responses
- Conditional command handling

---

## 📂 Project Structure

The repository contains the application code and supporting files required for the voice assistant. A typical structure includes:

```text
Lyra-Speech-Recognition-System/
│
├── main.py                # Main voice assistant logic
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment configuration
├── music/                 # Local music files
└── README.md              # Project documentation
```

> The exact file names and structure may evolve as the project develops.

---

## 🔮 Future Improvements

Potential future enhancements include:

- 🌦️ Weather information support
- 📅 Calendar and reminder integration
- 🖥️ Graphical user interface
- 🌍 Support for additional languages
- 🎙️ Improved wake-word detection
- 🧠 More advanced contextual conversations
- 🔌 Integration with additional APIs and smart devices

---

## 👩‍💻 Author

**Diksha Gangolia**

---

## 📌 Project Purpose

Lyra was created as a hands-on project to explore the combination of **Python, speech recognition, text-to-speech, APIs, and AI-powered language models**. The project demonstrates how multiple technologies can work together to create an interactive voice-based application.

---

⭐ **If you find this project interesting, consider giving the repository a star!**
