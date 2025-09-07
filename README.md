# ☕ Cafe Rating Collector

A simple **Flask web application** to manage and view cafe ratings.  
Users can add cafes with details like location, opening/closing times, coffee rating, WiFi strength, and power outlet availability.  
All cafes are stored in a CSV file and displayed in a **Bootstrap-styled table** using [Flask-Table](https://pypi.org/project/Flask-Table/).

---

## 🚀 Features
- Add new cafes with details through a **Flask-WTF form**
- Validate **Google Maps URL** using `URL` validator
- Ratings with emojis (☕, 🛜, ⚡) selectable via dropdown
- Display data in a **Bootstrap table** with hover effects
- Location links are clickable → opens in Google Maps
- Flash messages for successful submissions

---

## 🌍 Live Demo
🔗 [View Cafe Rating Collector](https://cafe-rating-collector.onrender.com/) 

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask**
- **Flask-Bootstrap**
- **Flask-WTF**
- **WTForms**
- **Flask-Table**
- **CSV** (for data storage)

---

## 📂 Project Structure
- ├── app.py # Main Flask app
- ├── cafe-data.csv # Stores cafe data
- ├── templates/ # Jinja2 HTML templates
- │ ├── base.html
- │ ├── index.html
- │ ├── add.html
- │ └── cafes.html
- ├── static/
- │ └── styles.css # Custom styles (optional)
- └── README.md

---

## ▶️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/cafe-rating-collector.git
cd cafe-rating-collector
