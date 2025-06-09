# 🩺 Patient Message Triage API

This is a Flask-based web service that uses a Hugging Face transformer model to classify patient messages into categories like **emergency**, **routine**, **follow-up**, or **other**.

---

## 🚀 Features

- Accepts patient name, mobile number, and message
- Uses `facebook/bart-large-mnli` or custom transformer model for zero-shot classification
- Returns current category and previous message history
- Input validation via `marshmallow`
- SQLite-based message logging
- Ready for deployment to Render or Railway

---

## 📦 Installation

```bash
https://github.com/DineshSharma897/triage-api.git
cd triage-api
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python app.py
```


## 📬 API Endpoint

### `POST /predict`

**Request JSON**:
```json
{
  "name": "John Doe",
  "mobile": "9876543210",
  "message": "I have chest pain and shortness of breath"
}
```

**Response JSON**:
```json
{
  "current_result": {
    "category": "emergency",
    "confidence": 0.91
  },
  "history": [
    {
      "message": "I need to refill my medication.",
      "category": "routine",
      "confidence": 0.87,
      "timestamp": "2025-06-09T08:00:00"
    }
  ]
}
```

---

## 🧪 Test Locally with Postman

1. Open Postman
2. Set method to **POST**
3. URL: `http://127.0.0.1:5000/predict`
4. Go to **Body > raw > JSON**, and paste sample request

---


## 📂 Folder Structure

```
triage_app/
├── app.py
├── model.py
├── utils.py
├── schema.py
├── requirements.txt
├── README.md
```

---
