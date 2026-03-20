import numpy as np

def compute_uncertainty(model_state, X, pred_intensity):

    probs = model_state.predict_proba(X)

    confidence = probs.max(axis=1)

    uncertain_flag = (confidence < 0.6).astype(int)

    return confidence, uncertain_flag