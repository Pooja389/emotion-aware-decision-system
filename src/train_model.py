import os
import joblib
from scipy.sparse import hstack
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from preprocess import load_data, preprocess


def train():

    # Ensure folders exist
    os.makedirs("models", exist_ok=True)

    #-------------------------------------------------- 1. Load data -------------------------------------
    df = load_data("data/Sample_arvyax_reflective_dataset.xlsx - Dataset_120.csv")

    #print(df.columns)
    #print("Test shape:", df.shape)
    #print(df.head(2))

    #-------------------------------------------------- 2. Preprocess---------------------------------------
    X_text, X_meta, tfidf, scaler, feature_columns = preprocess(df, fit=True)

    # Combine text + metadata
    X = hstack([X_text, X_meta])

    # Targets
    y_state = df['emotional_state']
    y_intensity = df['intensity']

    
    #------------------------------------------------ 3. Train models---------------------------------------
    model_state = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model_intensity = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model_state.fit(X, y_state)
    model_intensity.fit(X, y_intensity)


    #----------------------------------------------- 4. Save models----------------------------------------

    joblib.dump(model_state, "models/state_model.pkl")
    joblib.dump(model_intensity, "models/intensity_model.pkl")
    joblib.dump(tfidf, "models/tfidf.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(feature_columns, "models/feature_columns.pkl")

    print("✅ Training complete. Models saved in /models")


if __name__ == "__main__":
    train()