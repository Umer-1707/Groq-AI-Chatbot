# 🤖 AI Chatbot (Groq API + Voice + GUI)

This is a Python-based AI chatbot powered by the Groq API. It supports text conversations, voice input using speech recognition, and text-to-speech responses through a clean Tkinter desktop interface.

The project was originally built around two years ago and was recently refactored with a better project structure and improved user interface.


## 🚀 Features

*  Chat with AI (powered by Groq API)
*  Voice input (Speech Recognition)
*  Text-to-Speech output
*  Clean Tkinter GUI
*  Fast responses (thanks to Groq)
*  Modular code structure (easy to extend)



## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* Groq API (LLM)
* SpeechRecognition
* pyttsx3 (Text-to-Speech)
* python-dotenv



## 📁 Project Structure


AI-Chatbot/
│── main.py
│── config.py
│
├── api/
│   └── groq_client.py
│
├── core/
│   └── chatbot.py
│
├── voice/
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── ui/
│   └── gui.py
│
├── assets/
│   └── title.png
│
├── .env (create manually)
├── requirements.txt
└── README.md



## ⚙️ Setup Instructions

1. Clone the repository:

git clone <your-repo-link>
cd AI-Chatbot

2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file:

GROQ_API_KEY=your_api_key_here

4. Run the project:

python main.py


## ⚠️ Notes

* Make sure your microphone is working for voice input
* Internet connection is required (API calls)
* `.env` file should not be uploaded to GitHub


## 💡 Why I Built This

I wanted to explore how AI APIs can be integrated into real applications,
not just command-line scripts.

This project helped me understand:

* API integration
* GUI design
* threading in Python
* structuring a project properly


## 🚧 Future Improvements

* Chat history saving
* Better UI (chat bubbles, animations)
* Web version (Flask / React)
* File-based chat (PDFs, etc.)


## 👨‍💻 Author

**Muhammad Umer**


## ⭐ Final Thoughts

This project serves as a foundation for more advanced AI assistants. Feel free to fork it, experiment with it, or build your own features on top of it.
