from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import traceback
import pandas as pd

import pickle

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

MODEL_FEATURES = [
    "plusMinus",
    "Position",
    "G",
    "A1",
    "GP",
    "Grit",
    "TOI%",
    "xGA",
    "xGF",
]
ID_FEATURES = ["First Name", "Last Name", "Team"]


@app.route("/")
def home():
    html = "<h3>Sklearn Random Forest Predict NHL Player Salary: Hosted by Azure</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Performs predictions on static test data."""

    try:
        with open("simple_pipeline_clf.pkl", "rb") as f:
            clf = pickle.load(f)

    except Exception as e:
        LOG.error(f"Error loading model: {e}")
        LOG.error(f"Exception traceback: {traceback.format_exc()}")
        return "Model was not loaded"

    json_payload = request.json
    sample_prediction_records = pd.DataFrame(json_payload)

    preds = clf.predict(sample_prediction_records[MODEL_FEATURES])

    # return render_template(
    #     "view.html",
    #     tables=[sample_prediction_records[ID_FEATURES + ["preds"]].to_html()],
    #     titles="RF Salary Predictions",
    # )
    return jsonify({"predictions": list(preds)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
