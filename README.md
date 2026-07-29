# 🎙️ Lyra – Voice-Activated Virtual Assistant

Lyra is a Python-based voice assistant that listens for a wake word, understands your commands, and responds using natural-sounding speech. It can open websites, play music, read the latest news headlines, and answer general questions using an LLM (via Groq).

---

## ✨ Features

- 🎤 **Wake-word activation** — say "Lyra" to activate listening
- 🗣️ **Speech recognition** — converts your voice commands to text using Google Speech Recognition
- 🔊 **Natural voice responses** — uses gTTS (Google Text-to-Speech) for clear, human-like audio
- 🌐 **Quick web shortcuts** — open Google, YouTube, LinkedIn, Facebook, Instagram with a voice command
- 🎵 **Music playback** — play songs from a local music library
- 📰 **News headlines** — fetches and reads out top headlines via NewsAPI
- 🤖 **AI fallback** — any command it doesn't recognize is handled by an LLM (Llama 3.3 70B via Groq), so it can answer general questions like a real assistant

---

## 🛠️ Tech Stack

| Component | Purpose |
|---|---|
| `speech_recognition` | Captures and transcribes voice input |
| `gTTS` + `pygame` | Converts text responses to speech and plays audio |
| `pydub` + `ffmpeg` | Adjusts playback speed for a natural speaking pace |
| `Groq API` (Llama 3.3 70B) | Powers conversational/general-purpose responses |
| `NewsAPI` | Fetches current top headlines |
| `python-dotenv` | Loads API keys securely from a `.env` file |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/DikshaGangolia/Lyra-Speech-Recognition-System.git
cd Lyra-Speech-Recognition-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg (required for audio speed adjustment)

- **Windows**: Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extract, and add the `bin` folder to your system PATH.
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

Verify with:
```bash
ffmpeg -version
```

### 5. Set up environment variables

Copy the example file and add your own API keys:

```bash
cp .env.example .env
```

Then open `.env` and fill in your real keys:

```
GROQ_API_KEY=your_groq_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

> ⚠️ **Never commit your `.env` file.** It's already excluded via `.gitignore`. Get your keys from [Groq Console](https://console.groq.com) and [NewsAPI](https://newsapi.org).

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

1. Lyra will calibrate for ambient noise, then start listening.
2. Say **"Lyra"** to wake it up.
3. Once it responds, speak your command — for example:
   - *"Open YouTube"*
   - *"Play [song name]"*
   - *"What's the news?"*
   - *"What's the capital of France?"* (handled by the AI)

---

## 📁 Project Structure

```
Lyra-Speech-Recognition-System/
├── main.py              # Core assistant logic
├── musicLibrary.py      # Local song name → URL mapping
├── .env.example         # Template for required environment variables
├── .gitignore           # Excludes .env, venv, cache files, etc.
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🎵 Adding Songs

Add entries to `musicLibrary.py` in this format:

```python
music = {
    "song_name": "https://youtube.com/watch?v=..."
}
```

Then say *"Play song_name"* to trigger playback.

---

## 🔐 Security Notes

- API keys are loaded from `.env` and never hardcoded.
- `.env` is excluded from version control via `.gitignore`.
- If a key is ever accidentally exposed, **revoke and regenerate it immediately** from the provider's dashboard rather than just deleting it from Git history.

---

## 🚧 Known Limitations

- Requires an active internet connection (speech recognition, gTTS, and the AI/news APIs are all cloud-based).
- Wake-word detection is a simple exact-match on "lyra," not a dedicated wake-word model.
- Currently supports English only.

---

## 📄 License

This project is open source and available for personal and educational use.
