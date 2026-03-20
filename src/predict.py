import os
import pandas as pd
import joblib
from scipy.sparse import hstack

from preprocess import load_data, preprocess
from decision_engine import decide_action
from uncertainty import compute_uncertainty


def predict():

    # -------------------------
    # 0. Ensure output folder
    # -------------------------
    os.makedirs("outputs", exist_ok=True)


    # -------------------------
    # 1. Load test data
    # -------------------------
    df = load_data("data/arvyax_test_inputs_120.xlsx - Sheet1.csv")

    # -------------------------
    # 2. Load models + tools
    # -------------------------
    model_state = joblib.load("models/state_model.pkl")
    model_intensity = joblib.load("models/intensity_model.pkl")
    tfidf = joblib.load("models/tfidf.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_columns = joblib.load("models/feature_columns.pkl")

    # -------------------------
    # 3. Preprocess test data
    # -------------------------
    X_text, X_meta, _, _, _ = preprocess(
        df,
        fit=False,
        tfidf=tfidf,
        scaler=scaler,
        feature_columns=feature_columns
    )

    X = hstack([X_text, X_meta])

    # -------------------------
    # 4. Predictions
    # -------------------------
    state_preds = model_state.predict(X)
    intensity_preds = model_intensity.predict(X)

    # Optional: round intensity to 1–5
    intensity_preds = intensity_preds.round().clip(1, 5)

    print("State preds:", len(state_preds))
    print("Intensity preds:", len(intensity_preds))
    # -------------------------
    # 5. Uncertainty
    # -------------------------
    confidence, uncertain_flag = compute_uncertainty(
        model_state, X, intensity_preds
    )

    # -------------------------
    # 6. Decision Engine
    # -------------------------
    actions = []
    timings = []

    for i in range(len(df)):

        energy = df.loc[i, 'energy_level'] if 'energy_level' in df else 3
        stress = df.loc[i, 'stress_level'] if 'stress_level' in df else 3
        time_of_day = df.loc[i, 'time_of_day'] if 'time_of_day' in df else "unknown"

        action, timing = decide_action(
            state_preds[i],
            intensity_preds[i],
            energy,
            stress,
            time_of_day
        )

        actions.append(action)
        timings.append(timing)

    # -------------------------
    # 7. Save output
    # -------------------------
    output = pd.DataFrame({
        "id": df["id"],
        "predicted_state": state_preds,
        "predicted_intensity": intensity_preds,
        "confidence": confidence,
        "uncertain_flag": uncertain_flag,
        "what_to_do": actions,
        "when_to_do": timings
    })
    print("Output preview:")
    print(output.head())
    output.to_csv("outputs/predictions.csv", index=False)

    print("✅ Predictions saved to outputs/predictions.csv")


if __name__ == "__main__":
    predict()