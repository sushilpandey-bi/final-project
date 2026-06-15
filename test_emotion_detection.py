import requests

def test_emotion_detection(text_analyze):

    url = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")

    payload = { "raw_document": {"text": text_analyze}}

    headers = {"grpc-metadata-mm-model-id":"emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=10
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    result = response.json()

    emotions = result["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
