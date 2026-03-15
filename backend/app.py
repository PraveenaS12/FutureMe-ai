from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "model.pkl"))

try:
    model = joblib.load(model_path)
    MODEL_LOADED = True
except Exception:
    MODEL_LOADED = False
    print("model.pkl not found — using fallback simulation")


def simulate_fallback(sleep, study, screen, exercise, stress):
    sn  = (sleep - 1) / 11
    stn = study / 10
    scn = 1 - (screen / 14) * 0.75
    exn = exercise / 5
    srn = 1 - (stress - 1) / 9 * 0.85
    focus        = max(18, min(95, int((sn*35 + stn*25 + scn*20 + srn*20) * 0.9)))
    energy       = max(12, min(95, int((sn*40 + exn*30 + srn*20 + scn*10) * 0.9)))
    productivity = max(18, min(95, int((sn*35 + stn*30 + scn*15 + srn*20) * 0.9)))
    burnout      = max(5,  min(92, int((1-srn)*40 + (1-sn)*25 + (1-exn)*15 + (18 if scn < 0.4 else 4))))
    return focus, energy, productivity, burnout


@app.route("/")
def home():
    return "FutureMe AI Backend Running"


@app.route("/predict", methods=["POST"])
def predict():
    data        = request.json
    sleep       = float(data.get("sleep", 7))
    study       = float(data.get("study", 3))
    screen      = float(data.get("screen", 5))
    exercise    = float(data.get("exercise", 1))
    stress      = float(data.get("stress", 4))
    future_year = int(data.get("futureYear", 1))

    if MODEL_LOADED:
        pred         = model.predict([[sleep, study, screen, exercise, stress]])[0]
        focus, energy, productivity, burnout = float(pred[0]), float(pred[1]), float(pred[2]), float(pred[3])
    else:
        focus, energy, productivity, burnout = simulate_fallback(sleep, study, screen, exercise, stress)

    gf = 1 + future_year * 0.15
    br = max(0.1, 1 - future_year * 0.05)
    focus        = max(0, min(100, int(focus * gf)))
    energy       = max(0, min(100, int(energy * gf)))
    productivity = max(0, min(100, int(productivity * gf)))
    burnout      = max(0, min(100, int(burnout * br)))

    if productivity < 50:
        advice = f"In {future_year} year(s), productivity may drop. Increase focused study time."
    elif burnout > 70:
        advice = f"Burnout risk in {future_year} year(s)! Improve sleep & reduce stress."
    elif energy < 40:
        advice = f"Energy may decline in {future_year} year(s). Add daily exercise."
    else:
        advice = f"In {future_year} year(s), you are on a powerful growth trajectory!"

    return jsonify({"focus": focus, "energy": energy, "productivity": productivity, "burnout": burnout, "advice": advice})


@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "").lower()
    if "sleep" in msg:       reply = "Adequate sleep (7-8 hrs) dramatically improves focus and energy."
    elif "stress" in msg:    reply = "Box breathing (4s in, 4s hold, 4s out) lowers cortisol within minutes."
    elif "study" in msg:     reply = "Consistent study routines with proper breaks improve long-term productivity."
    elif "exercise" in msg:  reply = "Even 30 minutes of daily movement boosts energy by 20-40%."
    elif "screen" in msg:    reply = "Under 4h screen time per day improves sleep quality by ~25%."
    else:                    reply = "Tell me more about your habits so I can give tailored advice!"
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
