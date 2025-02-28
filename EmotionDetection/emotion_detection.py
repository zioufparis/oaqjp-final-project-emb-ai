import requests
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    data = response.json()
    # Extract emotions from the response
    emotion_scores = data["emotionPredictions"][0]["emotion"]
    # Extract the required emotions and their scores
    anger_score = emotion_scores.get("anger", 0)
    disgust_score = emotion_scores.get("disgust", 0)
    fear_score = emotion_scores.get("fear", 0)
    joy_score = emotion_scores.get("joy", 0)
    sadness_score = emotion_scores.get("sadness", 0)
    emotions = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }


