from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
CATEGORIES = ["emergency", "routine", "follow-up", "other"]

def classify_message(text):
    result = classifier(text, CATEGORIES)
    return result['labels'][0], float(result['scores'][0])