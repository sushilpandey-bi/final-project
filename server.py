from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotions.
    """

    text_to_analyze = request.args.get(
        "textToAnalyze"
    )

    response = emotion_detector(
        text_to_analyze
    )

    if response["dominant_emotion"] is None:
        return (
            "Invalid text! "
            "Please try again."
        )

    return (
        f"For the given statement, "
        f"the system response is "
        f"{response}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
