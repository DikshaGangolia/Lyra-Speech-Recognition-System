# 🎙️ Lyra – Voice-Activated Virtual Assistant
Lyra is a Python-based voice assistant that listens for a wake word, understands your commands, and responds using natural-sounding speech. It can open websites, play music, read the latest news headlines, and answer general questions using an LLM (via Groq).

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

## 👩‍💻 Author
DikshaGangolia
