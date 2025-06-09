from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import classify_message
from model import db, Message
from schema import PredictRequestSchema
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    schema = PredictRequestSchema()

    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    name = validated_data['name'].strip()
    mobile = validated_data['mobile'].strip()
    message = validated_data['message'].strip()

    category, confidence = classify_message(message)

    new_entry = Message(name=name, mobile=mobile, message=message,
                        category=category, confidence=confidence)
    db.session.add(new_entry)
    db.session.commit()

    history = (
        Message.query
        .filter_by(mobile=mobile)
        .filter(Message.message != message)
        .order_by(Message.id.desc())
        .limit(5)
        .all()
    )

    history_list = [
        {"message": m.message, "category": m.category, "confidence": round(m.confidence, 2)
}
        for m in history
    ]

    return jsonify({
        "current_result": {
            "category": category,
            "confidence": round(confidence, 2)

        },
        "history": history_list
    })

if __name__ == '__main__':
    app.run(debug=True)