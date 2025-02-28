from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detector_route():
    # Retrieve the text to analyze from the query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: No text provided", 400

    # Call the emotion_detector function to get the analysis
    response = emotion_detector(text_to_analyze)

    # Format the result as the desired plain-text response
    result = (
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']}, "
        f"sadness: {response['sadness']}, "
        f"dominant_emotion: {response['dominant_emotion']}"
    )
    return result
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
