from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


# ============================================================
# Load Complete ML Pipeline
# ============================================================

model = joblib.load(
    "power_output_prediction_model.pkl"
)


# ============================================================
# Home Page
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# Prediction API
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        print("Received data:", data)

        AT = float(data["AT"])
        V = float(data["V"])
        AP = float(data["AP"])
        RH = float(data["RH"])

        input_data = pd.DataFrame(
            [[AT, V, AP, RH]],
            columns=[
                "AT",
                "V",
                "AP",
                "RH"
            ]
        )

        print("Input:")
        print(input_data)

        prediction = model.predict(
            input_data
        )[0]

        print(
            "Predicted Power Output:",
            prediction
        )

        return jsonify({
            "prediction": round(
                float(prediction),
                2
            )
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 400


# ============================================================
# Run Flask
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=True
    )