"""
 This is a server.py opens a port, calls emotion detector and fails to recognize status code
 other than 200.... im done, i give up, i dont understand how is crap does not work
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emot_analyzer():
    """
        get docstrings
    """
    # Retrieve the text to analyze from the request arguments

    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    dominant_emotion = result["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid input! Try again."
    return f"The given text represents {dominant_emotion}"

@app.route("/")
def render_index_page():
    """
        get docstrings
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
