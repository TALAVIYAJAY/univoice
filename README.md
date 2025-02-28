# 🌍 UniVoice - AI-Powered Translation App
UniVoice is an advanced AI-powered multilingual translation app that provides real-time text translation using Google Translate API. This Django-based web application enables seamless communication across languages with an intuitive and responsive interface.

## 🚀 **Features**  
✅ Translate text between multiple languages  
✅ AI-powered translations using **Google Translate API**  
✅ Stores translation history in the database  
✅ Secure API endpoints for **developers**  
✅ **Mobile-first design** for a smooth user experience  

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
$ git clone https://github.com/TALAVIYAJAY/univoice.git
$ cd univoice-main
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




