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
🔗 **Deployed App:** [Visit the Live App](https://univoice-all.onrender.com) 

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
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
```

### 5️⃣ Run Migrations & Start Server
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.




