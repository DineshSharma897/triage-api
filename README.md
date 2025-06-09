# Patient Message Triage API

## 📦 Setup

```bash
pip install -r requirements.txt
python app.py
```

## 🚀 API Usage

### POST `/predict`

**Input JSON:**
```json
{
  "name": "John",
  "mobile": "9876543210",
  "message": "I need to refill my medication."
}
```

**Response:**
```json
{
  "current_result": {
    "category": "follow-up",
    "confidence": 0.26
  },
  "history": [
        {
            "category": "follow-up",
            "confidence": 0.85,
            "message": "I need to refill my cholesterol medication"
        }
  ]
}
```