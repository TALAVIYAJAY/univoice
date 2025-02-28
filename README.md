# 🏥 Translation Web App with Generative AI

## 🌍 Overview
The **Healthcare Translation Web App** is an AI-powered solution designed to bridge language barriers in medical settings. This application enables **real-time voice-to-text conversion, AI-powered translation, and text-to-speech playback**, ensuring seamless communication between healthcare providers and patients.

🚀 **Key Features:**
- 🎙 **Voice-to-Text**: Convert spoken words into text using Web Speech API.
- 🌐 **AI-Powered Translation**: Translate text into multiple languages using OpenAI/Google Translate.
- 🔊 **Text-to-Speech (TTS)**: Listen to translated text via speech synthesis.
- 📱 **Mobile-First UI**: Fully responsive and optimized for various devices.
- 🔒 **Secure & Scalable**: CSRF protection, input validation, and error handling.

---

## 🛠️ Tech Stack
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **AI & NLP**: Google Translate API
- **Speech Recognition & Synthesis**: Web Speech API
- **Database**: PostgreSQL (or SQLite for development)
- **Deployment**: Render

---

## 🚀 Live Demo
🔗 **Deployed App:** [Visit the Live App](#) *(Replace with actual URL)*

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/yourusername/healthcare-translation.git
$ cd healthcare-translation
```

### 2️⃣ Set Up a Virtual Environment
```sh
$ python -m venv env
$ source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=*
TRANSLATION_API_KEY=your_api_key_here
```

### 5️⃣ Run Migrations & Start Server
```sh
$ python manage.py migrate
$ python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

---

## 🔧 API Endpoints

### 🎙 Voice-to-Text
**POST** `/api/voice-to-text/`
```json
{
  "audio": "base64_encoded_audio_string"
}
```
_Response:_
```json
{
  "text": "Detected speech content"
}
```

### 🌍 Text Translation
**POST** `/api/translate/`
```json
{
  "text": "Hello, how are you?",
  "target_language": "es"
}
```
_Response:_
```json
{
  "translated_text": "Hola, ¿cómo estás?"
}
```

### 🔊 Text-to-Speech
**POST** `/api/text-to-speech/`
```json
{
  "text": "Hola, ¿cómo estás?"
}
```
_Response:_
- Returns an **audio file** for playback.

---

## 📦 Deployment on Render

### 1️⃣ Create a New Web Service on Render
- Choose **Python** as the runtime.
- Connect your GitHub repository.
- Set environment variables in Render's **Secret Settings**.

### 2️⃣ Automatic Deployment
Every push to the **main** branch will trigger a new deployment.

---

## 📌 Future Enhancements
✅ Multi-voice support (e.g., gender selection for TTS)
✅ Offline functionality using IndexedDB
✅ Integration with Electronic Health Records (EHR)

---

## 🏆 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit your changes.
4. Push and create a pull request.

---

## 📄 License
This project is licensed under the **MIT License**.

---

💡 **Created by [Your Name]** | 🚀 AI-Powered Healthcare Communication

